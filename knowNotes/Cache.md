# Cache

When we talk about Cache, we need to consider the following:
- Read/write speed.
- Memory usage.
- Disk I/O dumping.
- Scaling.

## General
Cache，缓存，常见于系统设计中为了提高数据读取的性能而添加的一种存储方式。
缓存的工作原理简单来讲是将花费时间较长的读取数据请求结果，存放至内存中，使数据库不必处理第一次之后的相同请求，而使直接读取结果。
对于数据的读取有着显著的提高。
相同的方式也可以应用于写入。在对同一份数据的多次写入情景下，加入缓存，可以分批量处理对同一个数据点的多次写入。将多次写入的最终结果已一次写入记录到数据库中，
以减少对数据库的请求次数，提高数据库的可用性。

### Distributed cache - 分布式缓存
在需要缓存的数据量特别大的时候，将数据按照一定的规律分类，将其缓存到不同的机器/实例中，通过算法来吧对数据的请求导流到相对应的缓存实例当中。
例如将3TB的缓存分为3个1TB，每个缓存单位都可以处理100000次/s的请求，处理能力增加。
通过分类和导流，缓存可以存储更多的数据，并且可以处理更多的请求。

### Global Cache - 全局缓存
全局缓存更像是数据库和后端之间的一整个中间层。全局缓存一般只有一个实例，处理所有来自服务器的请求。同时也处理缓存数据与数据库数据的同步。因为是所有数据请求的枢纽，一般会在系统设计当中成为一个潜在的瓶颈。

### CDN - Content Distributed Network - 内容分发网络
用于缓存网页服务当中的CSS，html和js文件，很多情况下，这些文件都不会经常更改。所以对于经常访问的那些链接以及资源，将其缓存至内存当中，提高其读取的速度，已方便更好的服务于网络用户。节省了从磁盘读取文件的时间。

## Cache design patterns
[Amazon Caching best practices](https://aws.amazon.com/caching/best-practices/)

## Cache Invalidation
Invalidation refers to the process to make the cache block replaced or removed. Since all the data in cahche is a duplication of the data in the database, the invalidation is the main way to keep the two data in-sync to avoid data mismatch.

### Write through
Write data to cache and database at the same time. This is the simpliest way to keep the data sync but it's slow compare to others since it needs to write to 2 places in one request. Also, the possibility of error is higher. It requires more  steps to recover&roll back in case of an error.

### Write around
Write the data to database first, and update the cache later. This will make the database as the source of truth. While extra read need to be made to the cache layer in order to sync the data, some user may experience the outdated data because there is a measured gap between the data write to the database and data is read to the cache. If we want to deliver the most recent and updated data all the time like flight ticket, we don't want this kind of design. But if this is some statistical data, then this little delay is acceptable. Also, if the system is heave write one, this design is not going to be efficient. High volum of write data will take down the database and cause some trouble.

### Write back
Write the data to the cache layer first and write it back to the database later. This is especially useful in the IOT system, where the write traffic is super heavy and the data amount is high as well. This kind of design will build a buffer layer between server and database to collect data in cache and aggragate them. Thus pieces of data in one collection can be written in one big bulk request. This improves the performance of the datalayer.
However, since the cache now is the sourth of truth, in case of the error or accident, the data in cache layer will be lost without saving into the database. In some case, the data loss will happen and will not be recovered. If we are saving the sensitive data, we don't want to use this design.

## Cache Eviction
Cache eviction is a policy to manage the cache mamery to keep the cache within a limited budget. Whenever the data comes into cache and reaches the memory limit, the eviction is executed to flush some old/less used data out of cache.

### First In First Out
The oldest data which is inserted into the cache at first place is evicted first.

### Last In First Out
The newest data is evicted first. This often used when the data in the cache already is more likely to be accessed than the new cached data. The good example would be the best coffee bean growing land. There are always a few of top coffee producer in the would and people always like them for the long time. Even if the new comers could shake the market for a bit but the old and famous one would never be fadded.

### Least recently used
Keep a stamp of the last used date, evict the oldest used data out. This helps the cache to maintain the freshest data in the set.

### Most recently used
Opposite to the least recently used, the most recently used policy is mostly used in some cases that having "just seen something" is a good indicator that you're unlikely to see the same thing again soon.

### Least frequently used
The less used on is evicted to keep the data hot.

### Random
Treat the data all the same and replace them randomly.

## Memcached & Redis
Both are
- Key-value data store
- in-memory RAM
- NoSQL data management solutions


## Memcached
[official defination](https://memcached.org/about)

It abstracts the memory of the computer and make that part of memory public to the applications. The shared memory is more like a shared fast database which can tempararily store the data.
Without memcached, the memory for each application is seperated and memcache can never share between the nodes/replicas. But with this, memcached published a chunck of memory so all the nodes can access the same memory for data.

### When to use Memcached and why
1. Relatively small and static data, such as HTML code framgments
    - the internal memory management consumes comparativly less memory resources for metadata, so it's efficient in the simplest use case.

1. Scale to more space but don't want to handle clusters
    - Multithreaded so by giving it more resources (RAM & CPU) the performance can be better

1. High traffic websites
    - High read speed can give out a good response time.

### Downside
- Bad at handles dynamic data. The memory becomes fragmented after handling the dynamic data for a while.
- Costly to rebuild after a restart.
- Only suppoprts Least Recently Used eviciton policy.



## Redis
- Data structure store
- Five data structures: string, hashes(maps), lists, sets, sorted sets
- Full control over the eviction policy, 6 different kinds
- Persistence to disk, by default.
- Transactions with optimistic locking ([WATCH/MULTI/EXEC](https://redis.io/topics/transactions))
    - The lock in the redis will make sure only one operation is executed at the same time even multiple clients are running
    - It's a all or nothing protocal which guarantees that the redis transaction is atomic
    - The [optimistic locking](https://redis.io/topics/transactions#cas) using watching to abort the transaction to avoid the race condition when 2 or more clients try to modify the same field at the same time.
- [Pub/sub](https://redis.io/topics/pubsub). Extremely fast.
    - Uses the observable pattern to build a publisher and subscriber structure to decouple the server and client. This kind of decoupling is enabling the flxibility of the client to listen and subscribe to many publishers at once where the publishers are hosting in different caching servers.
- Values up to 512MB in size (memcached limited to 1MB per key)
- Lua scripting (as of 2.6)
- [Built in clustering](https://redis.io/topics/cluster-tutorial) (as of 3.0)
    - Redis Cluster provides a way to run a Redis installation where data is automatically sharded across multiple Redis nodes.
    - The ability to automatically split your dataset among multiple nodes.
    - The ability to continue operations when a subset of the nodes are experiencing failures or are unable to communicate with the rest of the cluster.


## The use cases for Redis as Caching
### E-Commerce Applications
Usually this is a read heavy application. By caching the pages, configurations, and sessions, performance and be improved a lot.

### IOT Application
Since the devices and node in the IOT system sents a vast number of data to the system, it is a super heavy write application. The caching layer provide a buffer to flush a high volume of data before storing it to persistent storage - Database or hard drive file.

### Real Time Analytics
The Sorted set is a super matched featrue for hanlding the counting and summary statistics. Get the top few items in the sorted set can be achieved farly quick in Redis which boost the real-time analytics a lot.
