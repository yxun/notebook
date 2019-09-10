#%% [markdown]
'''
shared memory model, each processor can access any location in memory.
distributed memory model, a processor must explicitly send a message to another processor to access its memory.

One of the key challenges of parallel programs is races, two concurrent instruction sequences access the same address in memory and at least one of them writes to that address.
Other challenges:
- starvation, a processor needs a resource but never gets it.
- deadlock, Thread A acquires Lock L1 and Thread B acquires Lock L2, following which A tries to acquire L2 and B tries to acquire L1
- livelock, a process keeps retrying an operation that always fails.
'''


#%%
'''
A semaphore maintains a set of permits. 
A thread calling acquire() on a semaphore waits, if necessary, until a permit is available, and then take it.
A thread calling release() on a semaphore adds a permit and notifies threads waiting on that semaphore, potentially releasing a blocking acquirer.
'''

import threading

class Semaphore():

    def __init__(self, max_available):
        self.cv = threading.Condition()
        self.MAX_AVAILABLE = max_available
        self.taken = 0

    def acquire(self):
        self.cv.acquire()
        while (self.taken == self.MAX_AVAILABLE):
            self.cv.wait()
        self.taken += 1
        self.cv.release()

    def release(self):
        self.cv.acquire()
        self.taken -= 1
        self.cv.notify()
        self.cv.release()


#%% [markdown]
'''
### Tips
- Try to work at a higher level of abstraction. Know the concurrency libraries, don't implement your own semaphores, thread pools, deferred execution, etc.
- Start with an algorithm that locks aggressively.
- When analyzing parallel code, assume a worst-case thread scheduler.
'''
