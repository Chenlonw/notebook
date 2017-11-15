import time
import threading
import Queue

class Consumer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        while True:
            content = self._queue.get()
            if isinstance(content, str) and content == 'quit':
                break
            # "Processes" (or in our case, prints) the queue item
            print "I'm a thread %s, and I received %s\n" %(self.getName(),
                                                           content)
        print 'Bye byes!\n'


def Producer():
    queue = Queue.Queue()
    worker_threads = build_worker_pool(queue, 4)
    start_time = time.time()

    words = ['this', 'is', 'a', 'hello', 'world', 'test', '!']
    for word in words:
        queue.put(word)

    for _ in worker_threads:
        queue.put('quit')
    for worker in worker_threads:
        worker.join()

    print 'Done! Time taken: {}'.format(time.time() - start_time)

def build_worker_pool(queue, size):
    workers = []
    for _ in range(size):
        worker = Consumer(queue)
        worker.start()
        workers.append(worker)
    return workers

if __name__ == '__main__':
    Producer()