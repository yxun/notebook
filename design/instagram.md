
## Requirements and Goals

### Functional Requirements
1. Users should be able to upload/download/view photos
2. Users can perform searches based on photo/video titles
3. Users can follow other users
4. The system should be able to generate and display a user's News Feed consisting of top photos from all the people the user follows

### Non-functional Requirements
1. Our service needs to be highly available
2. The acceptable latency of the system is 200ms for News Feed generation
3. Consistency can take a hit, if a user doesn't see a photo for a while, it should be fine
4. The system should be highly reliable, any uploaded photo or video should never be lost

### Design Considerations
ready-heavy
1. Efficient management of storage should be a crucial factor
2. Low latency is expected while viewing photos
3. Data should be 100% reliable

## Capacity estimation and Constraints

Assume 500M total users, with 1M daily active users
2M new photos per day, 23 new photos per second
Average photo file size =~ 200KB
Total space per day 2M * 200KB =~ 400GB
Total space for 10 years 400GB * 365 * 10 =~ 1425TB

## High level system design
two use cases, one to upload photos and the other to view/search photos
object storage to store photos and database to store metadata

## Database Schema

Photo
PK PhotoID: int
UserID: int
PhotoPath: varchar(256)
CreationDate: datetime

User
PK UserID: int
Name: varchar(20)
Email: varchar(32)
DateOfBirth: datetime
CreationDate: datetime
LastLogin: datetime

UserFollow
UserID1: int
UserID2: int

We can store photos in a distributed file storage like HDFS or S3

## Data size estimation
Assume each int and dateTime is four bytes, each row in the User's table will be 68 bytes
If we have 500M users, we will need 32GB of total storage

Each row in Photo's table will be of 284 bytes
If 2M new photos get uploaded every day, we will need 0.5GB storage per day 2M * 284 bytes =~ 0.5GB
For 10 years we will need 1.88TB of storage

## Component Design
Uploading user can consume all the available connections, as uploading is a slow process.
If we assume that a web server can have a maximum 500 connections at any time, then it can't have more than 500 concurrent uploads or reads.
We can split reads and writes into separate services.

### Reliability and Redundancy

### Data Sharding
Let's assume we shard based on the UserID so that we can keep all photos of a user on the same shard.

How can we generate PhotoIDs? Each DB shard can have its own auto-increment sequence for PhotoIDs and since we will append ShardID with each PhotoID, it will make it unique throughout our system.



