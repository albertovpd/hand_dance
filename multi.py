# https://docs.python.org/3.5/library/multiprocessing.html#module-multiprocessing

# https://stackify.com/when-to-use-asynchronous-programming/

 # https://github.com/timofurrer/awesome-asyncio#alternatives-to-asyncio

from multiprocessing import Process, Queue
import time
import sys

def reader_proc(queue):
    ## Read from the queue; this will be spawned as a separate Process
    while True:
        msg = queue.get()         # Read from the queue and do nothing
        if (msg == 'DONE'):
            break

def writer(count, queue):
    ## Write to the queue
    for ii in range(0, count):
        queue.put(ii)             # Write 'count' numbers into the queue
    queue.put('DONE')

if __name__=='__main__':
    pqueue = Queue() # writer() writes to pqueue from _this_ process
    for count in [10**4, 10**5, 10**6]:             
        ### reader_proc() reads from pqueue as a separate process
        reader_p = Process(target=reader_proc, args=((pqueue),))
        reader_p.daemon = True
        reader_p.start()        # Launch reader_proc() as a separate python process

        _start = time.time()
        writer(count, pqueue)    # Send a lot of stuff to reader()
        reader_p.join()         # Wait for the reader to finish
        print("Sending {0} numbers to Queue() took {1} seconds".format(count, 
            (time.time() - _start)))


# SHARE MEMORY
# from multiprocessing import Process, Value, Array

# def f(n, a):
#     n.value = 3.1415927
#     for i in range(len(a)):
#         a[i] = -a[i]

# if __name__ == '__main__':
#     num = Value('d', 0.0)
#     arr = Array('i', range(10))

#     p = Process(target=f, args=(num, arr))
#     p.start()
#     p.join()

#     print("esto es parent",num.value)
#     print("esto ",arr[:])

# POOL
# Create a pool of processes which will carry
# out tasks submitted to it with the Pool class.

# it supports asynchronous results with timeouts
# and calbacks and has a parallel map implementation
# (lo necesito para usar el wav mientras corre el programa)


#import os
#print("cpu avabiable", os.cpu_count())


# QUEUEEEEEEE
# E
#import multiprocessing

# result=[]

# # this is wroooooong, it does not queue a fuck
# def calc_square(numbers):
#     global result
#     for n in numbers:
#         result.append(n*n)
#     print("inside process"+str(result))

# if __name__=="__main__":
#     numbers=[1,2,3]
#     p=multiprocessing.Process(target=calc_square,args=(numbers,))
#     p.start()
#     p.join()
#     print("outside process "+str(result))

# this is chachi pistachi

# def calc_square(numbers,q): # child
#     for n in numbers:
#         q.put(n*5)  # esto es el append
    
# if __name__=="__main__": #parent
#     numbers=[2,3,5]
#     q=multiprocessing.Queue()
#     p=multiprocessing.Process(target=calc_square,args=(numbers,q))
    
#     p.start()
#     p.join()

#     while q.empty() is False:
#         print(q.get()) 

# esto coge los elementos de la lista uno por uno del comienzo de la lista y traerlos




# PROCESS
#  process, lock (queue and pool not in video ) 
#  https://www.youtube.com/watch?v=CRJOQtaRT_8


#class process => proc.start(), proc.join()

# from multiprocessing import Process

# case1
# def myfunc():
#     print("Hello World")

# if __name__=="__main__":
#     proc= Process(target=myfunc)
#     proc.start()
#     proc.join()

#case2
# from multiprocessing import Process

# def lang_func(lang):
#     print(lang)

# if __name__=="__main__":
#     langs=["C","Python","JAVA","PHP"]
#     processes=[]
#     for l in langs:
#         proc = Process(target=lang_func, args=(l,))
#         processes.append(proc)
#         proc.start()
#     for p in processes:
#         p.join()

## LOCK => no other process can execute similar code until
# the lock has been released (no me interesa)
#  acquire() // release()
# 