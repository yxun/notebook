
# Design Mint.com

## Use cases
- User connects to a financial account
- Service extracts transactions from the account
  - Updates daily
  - Categorizes transactions
    - Allows manual category override by the the user
    - No automatic re-categorization
  - Analyzes monthly spending, by category
- Service recommends a budget
  - Allows users to manually set a budget
  - Sends notifications when approaching or exceeding budget
- Service has high availability

### Out of scope
Service performs additional logging and analytics

## Constraints and assumptions
### State assumptions
- Traffic is not evenly distributed
- Automatic daily update of accounts applies only to users active in the past 30 days
- Adding or removing financial accounts is relatively rare
- Budget notifications don't need to be instant
- 10 million users
  - 10 budget categories per user = 100 million budget items
  - Example categories:
    - Housing = $1000
    - Food = $200
    - Gas = $100
  - Sellers are used to determine transaction category
    - 50000 sellers
- 30 million financial accounts
- 5 billion transactions per month
- 500 million read requests per month
- 10:1 write to read ration
  - Write-heavy, users make transactions daily, but few visit the site daily

### Calculate usage
- Size per transaction
  - user_id - 8 bytes
  - created_at - 5 bytes
  - seller - 32 bytes
  - amount - 5 bytes
  - Total ~50 bytes
- 250 GB of new transaction content per month
  - 50 bytes per transaction * 5 billion transactions per month
  - 9 TB of new transaction content in 3 years
  - Assume most are new transactions instead of updates to existing ones
- 2000 transactions per second on average
- 200 read requests per second on average

## Create a high level design

![](./img/mint1.png)

## Design core components
### Use case: User connects to a financial account
We could store info on the 10 million users in a relational database.
- The Client sends a request to the Web Server, running as a reverse proxy
- The Web Server forwards the requests to the Accounts API server
- The Accounts API server updates the SQL Database accounts table with the newly entered info

The `accounts` table
```
id int NOT NULL AUTO_INCREMENT
created_at datetime NOT NULL
last_update datetime NOT NULL
account_url varchar(255) NOT NULL
account_login varchar(32) NOT NULL
user_id int NOT NULL
PRIMARY KEY(id)
FOREIGN KEY(user_id) REFERENCES users(id)
```

We can create an index on `id`, `user_id`, and `created_at` to speed up lookups.

REST API
```
curl -X POST --data '{ "user_id": "foo", "account_url": "bar", \
    "account_login": "baz", "account_password": "qux" }' \
    https://mint.com/api/v1/account
```

### Use case: Service extracts transactions from the account
Extract information from an account in these cases:
- The user first links the account
- The user manually refreshes the account
- Automatically each day for users who have been active in the past 30 days

Data flow:
- The Client sends a request to the Web Server
- The Web Server forwards the request to the Accounts API server
- The Accounts API server places a job on a Queue 
- The Transaction Extraction Service does the following:
  - Pulls from the Queue and extracts transactions for the given account from the financial institution, storing the results as raw log files in the Object Store.
  - Uses the Category Service to categorize each transaction
  - Uses the Budget Service to calculate aggregate monthly spending by category
    - The Budget Service uses the Notification Service
  - Updates the SQL Database `transactions` table with categorized transactions
  - Updates the SQL Database `monthly_spending` table with aggregate monthly spending by category
  - Notifies the user the transactions have completed through the Notification Service
    - Uses a Queue to asynchronously send out notifications

The `transactions` table
```
id int NOT NULL AUTO_INCREMENT
created_at datetime NOT NULL
seller varchar(32) NOT NULL
amount decimal NOT NULL
user_id int NOT NULL
PRIMARY KEY(id)
FOREIGN KEY(user_id) REFERENCES users(id)
```

We can index on `id`, `user_id` and `created_at`

The `monthly_spending` table
```
id int NOT NULL AUTO_INCREMENT
month_year date NOT NULL
category varchar(32)
amount decimal NOT NULL
user_id int NOT NULL
PRIMARY KEY(id)
FOREIGN KEY(user_id) REFERENCES users(id)
```

We can index on `id` and `user_id`

#### Category service
We can seed a seller-to-category dictionary.

```python
class DefaultCategories(Enum):
    HOUSING = 0
    FOOD = 1
    GAS = 2
    SHOPPING = 3
    ...

seller_category_map = {}
seller_category_map['Exxon'] = DefaultCategories.GAS
seller_category_map['Target'] = DefaultCategories.SHOPPING
```

We could use a heap to quickly lookup the top manual override per seller.

Transaction
```python
class Transaction(object):

    def __init__(self, created_at, seller, amount):
        self.timestamp = timestamp
        self.seller = seller
        self.amount = amount
```

### Use case: Service recommends a budget

```python
class Budget(object):

    def __init__(self, income):
        self.income = income
        self.categories_to_budget_map = self.create_budget_template()

    def create_budget_template(self):
        return {
            'DefaultCategories.HOUSING': income * .4,
            'DefaultCategories.FOOD': income * .2,
            'DefaultCategories.GAS': income * .1,
            'DefaultCategories.SHOPPING': income * .2
            ...
        }

    def override_category_budget(self, category, amount):
        self.categories_to_budget_map[category] = amount

```

For the Budget Service, we can run SQL queries on the transactions table to generate the monthly_spending aggregate table. 

As an alternative, we can run MapReduce jobs on the raw transaction files to:
- Categorize each transaction
- Generate aggregate monthly spending by category

## Scale the design

![](./img/mint2.png)

- The Read API server does the following
  - Checks the Memory Cache for the content
    - If the url is in the Memory Cache, returns the cached contents
    - Else
      - If the url is in the SQL Database, fetches the contents
        - Updates the Memory Cache with the contents

The SQL Read Replicas should be able to handle the cache misses.
