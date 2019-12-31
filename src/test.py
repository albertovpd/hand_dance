import pickle
from synthesizer import Player, Synthesizer, Waveform
import multiprocessing
from my_functions import transforming_to_tones
import time

timeout = time.time() + 5 #seconds
print("Timer engaged")
while True:

    # timer to break the loop
    if time.time() > timeout:
        print("Timer finished")
        break

    try:
        with open ('outfile', 'rb') as fp:
            area_out = pickle.load(fp)

        #print(area_out, "patata")
        note, areatone = transforming_to_tones(area_out)
        print(areatone, note)
    except:
        print(0)





# import time
# timeout = time.time() + 60*5   # 5 minutes from now
# while True:
#     test = 0
#     if test == 5 or time.time() > timeout:
#         break