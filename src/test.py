import pickle
from synthesizer import Player, Synthesizer, Waveform
import multiprocessing
from my_functions import transforming_to_tones, theremin, mama_isnt_home,deep_purple
import time

# script to try new stuff

timeout = time.time() + 10 #seconds
print("Timer engaged")

player = Player()
player.open_stream()
synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=0.7, use_osc2=False)

# sharing_memory_elements={"outfile_a":area_out,"outfile_w":w,"outfile_h":h}

while True:

    # timer to break the loop
    if time.time() > timeout:
        print("Timer finished")
        break

    # try/except to avoid errors while writing and reading at the same time
    try:
        with open ("outfile_w", "rb") as fw:
            w=pickle.load(fw)
            print(w)
        with open ("outfile_h", "rb") as fh:
            h=pickle.load(fh)
            print(h)
        with open ('outfile_a', 'rb') as fp:
            area_out = pickle.load(fp)
            #areatone,note = transforming_to_tones(area_out)
            #areatone = theremin(area_out)
            #areatone, note = mama_isnt_home(area_out)
            areatone, note=deep_purple(area_out)
            player.play_wave(synthesizer.generate_constant_wave(areatone, 0.05))
            #print(areatone)
    except:
        print("Hand frame casualty")

   
    # import time
# timeout = time.time() + 60*5   # 5 minutes from now
# while True:
#     test = 0
#     if test == 5 or time.time() > timeout:
#         break