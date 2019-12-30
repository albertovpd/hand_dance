import pickle
from synthesizer import Player, Synthesizer, Waveform
import multiprocessing
from my_functions import transforming_to_tones

tones=[]

while True:
    try:
        with open ('outfile', 'rb') as fp:
            area_out = pickle.load(fp)
        print(area_out)
    except:
        print(0)

    note,areatone = transforming_to_tones(area_out)

    print(areatone)

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