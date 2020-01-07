import pickle
from synthesizer import Player, Synthesizer, Waveform
import multiprocessing
from my_functions import mama_isnt_home, bluesly, chromatic, theremin, deep_purple, plotting_notes
import time

player = Player()
player.open_stream()
synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=0.7, use_osc2=False)
notes=[]


timeout = time.time() + 5 #seconds 32-35 is ok
print("Timer engaged")
while True:
    # timer to break the loop
    if time.time() > timeout:
        print("Timer finished")
        break

    # try/except to avoid errors while writing and reading at the same time
    try:
        with open("../input/outfile_area","rb") as fa:
            area_out=pickle.load(fa)
            areatone, note = deep_purple(area_out)
            print(areatone, " Hz")
            notes.append(note)
            player.play_wave(synthesizer.generate_constant_wave(areatone, 0.05))
            #areatone,note = transforming_to_tones(area_out)
            #areatone = theremin(area_out)  
            #areatone, note = mama_isnt_home(area_out)
            #areatone, note=chosen_scale
    except:
        print("Hand frame casualty")


print("-----42-----")
print("Plotting notes:")

# Plotting notes.
plotting_notes(notes)
print("Plots saved with .PDF format in input folder")


        # take a glance to what's written in just_video.py

        #with open ("../input/outfile_w", "rb") as fw:
        #    w=pickle.load(fw)
            #print("width ", w)
        #with open ("../input/outfile_h", "rb") as fh:
        #    h=pickle.load(fh)
            #print("height " ,h)
        #     #area_out= w*h
        # if w <= h: 
        #     #areatone,note = transforming_to_tones(area_out)
        #     #areatone = theremin(area_out)  
        #     #areatone, note = mama_isnt_home(area_out)
        #     areatone, note=deep_purple(area_out)
        #     print(areatone)
        #     player.play_wave(synthesizer.generate_constant_wave(areatone, 0.05))