import threading

def worker():
    print("Hello from worker thread")

t = threading.Thread(target=worker)

t.start()

print("Hello from main thread")

t.join()

print("Program Finished")


import threading

def numbers():
    for i in range(1, 6):
        print(threading.current_thread().name, ":", i)

t1 = threading.Thread(target=numbers, name="Thread-1")
t2 = threading.Thread(target=numbers, name="Thread-2")
t3 = threading.Thread(target=numbers, name="Thread-3")

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()


import threading

def add(a, b):
    print("Sum =", a + b)

t = threading.Thread(target=add, args=(10, 20))

t.start()

t.join()

print("Main Thread Finished")


import threading

counter = 0

def increment():
    global counter
    for i in range(100000):
        counter += 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print("Counter =", counter)



import threading

counter = 0

def increment():
    global counter
    for i in range(100000):
        counter += 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print("Counter =", counter)



import threading

counter = 0

lock = threading.Lock()

def increment():
    global counter

    for i in range(100000):
        lock.acquire()
        counter += 1
        lock.release()

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print("Counter =", counter)




import threading
import time

def A():
    print("A started")
    time.sleep(2)

def B():
    print("B started")

t1 = threading.Thread(target=A)
t2 = threading.Thread(target=B)

t1.start()

t1.join()

t2.start()

t2.join()





import threading
import time

event = threading.Event()

def worker():
    print(threading.current_thread().name, "waiting")
    event.wait()
    print(threading.current_thread().name, "started")

t1 = threading.Thread(target=worker, name="Thread-1")
t2 = threading.Thread(target=worker, name="Thread-2")
t3 = threading.Thread(target=worker, name="Thread-3")

t1.start()
t2.start()
t3.start()

time.sleep(2)

print("Main thread gives signal")

event.set()

t1.join()
t2.join()
t3.join()




import threading
import time

sem = threading.Semaphore(2)

def worker():
    sem.acquire()

    print(threading.current_thread().name, "Entered")

    time.sleep(2)

    print(threading.current_thread().name, "Exited")

    sem.release()

threads = []

for i in range(5):
    t = threading.Thread(target=worker, name="Thread-"+str(i+1))
    threads.append(t)
    t.start()

for t in threads:
    t.join()





import threading
import time

def background():
    while True:
        print("Running in background")
        time.sleep(1)

t = threading.Thread(target=background)

t.daemon = True

t.start()

time.sleep(2)

print("Main Thread Exits")




from concurrent.futures import ThreadPoolExecutor, as_completed

def square(n):
    return n * n

with ThreadPoolExecutor(max_workers=3) as executor:

    futures = []

    for i in range(1, 6):
        futures.append(executor.submit(square, i))

    for future in as_completed(futures):
        print(future.result())

