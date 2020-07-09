# Java Garbage Collect
[Reference](https://mp.weixin.qq.com/s/UwrSOx4enEX9iNmD4q_dXg)

## The basic approach of multi-threading in JVM

Each CPU core schedule to run one thread at a time for JVM so JVM looks like multi-threading.
Once the CPU time allocated to a thread is reached, the thread is pushed to stack and the core is switched to serve another thread. Then the next time the core is ready to serve this thread again, the CUP will read the stack to determine where to start for this thread, then continue.

## How to detect the garbage
There are 2 main approaches to detect the garbage.
- Reference count
    - For the object oriented language, every object has a reference count in the system. When the count decremented to zero, the garbage collector will recycle the object and free the memory.
    - The down side of this algorithm is that, it is hard to detect the reference circle. For instance, a group of object is referencing each other but is not reachable from the main method, then this group of object should be recycled but the reference count for every of them is not 0.

- Reachable algorithm
    - From the root of the program, find all the object that can be reachable. For those that is not reachable, mark them as garbage and recycle them. This algorithm can detect all the garbage at once and clean up the system all together. But it is super costly and need to shut down the system to finish up this recycle.


## How to clean up the garbage *4

- 标记法
    - 标记后直接释放内存，容易产生内存碎片和不连续的内从空间，导致之后的内存使用效率低下。
- 标记后复制
    - 标记并清楚内存区间A的垃圾。将非垃圾的数据连续地复制到内存区间B中，之后完全释放内存区间A的所有数据。这样B中就有连续的数据块，而A中的空间被完全释放。
- 标记并整理当前模块中的内存。
    - 在当前区域中边清除回收边整理内存碎片。
- 世代标记法
    - 将没有被GC清除的内存数据标记并保存至额外区间。当数据经历过的GC次数达到已经数量，则将数据移动至特殊内存区间，在GC时不去扫描。
    - 在特殊内存区间被填满后，对整个系统进行GC，reachable algorithm, 来一次清除所有垃圾。


## What happen when garbage is full
Run "STOP THE WORLD" algorithm to recycle all the garbage in the RAM. This algorithm will stop the system and have the computer focus on the GC to finish it up quicker. After this execution, the garbage will be removed completely and the memory will be freed.
Because when the program is running it naturally will use the memory to store new data. And the reachable algorithms is way to scan the memory. When the reachable algorithm is running while the program is executing, the race condition will happen and will accidentally recycle the new data in the memory that is not reachable before but now. So we need to stop the world to avoid the race condition.
