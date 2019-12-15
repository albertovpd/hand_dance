from synthesizer import Player, Synthesizer, Waveform


# # SOUND
def soundhand():
    #if areas[-1]>60000:
    for e in list(range(50)):
        player = Player()
        player.open_stream()
        synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
        # Play A4
        #player.play_wave(synthesizer.generate_constant_wave(440.0, 0.15))

    # Play C major  
        chord = [261.626,  329.628, 391.996]
        player.play_wave(synthesizer.generate_chord(chord, 0.15))

soundhand()

# player = Player()
# player.open_stream()
# synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
# for e in list(range(80,1200,50)):
#     player.play_wave(synthesizer.generate_constant_wave(e, 0.15))


#  def renormalize(area):
#         range1=[300000,32000]
#         range2=[1200,80]
#         delta1 = range1[1] - range1[0]
#         delta2 = range2[1] - range2[0]
#         area = (delta2 * (area - range1[0]) / delta1) + range2[0]
#         return int(area)
#     areatone=renormalize(area

# If you want to normalize to [x, y], first normalize to [0, 1] via:

# a=input("area")
# a=int(a)
# max_area=300000
# min_area=32000
# tone_range = max_area - min_area
# a = (a - min_area ) / tone_range


#  # Then scale to [x,y] via:
# max_freq=1200
# min_freq=80
# range2 = max_freq - min_freq
# a = int((a * range2) + min_freq)

# print(a)