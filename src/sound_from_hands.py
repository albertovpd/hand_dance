import cv2
import numpy as np
import multiprocessing
import time
import multiprocessing
manager = multiprocessing.Manager()
shared_list_area = manager.list()

from synthesizer import Player, Synthesizer, Waveform #from src.music_from_hands import my_sound

def handysound():

    def worker2(areatone):
        #print("multiprocess of hand area from worker1 to worker2,MADAFAKA, which is ", area)
        print("the tone of the area is" , areatone, "Hz")
        player = Player()
        player.open_stream()
        synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=0.7, use_osc2=False)
        
        # Play A4
        return player.play_wave(synthesizer.generate_constant_wave(areatone, 0.15))
    return worker2
           

    #------------------------------------------------
