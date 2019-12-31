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
        print(note, areatone, "patata")
        if time.time() > timeout:
            break
    # except:
    #     print(0)
    
    
    

#     import time
# timeout = time.time() + 60*5   # 5 minutes from now
# while True:
#     test = 0
#     if test == 5 or time.time() > timeout:
#         break
#     test = test - 1

    # ver si lagea ahora o qué
    # tones.append(areatone)

    # player = Player()
    # player.open_stream()
    # synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=0.7, use_osc2=False)

    # #if tones[-1]==tones[-2]:
        
    #     player.play_wave(synthesizer.generate_constant_wave(tone[-1], 0.14))    
        

    #     process = multiprocessing.Process(target=worker)
    #     process.start()
    #     process.join()