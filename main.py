from src.basesound_f import base

#from src.detection_f import hdetection
#from src.soundhand_f import soundhand

#process_list=[]
#hdetection()

def jobA(num, q):
    q.put(num * 2)

def jobB(num, q):
    base=base()

    q.put(base)

import multiprocessing as mp
q = mp.Queue()
jobs = (jobA, jobB)
args = ((10, q), (2, q))
for job, arg in zip(jobs, args):
    mp.Process(target=job, args=arg).start()

for i in range(len(jobs)):
    print('Result of job {} is: {}'.format(i, q.get()))
