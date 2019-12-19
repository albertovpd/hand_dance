
from synthesizer import Player, Synthesizer, Waveform

cantar2= [
    342,0,
    500,    
    676,0,676,0,676,0,676,0,676,0,
    500, 0,
    542,0, 
    612,0,
    672,0,
    542,0,
    500,0,0,0,0,0,0,0,
    342,0,
    500,    
    676,0,676,0,676,0,676,0,676,0,
    500, 0,
    542,0, 
    500,0,
    412,0,
    380,0,
    342,0
]
    # from synthesizer import Player, Synthesizer, Waveform


player = Player()
player.open_stream()
synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=0.7, use_osc2=False)        
# # Play A4

#cantar2=sorted(cantar2)
print(set(cantar2))
# {355,440,478,532,590,618,700,776,812, 912,964, 1074, 1202}

for e in cantar2:
    player.play_wave(synthesizer.generate_constant_wave(e, 0.14))
