
## Requirements and Goals of the system

### Functional Requirements
1. Given a URL, our service should generate a shorter and unique alias of it.
2. When users access a short link, our service should redirect them to the original link.
3. Users should optionally be able to pick a custom short link for their URL.
4. Links will expire after a standard default timespan. Users should be able to specify the expiration time.

### Non-funcational Requirements
1. The system should be highly available.
2. URL redirection should happen in real-time with minimal latency.
3. Shortened links should not be predictable.

## Capacity estimation and Constraints
Our system will be read-heavy. There will be lots of redirection requests compared to new URL shortenings.
Let's assume a 100:1 ratio between read and write.

### Traffic estimates
Assume 500M new URL shortenings per month. 100 * 500M => 50B redirections per month.
Queries per seconds (QPS) New URLs shortenings: 500M / (30 days * 24 hours * 3600 seconds) =~ 200 URLs/s
URL redirection 100 * 200 URLs/s = 20K/s

### Storage estimates
Let's assume we store every URL shortening request and associated shortened link for 5 years.
500M * 12 months * 5 years = 30 billion objects(files)

Let's assume that each stored object will be approximately 500 bytes. We will need 15TB storage.

### Bandwidth estimates
For write requests, expect 200 URLs/s, incoming data will be 200 * 500 bytes = 100 KB/s
For read requests, expect ~20K URLs redirections, outgoing data will be 20K * 500 bytes =~ 10MB/s

### Memory estimates
cache some of the hot URLs that are frequently accessed. If we follow the 80-20 rule, 20% URLs generate 80% traffic. 20K * 3600 seconds * 24 hours = ~1.7billion per day
To cache 20% of these requests, will need 170GB of memory: 0.2 * 1.7 billion * 500 bytes = ~170GB

there will be a lot of duplicate requests, therefore our actual memory usage will be less than 170GB

### High level estimates
New URLs            200/s
URL redirections    20K/s
Incoming data       100KB/s
Outgoing data       10MB/s
Storage for 5 years 15TB
Memory for cache    170GB

## System APIs
REST APIs. creating and deleting URLs:

createURL(api_dev_key string, original_url string, custom_alias string, user_name string, expire_date string) (string, error)

Parameters:
api_dev_key (string): The API developer key of a registered account. This will be used to, among other things, throttle users based on their allocated quota.
original_url (string): Original URL to be shortened.
custom_alias (string): Optional custom key for the URL.
user_name (string): Optional user name to be used in the encoding.
expire_date (string): Optional expiration date for the shortened URL.

Returns: (string)
A successful insertion returns the shortened URL; otherwise, it returns an error code.

deleteURL(api_dev_key string, url_key string)

How do we detect and prevent abuse? A malicious user can put us out of business by consuming all URL keys in the current design. To prevent abuse, we can limit users via their api_dev_key. Each api_dev_key can be limited to a certain number of URL creations and redirections per some time period (which may be set to a different duration per developer key).

## Database Design
1. We need to store billions of records.
2. Each object we store is small (less than 1K)
3. There are no relationships between records, other than storing which user created a URL.
4. read-heavy

### Database Schema
need two tables: one for the URL mappings, and one for the user's data who created the short link

URL
PK Hash varchar(16)
OriginalURL: varchar(512)
CreationDate: datetime
ExpirationDate: datetime
UserID: int

User
PK UserID: int
Name: varchar(20)
Email: varchar(32)
CreationDate: datetime
LastLogin: datetime

What kind of database should we use? Since we anticipate storing billions of rows, and we don’t need to use relationships between objects – a NoSQL store like DynamoDB, Cassandra or Riak is a better choice. A NoSQL choice would also be easier to scale. Please see SQL vs NoSQL for more details.

## Basic system design and Algorithm

a. Encoding actual URL
We can compute a unique hash (e.g. MD5 or SHA256, etc.) of the given URL. This encoding could be base36 ([a-z,0-9]) or base62 ([A-Z,a-z,0-9]) and if we add '+' and '/' we can use Base64 encoding.

Using base64 encoding, a 6 letters long key would result in 64^6 = ~68.7 billion possible strings
Let's assume six letter keys would suffice.

If we use the MD5 algorithm, it'll produce a 128-bit hash value. After base64 encoding, we'll get a string having more than 21 characters.

b. Generating keys offline
We can have a standalone Key Generation Service (KGS) that generates random six-letter strings beforehand and 
stores them in a database. Whenever we want to shorten a URL, we will just take one of the already-generated keys.
As soon as a key is used, it should be marked in the database to ensure it doesn't get reuse. KGS can use two tables to store keys: one for keys that are not used yet, and one for all the used keys.

With base64 encoding, we can generate 68,7B unique six letters keys. 6 characters per key * 68.7B = 412 GB

KGS is a single point of failure. We can have a standby replica of KGS.

## Data Partitioning and Replication
To scale out our DB, we need to partition it so that it can store information about billions of URLs.

a. Range Based Partitioning
We can store URLs in separate partitions based on the first letter of the hash key. The main problem is that it can lead to unbalanced DB servers.

b. Hash-Based Partitioning

## Cache
Memcached, Redis

Which cache eviction policy would best fit our needs? When the cache is full, and we want to replace a link with a newer/hotter URL, how would we choose? Least Recently Used (LRU) can be a reasonable policy for our system. Under this policy, we discard the least recently used URL first. We can use a Linked Hash Map or a similar data structure to store our URLs and Hashes, which will also keep track of the URLs that have been accessed recently.

## Load Balancer
1. Between Clients and Applications servers
2. Between Application Servers and database servers
3. Between Application Servers and Cache servers

Round Robin approach. Another benefit of this approach is that if a server is dead, LB will take it out of the rotation and will stop sending any traffic to it. A problem with Round Robin LB is that we don’t take the server load into consideration.

## Purging or DB cleanup

A separate Cleanup service can run periodically to remove expired links from our storage and cache. This service should be very lightweight and can be scheduled to run only when the user traffic is expected to be low.
After removing an expired link, we can put the key back in the key-DB to be reused.

## Telemetry

## Security and Permissions

