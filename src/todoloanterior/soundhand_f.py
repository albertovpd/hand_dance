from synthesizer import Player, Synthesizer, Waveform
from multiprocessing import Pool



# SOUND
def soundhand():
    #if areas[-1]>60000:
    player = Player()
    player.open_stream()
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=2.0, use_osc2=False)
    # Play A4
    #player.play_wave(synthesizer.generate_constant_wave(440.0, 0.2))

    # Play C major  
    chord = [261.626,  329.628, 391.996]
    player.play_wave(synthesizer.generate_chord(chord, 1))

soundhand()
# # write a wav

# # >>> from synthesizer import Writer
# # >>> writer = Writer()

# >>> chord = [261.626,  329.628, 391.996]
# >>> wave = synthesizer.generate_chord(chord, 3.0)
# >>> writer.write_wave("path/to/your.wav", wave)

