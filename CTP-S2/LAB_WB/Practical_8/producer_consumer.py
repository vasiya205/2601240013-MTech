import threading
import queue
import time
import random

buffer = queue.Queue(maxsize=5)

def producer(prod_id: int):
    for i in range(3):
        item = f"Item-{prod_id}-{i}"
        buffer.put(item)
        print(f"Producer {prod_id} produced: {item}")
        time.sleep(random.uniform(0.1, 0.2))

def consumer(cons_id: int):
    for _ in range(3):
        item = buffer.get()
        print(f"Consumer {cons_id} consumed: {item}")
        buffer.task_done()
        time.sleep(random.uniform(0.2, 0.3))

if __name__ == "__main__":
    t1 = threading.Thread(target=producer, args=(1,))
    t2 = threading.Thread(target=consumer, args=(1,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    print("Producer-Consumer execution completed successfully.")
