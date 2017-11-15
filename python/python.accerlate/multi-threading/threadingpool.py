from multiprocessing.dummy import Pool as ThreadPool
import time

secds = [
    '1',
    '1',
    '1',
    '1',
    '1',
    '1',
    '1',
]

def sleep(url):
    time.sleep(int(url))

num = 2
# Make the Pool of workers
pool = ThreadPool(num)
# Open the urls in their own threads
# and return the results
start_time = time.time()
results = pool.map(sleep, secds)
print 'Done! Time taken with {} thread: {}'.format(num, time.time() -
                                                   start_time)

#close the pool and wait for the work to finish
pool.close()
pool.join()