import pickle
from synthesizer import Player, Synthesizer, Waveform
import multiprocessing
from my_functions import transforming_to_tones, theremin, mama_isnt_home,deep_purple
import time

player = Player()
player.open_stream()
synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=0.7, use_osc2=False)

timeout = time.time() + 10 #seconds
print("Timer engaged")
while True:
    # timer to break the loop
    if time.time() > timeout:
        print("Timer finished")
        break
    # try/except to avoid errors while writing and reading at the same time
    try:
        with open ("../input/outfile_w", "rb") as fw:
            w=pickle.load(fw)
            #print("width ", w)
        with open ("../input/outfile_h", "rb") as fh:
            h=pickle.load(fh)
            #print("height " ,h)
            area_out= w*h
        if w <= h: 
            #areatone,note = transforming_to_tones(area_out)
            #areatone = theremin(area_out)  
            #areatone, note = mama_isnt_home(area_out)
            areatone, note=deep_purple(area_out)
            print(areatone)
            player.play_wave(synthesizer.generate_constant_wave(areatone, 0.05))
    except:
        print("Hand frame casualty")

        