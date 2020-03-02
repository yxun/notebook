
# Design Pastebin.com (or Bit.ly)

## Step 1: Outline use cases and constraints

### Use cases
- User enters a block of text and gets a randomly generated link
  - Expiration
    - Default setting does not expire
    - Can optionally set a timed expiration
- User enters a paste's url and views the contents
- User is anonymous
- Service tracks analytics of pages
  - Monthly visit stats
- Service deletes expired pastes
- Service has high availability

### Out of scope
- User registers for an account
  - User verifies email
- User logs into a registered account
  - User edits the document
- User can set visibility
- User can set the shortlink

### Constraints and assumptions
Assumptions
- Traffic is not evenly distributed
- Following a short link should be fast
- Pastes are text only
- Page view analytics do not need to be realtime
- 10 million users
- 10 million paste writes per month
- 100 million paste reads per month
- 10:1 read to write ratio

Calculate usage
- Size per paste
  - 1 KB content per paste
  - shortlink 7 bytes
  - expiration_lenght_in_minutes 4 bytes
  - created_at 5 bytes
  - paste_path 255 bytes
  - total ~1.27 KB
- 12.7 GB of new paste content per month
- 4 paste writes per second on average
- 40 read requests per second on average


## Step 2: Create a high level design

![](./img/pastebin1.png)


## Step 3: Design core components
> Dive into details for each use case.

### Use case: User enters a block of text and gets a randomly generated link
We could use a `relational database` or a `NoSQL key-value store` as a large hash table, mapping the generated url to a `file server` or an `Object Store` (e.g. Amazon S3 or a NoSQL document store) and path containing the paste file.

- The `Client` sends a create paste request to the `Web Server`, running as a `reverse proxy`.
- The `Web Server` forwards the request to the `Write API server`.
- The `Write API server` does the following:
  - Generates a unique url.
    - Checks if the url is unique by looking at the `SQL Database`.
    - If the url is no unique, it generates another url.
    - If we supported a custom url, we could use the user-supplied (also check for duplicate).
  - Saves to the SQL Database `pastes` table.
  - Saves the paste data to the `Object Store`.
  - Returns the url.

**Example code**

The `paste` table could have the following structure:

```
shortlink char(7) NOT NULL
expiration_length_in_minutes int NOT NULL
created_at datetime NOT NULL
paste_path varchar(255) NOT NULL
PRIMARY KEY (shortlink)
```

We'll create an index on `shortlink` and `created_at` to speed up lookups (log-time instead of scanning the entire table) and to keep the data in memory.

To generate the unique url:
- Take the MD5 hash of randomly-generated data or the user's ip address + timestamp.
  - MD5 hashing function that produces a 128-bit hash value.
  - MD5 is uniformly distributed.
- Base 62 encode the MD5 hash.
  - Base 62 encodes to [a-zA-Z0-9] which works well for urls, eliminating the need for escaping special characters.
  - Base 62 is deterministic (no randomness).
  - Base 64 is another encoding but provides issues for urls because of + and / characters.
  - Base 62 (the following) runs in O(k) time where k is the number of digits = 7:

```python
def base_encode(num, base=62):
    digits = []
    while num > 0:
        remainder = modulo(num, base)
        digits.push(remainder)
        num = divide(num, base)
    digits = digits.reverse
```

```python
url = base_encode(md5(ip_address+timestamp))[:URL_LENGTH]
```

Define a public REST API:

```bash
$ curl -X POST --data '{ "expiration_length_in_minutes": "60", \
    "paste_contents": "Hello World!" }' https://pastebin.com/api/v1/paste 
```

Response

```
{
    "shortlink": "foobar"
}
```

For internal communications, we could use Remote Procedure Calls.


### Use case: User enters a paste's url and views the contents

- The `Client` sends a get paste request to the `Web Server`.
- The `Web Server` forwards the request to the `Read API` server.
- The `Read API` server does the following:
  - Checks the `SQL Database` for the generated url.
    - If the url is in the `SQL Database`, fetch the paste contents from the `Object Store`.
    - Else, return an error message for the user.

REST API
```bash
$ curl https://pastebin.com/api/v1/paste?shortlink=foobar
```

Response
```
{
    "paste_contents": "Hello World"
    "created_at": "YYYY-MM-DD HH:MM:SS"
    "expiration_length_in_minutes": "60"
}
```

### Use case: Service tracks analytics of pages
MapReduce the Web Server logs to generate hit counts.

```python
...

def reducer(self, key, values):
    """Sum values for each key"""
    yield key, sum(values)

```

### Use case: Service deletes expired pastes
Scan the SQL Database for all entries whose expiration timestamp are older than the current timestamp.


## Step 4: Scale the design
> Identify and address bottlenecks, given the constraints.

![](./img/pastebin2.png)

**Do not simply jump right into the final design from the initial design**

Iteratively scale the initial design:
- Benchmark/Load Test.
- Profile for bottlenecks.
- Address bottlenecks while evaluating alternatives and trade-offs.

The Analytics Database could use a data warehousing solution such as Amazon Redshift or Google BigQuery.

To address the 40 average read requests per second, traffic for popular content should be handled by the Memory Cache. The SQL Read Replicas should be able to handle the cache misses.
Average paste writes per second should be do-able for a single SQL Write Master-Slave. Otherwise, employ additional SQL scaling patterns such as Federation, Sharding, Denormalization, SQL Tuning.

