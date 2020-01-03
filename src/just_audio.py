import pickle
from synthesizer import Player, Synthesizer, Waveform
import multiprocessing
from my_functions import transforming_to_tones
import time



timeout = 50   # [seconds]
timeout_start = time.time()

while time.time() < timeout_start + timeout:
    test=0
    try:
        with open ('outfile', 'rb') as fp:
            area_out = pickle.load(fp)
            note, areatone = transforming_to_tones(area_out)
            print(note, areatone)
        if time.time() > timeout:
            break
    
    except:
        print("This frame was not read")
            

