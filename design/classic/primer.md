
# Reference
[The System Design Primer](https://github.com/donnemartin/system-design-primer)


### How to approach system design questions

#### Step 1: Outline use cases, constraints, and asumptions

- Who is going to use it ?
- How are they going to use it ?
- How many users are there ?
- What does the system do ?
- What are the inputs and outputs of the system ?
- How much data do we expect to handle ?
- How many requests per second do we expect ?
- What is the expected read to write ratio ?


#### Step 2: Create a high level design

- Sketch the main components and connections
- Justify your ideas


#### Step 3: Design core components

For example, design a url shortening service:

- Generating and storing a hash of the full url
  - MD5 and Base62
  - Hash collisions
  - SQL or NoSQL
  - Database schema
- Translating a hashed url to the full url
  - Database lookup
- API and object-oriented design


#### Step 4: Scale the design

For example, do you need the following to address scalability issues ?

- Load balancer
- Horizontal scaling
- Caching
- Database sharding

Discuss pros and cons. Everything is a trade-off.


#### Step 5: Performance estimation

- Use back of the envelope calculations
- Powers of two table
- Latency numbers


### System design example questions

- Design Pastebin.com (or Bit.ly)
- Design the Twitter timeline and search (or Facebook feed and search)
- Design a web crawler
- Design Mint.com
- Design the data structures for a social network
- Design a key-value store for a search engine
- Design Amazon's sales ranking by category feature
- Design a system that scales to millions of users on AWS


### Object-oriented design example questions

- Design a hash map
- Design a least recently used cache
- Design a call center
- Design a deck of cards
- Design a parking lot
- Design a chat server
- Design a circular array

# Performance vs scalability

- If you have a performance problem, your system is slow for a single user.
- If you have a scalability problem, your system is fast for a single user but slow under heavy load.

# Latency vs throughput

- Latency is the time to perform some action or to produce some result.
- Throughput is the number of such actions or results per unit of time.

# Availability vs consistency

In a distributed computer system, you can only support two of the following guarantees:
- Consistency, Every read receives the most recent write or an error.
- Availability, Every request receives a response, without guarantee that it contains the most recent version of the information.
- Partition Tolerance, The system continues to operate despite arbitary partitioning due to network failures.

Networks are not reliable, so you'll need to support partition tolerance. You'll need to make a software tradeoff between consistency and availability.
CP is a good choice if your business needs require atomic reads and writes. AP is a good choice when the system needs to continue working despite external errors.

Reference: [A plain english introduction to CAP Theorem](http://ksat.me/a-plain-english-introduction-to-cap-theorem/)

## Consistency patterns

### Weak consistency
After a write, reads may or may not see it. Use cases such as video chat, realtime multiplayer games.

### Eventual consistency 
After a write, reads will eventually see it. Data is replicated asynchronously. Use cases such as DNS and email. Works well in highly available systems.

### Strong consistency
After a write, reads will see it. Data is replicated synchronously. Use cases such as file systems, RDBMSes. Works well in systems that need transactions.
  

## Availability patterns

### Fail-over
#### Active-passive
With active-passive fail-over, heartbeats are sent between the active and the passive server on standby. Only the active server handles traffic.

#### Active-active
Both servers are managing traffic, spreading the load between them.

#### Disadvantage(s): failover
- Fail-over adds more hardware and additional complexity.
- There is a potential for loss of data if the active system fails before any newly written data can be replicated to the passive.

### Replication
- Master-slave
- Master-master


# DNS
Domain name system

- NS record (name server): Specifies the DNS servers for your domain/subdomain.
- MX record (mail exchange): Specifies the mail servers for accepting messages.
- A record (address): Points a name to an IP address.
- CNAME (canonical): Points a name to another name or CNAME ( example.com to www.example.com) or to an A record.

Services such as CloudFlare and Route 53 provide managed DNS services.

## Disadvantage(s): DNS
- Accessing a DNS server introduces a slight delay.
- DNS server management could be complex and is generally managed by governments, ISPs, and large companies.
- DNS services have come under DDoS attack.


# CDN
Content delivery network

Generally, static files such as HTML/CSS/JS, photos, and videos are served from CDN. The site's DNS resolution will tell clients which server to contact.

## Push CDNs
Content is uploaded when it is new or changed, minimizing traffic, but maximizing storage.
Sites with a small amount of traffic or sites with content that isn't often updated work well with push CDNs.

## Pull CDNs
Pull CDNs grab new content from your server when the first user requests the content. 
This results in a slower requests until the content is cached on the CDN. A time-to-live(TTL) determines how long content is cached.
Pull CDNs minimizing storage space on the CDN, but can create redundant traffic.
Sites with heavy traffic work well with pull CDNs, as traffic is spread out more evenly with only recently-requested content remaining on the CDN.

## Disadvantage(s): CDN
- CDN costs could be significant depending on traffic.
- Content might be stale if it is updated before the TTL expires it.
- CDNs require changing URLs for static content to point to the CDN.


# Load balancer

Effective at:
- Preventing requests from going to unhealthy servers
- Preventing overloading resources
- Helping eliminate single points of failure

Additional benefits:
- SSL termination: Decrypt incoming requests and encrypt server responses so backend servers do not have to perform these potentially expensive operations.
  - Removes the need to install X.509 certificates on each server.
- Session persistence: Issue cookies and route a specific client's requests to same instance if the web apps do not keep track of sessions.

To protect against failures, it's common to setup multiple load balancers, either in active-passive or active-active mode.

Load balancers can route traffic based on:
- Random
- Least loaded
- Session/cookies
- Round robin or weighted round robin
- Layer 4
- Layer 7

## Layer 4 load balancing
Look at the transport layer information such as source, destination IP address, and ports in the header. Performing Network Address Translation (NAT).

## Layer 7 load balancing
Look at the application layer information such as contents of the header, message, and cookies.

## Horizontal scaling

Disadvantage(s): horizontal scaling
- Introduces complexity and involves cloning servers.
  - Servers should be stateless: they should not contain any user-related data like sessions or profile pictures.
  - Sessions can be stored in a centralized data store such as a database (SQL, NoSQL) or a persistent cache (Redis, Memcached).
- Downstream servers such as caches and databases need to handle more simultaneous connections as upstream servers scale out.

Disadvantage(s): load balancer
- The load balancer can become a performance bottleneck if it does not have enough resources or if it is not configured properly.
- It increased complexity.
- A single load balancer is a single point of failure, configuring multiple load balancers further increases complexity.


# Reverse proxy (web server)

Benefits:
- Increased security: Hide information about backend servers, blacklist IPs, limit number of connections per client.
- Increased scalability and flexibility: Clients only see the reverse proxy's IP, allowing you to scale servers or change their configuration.
- SSL termination: Decrypt incoming requests and encrypt server responses. Removes the need to install X.509 certificates on each server.
- Compression: Compress server responses
- Caching: Return the response for cached requests
- Static content: Serve static content directly such as HTML/CSS/JS, Photos, Videos.

Disadvantage(s): reverse proxy
- Increase complexity
- A single reverse proxy is a single point of failure.


# Application layer

Microservices: a suite of independently deployable, small, modular services.
Service Discovery: system such as Consul, Etcd, and Zookeeper can help services find each other by keeping track of registered names, addresses, and ports. Both Consul and Etcd have a built in key-value store.


# Database

## Relational database management system (RDBMS)

Transaction ACID:
- Atomicity: Each transaction is all or nothing.
- Consistency: Any transactions will bring the database from one valid state to another.
- Isolation: Executing transactions concurrently has the same results as if the transactions were executed serially.
- Durability: Once a transaction has been committed, it will remain so. 

Techniques to scale a relational database: 
master-slave replication, master-master replication, federation, sharding, denormalization, and SQL tuning.

### Master-slave replication
The master serves reads and writes, replicating writes to one or more slaves, which serve only reads.
Slaves can also replicate to additional slaves in a tree-like fashion. 
If the master goes offline, the system can contiune to operate in read-only mode until a slave is promoted to a master or a new master is provisioned.

Disadvantage(s): master-slave replication
- Additional logic is needed to promote a slave to a master
- Disadvantage(s): replication

Disadvatage(s): replication
- There is a potential loss of data if the master fails before any newly written data can be replicated.
- Writes are replayed to the read replicas. If there are a lot of writes, the read replicas can get bogged down with replaying writes and can't do as many reads.
- The more read slaves, the more you have to replicate, which leads to greater replication lag.
- On some systems, writing to the master can spawn multiple threads to write in parallel, whereas read replicas only support writing sequentially with a single thread.
- Replication adds more hardware and additional complexity.

### Master-master replication
Both masters serve reads and writes and coordinate with each other on writes.

Disadvantage(s): master-master replication
- Need a load balancer or need to make changes to your application logic to determine where to write.
- Most master-master systems are either loosely consistent (violating ACID) or have increased write latency due to synchronization.
- Conflict resolution comes more into play as more write nodes are added and as latency increases.
- Disadvantage(s): replication

### Federation
Federation (or functional partitioning) splits up databases by function. For example, instead of a single, monolithic database, you could have three databases: forums, users and products, resulting in less read and write traffic to each database and therefore less replication lag.

Disadvantage(s): federation
- Federation is not effective if your schema requires huge functions or tables.
- Need to update application logic to determine which database to read and write.
- Joining data from two databases is more complex with a server link.
- Adds more hardware and additonal complexity.

### Sharding
Sharding distributes data across different databases such that each database can only manage a subset of the data.

Disadvantage(s): sharding
- Need to update application logic to work with shards
- Data distribution can become lopsided in a shard.
- Joining data from multiple shards is more complex.
- Sharding adds more hardware and additional complexity.

### Denormalization
Denormalization attempts to improve read performance at the expense of some write performance. Redundant copies of data are written in multiple tables to avoid expensive joins.

Disadvantage(s):
- Data is duplicated.
- Constraints can help redundant copies of information stay in sync, which increases complexity of the database.
- A denormalized database under heavy write load might perform worse than its normalized counterpart.

### SQL tuning

Tighten up the schema
- Use CHAR instead of VARCHAR for fixed-length fields.
  - CHAR effectively allows for fast, random access, whereas with VARCHAR, you must find the end of a string before moving onto the next one.
- Use TEXT for large blocks of text such as blog posts. TEXT also allows for boolean searches. Using a TEXT field results in storing a pointer on disk that is used to locate the text block.
- Use INT for larger numbers up to 2^32
- Use DECIMAL for currency to avoid floating point representation errors.
- Avoid storing large BLOBS, store the location of where to get the object instead.
- VARCHAR(255) is the largest number of characters that can be counted in a 8 bit number, often maximizing the use of a byte in some RDBMS.
- Set the NOT NULL constraint where applicable to improve search performance.

Use good indices
- Columns that you are querying (SELECT, GROUP BY, ORDER BY, JOIN) could be faster with indices.
  - Indices are usually represented as self-balancing B-tree
- Placing an index can keep the data in memory, requiring more space.
- Writes could also be slower since the index also needs to be updated.
- When loading large amounts of data, it might be faster to disable indices, load the data, then rebuild the indices.

Avoid expensive joins: Denormalize where performance demands it.
Partition tables: Break up a table by putting hot spots in a separate table to help keep it memory.
Tune the query cache.


## NoSQL
NoSQL is a collection of data items represented in a key-value store, document store, wide column store or a graph database. Data is denormalized, and joins are generally done in the application code.
Most NoSQL stores lack true ACID transactions and favor eventual consistency.

In comparision with the CAP Theorem, BASE chooses availability over consistency.
- Basically available: The system gurantees availability.
- Soft state: the state of the system may change over time, even without input.
- Eventual consistency: the system will become consistent over a period of time, given that the system doesn't receive input during that period.

### Key-value store
> Abstrction: hash table

Key-value stores provide high performance and are often used for simple data models or for rapidly-changing data, such as an in-memory cache layer. Examples, Redis, Memcached.

### Document store
> Abstrction: key-value store with documents stored as values

A document store is centered around documents (XML, JSON, binary, etc), where a document stores all information for a given object. Documents are organized by collections, tags, metadata, or directories.
MongoDB and CouchDB also provide a SQL-like language to perform complex queries. DynamoDB supports both key-values and documents.
Document stores provide high flexibility and are often used for working with occasionally changing data.


### Wide column store
> Abstraction: nested map ColumnFamily<RowKey, Columns<ColKey, Value, Timestamp>>

A wide column store's basic unit of data is a column (name/value pair). A column can be grouped in column families. Super column families further group column families. 
You can access each column independently with a row key, and columns with the same row key form a row.
Each value contains a timestamp for versioning and for conflict resolution.

Google: Bigtable; Hadoop: HBase; Facebook: Cassandra

Wide column stores offer high availability and high scalability. They are often used for very large data sets.


### Graph database
> Abstraction: graph

In a graph database, each node is a record and each arc is a relationship between two nodes. Graph databases are optimized to represent complex relationships with many foreign keys or many-to-many relationships.


## SQL or NoSQL
Reasons for SQL:
- Structured data
- Strict schema
- Relational data
- Need for complex joins
- Transactions
- Clear patterns for scaling
- More established
- Lookups by index are very fast

Reasons for NoSQL:
- Semi-structured data
- Dynamic or flexible schema
- Non-relational data
- No need for complex joins
- Store many TB (or PB) of data
- Very data intensive workload
- Very high throughput for IOPS

Sample data well-suited for NoSQL:
- Rapid ingest of clickstream and log data
- Leaderboard or scoring data
- Temporary data, such as a shopping cart
- Frequently accessed ('hot') tables
- Metadata/lookup tables


# Cache

Client caching: OS or browser, server side, or in a distinct cache layer.

CDN caching

Web server caching: Reverse proxies, web servers.

Database caching

Application caching: In-memory caches such as Memcached and Redis.

Two cache general categories: database queries and objects:
- Row level
- Query-level
- Fully-formed serializable objects
- Fully-rendered HTML

Disadvatage(s): Caching at the database query level
- Hard to delete a cached result with complex queries
- If one piece of data changes such as a table cell, you need to delete all cached queries that might include the changed cell.

Caching at the object level
Suggestions of what to cache:
- User sessions
- Fully rendered web pages
- Activity streams
- User graph data

## When to update the cache
### Cache-aside
Cache-aside is also referred to as lazy loading.
The application does the following:
- Look for entry in cache, resulting in a cache miss
- Load entry from the database
- Add entry to cache
- Return entry

Example: Memcached

Disadvantage(s): cache-aside
- Each cache miss results in three trips, which can cause a noticeable delay.
- Data can become stale if it is updated in the database. This issue is mitigated by setting a TTL which forces an update of the cache entry, or by using write-through.
- When a node fails, it is replaced by a new, empty node, increasing latency.

### Write-through
The application uses the cache as the main data store, reading and writing data to it, while the cache is responsible for reading and writing to the database:
- Application adds/updates entry in cache
- Cache synchronously writes entry to data store
- Return

Disadvantage(s): write through
- When a new node is created due to failure or scaling, the new node will not cache entries until the entry is updated in the database. Cache-aside in conjunction with write through can mitigate this issue.
- Most data written might never be read, which can be minimized with a TTL.

### Write-behind (write-back)
The application does the following:
- Add/update entry in cache
- Cache adds an event to queue. 
- Event processor asynchronously write entry to the data store.

Disadvantage(s): write-behind
- There could be data loss if the cache goes down prior to its contents hitting the data store.
- It is more complex to implement write-behind than it is to implement cache-aside or write-through.

### Refresh-ahead
The cache automatically refresh any recently accessed cached entry prior to its expiration.
Refresh-ahead can result in reduced latency vs read-through if the cache can accurately predict which items are likely to be needed in the future.

Disadvantage(s): refresh-ahead
- Not accurately predicting which items are likely to be needed in the future can result in reduced performance.

Disadvantage(s): cache
- Need to maintain consistency between caches and the source of truth such as the database through cache invalidation.
- Cache invalidation is a difficult problem, there is additional complexity associated with when to update the cache.
- Need to make application changes such as adding Redis or memcached.


# Asynchronism

## Message queues
Message queue workflow:
- An application publishes a job to the queue, then notifies the user of job status.
- A worker picks up the job from the queue, processes it, then signals the job is complete.

Examples: Redis, RabbitMQ, Amazon SQS

### Task queues
Example: Celery

### Back pressure
If queues start to grow significantly, the queue size can become larger than memory, resulting in cache misses, disk reads. Back pressure can help by limiting the queue size.


# Communication
OSI 7 Layer Model

Application (7): User applications such as SMTP
Presentation (6): Syntax layer such as JPEG/ASCII, TIFF/GIF
Session (5): Sync and send to logical ports, e.g. RPC/SQL/NFS
Transport (4): TCP host to host, e.g. TCP/UDP
Network (3): Packets, e.g. Routers IP/ICMP
Data Link (2): Frames, switch Bridge WAP
Physical (1): Cables, hubs, etc.


# Security

- Encrypt in transit and at rest.
- Sanitize all user inputs or any input parameters exposed to user to prevent XSS and SQL injection.
- Use Parameterized queries to prevent SQL injection.
- Use the principle of least privilege.

# Appendix

## Powers of two table
```
Power           Exact Value         Approx Value        Bytes
---------------------------------------------------------------
7                             128
8                             256
10                           1024   1 thousand           1 KB
16                         65,536                       64 KB
20                      1,048,576   1 million            1 MB
30                  1,073,741,824   1 billion            1 GB
32                  4,294,967,296                        4 GB
40              1,099,511,627,776   1 trillion           1 TB
```

## Latency numbers
```
Latency Comparison Numbers
--------------------------
L1 cache reference                           0.5 ns
Branch mispredict                            5   ns
L2 cache reference                           7   ns                      14x L1 cache
Mutex lock/unlock                           25   ns
Main memory reference                      100   ns                      20x L2 cache, 200x L1 cache
Compress 1K bytes with Zippy            10,000   ns       10 us
Send 1 KB bytes over 1 Gbps network     10,000   ns       10 us
Read 4 KB randomly from SSD*           150,000   ns      150 us          ~1GB/sec SSD
Read 1 MB sequentially from memory     250,000   ns      250 us
Round trip within same datacenter      500,000   ns      500 us
Read 1 MB sequentially from SSD*     1,000,000   ns    1,000 us    1 ms  ~1GB/sec SSD, 4X memory
Disk seek                           10,000,000   ns   10,000 us   10 ms  20x datacenter roundtrip
Read 1 MB sequentially from 1 Gbps  10,000,000   ns   10,000 us   10 ms  40x memory, 10X SSD
Read 1 MB sequentially from disk    30,000,000   ns   30,000 us   30 ms 120x memory, 30X SSD
Send packet CA->Netherlands->CA    150,000,000   ns  150,000 us  150 ms

Notes
-----
1 ns = 10^-9 seconds
1 us = 10^-6 seconds = 1,000 ns
1 ms = 10^-3 seconds = 1,000 us = 1,000,000 ns
```

- Read sequentially from disk at 30 MB/s
- Read sequentially from 1 Gbps Ethernet at 100 MB/s
- Read sequentially from SSD at 1 GB/s
- Read sequentially from main memory at 4 GB/s
- 6-7 world-wide round trips per second
- 2000 round trips per second within a data center
