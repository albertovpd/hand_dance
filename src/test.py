import pickle
from synthesizer import Player, Synthesizer, Waveform
import multiprocessing

while True:
    try:
        with open ('outfile', 'rb') as fp:
            area_out = pickle.load(fp)
        print(area_out)
    except:
        print(0)

        
# count=0
# while True:
#     count=0

#     if count>=5: #to catch 1 of 5 frames 
        
#         def worker1(): 
            
#             area = pickle.load( open( "save.p", "rb" ) )
            
#             return area 
#     count=0

#     process = multiprocessing.Process(target=worker1)
#     process.start()
#     process.join()