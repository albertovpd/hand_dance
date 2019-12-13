
# QUEUEEEEEEEE

import multiprocessing

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

def calc_square(numbers,q): # child
    for n in numbers:
        q.put(n*5)  # esto es el append
    
if __name__=="__main__": #parent
    numbers=[2,3,5]
    q=multiprocessing.Queue()
    p=multiprocessing.Process(target=calc_square,args=(numbers,q))
    
    p.start()
    p.join()

    while q.empty() is False:
        print(q.get()) 

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