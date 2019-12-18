# from synthesizer import Player, Synthesizer, Waveform


# player = Player()
# player.open_stream()
# synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=0.7, use_osc2=False)        
# # Play A4
cantar2=[
    590,532,355,440,532,590,532,478,532,
    618,590,532,478,532,590,532,478,590,
    590,964,812,590,700,812,700,
    964,1074,964,912,
    590,964,812,700,590,532,590,532,478,590,
    590,964,812,590,700,812,700,
    964,1202,1074,964,912,
    590,619,964,
    619,700,964,
    700,812,776,
    590,700,812,
        590,700,964,812,
        812,964,812     
    ] 
cantar2=sorted(cantar2)
print(set(cantar2))
# {355,440,478,532,590,618,700,776,812, 912,964, 1074, 1202}

# for e in cantar:
#     player.play_wave(synthesizer.generate_constant_wave(e, 0.5))

# #  COMPARAR CON LA CANCIÓN DE CAMELA
# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np


# #labels = list(set(sonidos))
# men_means = [20, 34, 30, 35, 27]
# women_means = [25, 32, 34, 20, 25]

# x = np.arange(len(labels))  # the label locations
# width = 0.35  # the width of the bars

# fig, ax = plt.subplots()
# rects1 = ax.bar(x - width/2, men_means, width, label='Men')
# rects2 = ax.bar(x + width/2, women_means, width, label='Women')

# # Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('Scores')
# ax.set_title('Scores by group and gender')
# ax.set_xticks(x)
# ax.set_xticklabels(labels)
# ax.legend()


# def autolabel(rects):
#     """Attach a text label above each bar in *rects*, displaying its height."""
#     for rect in rects:
#         height = rect.get_height()
#         ax.annotate('{}'.format(height),
#                     xy=(rect.get_x() + rect.get_width() / 2, height),
#                     xytext=(0, 3),  # 3 points vertical offset
#                     textcoords="offset points",
#                     ha='center', va='bottom')


# autolabel(rects1)
# autolabel(rects2)

# fig.tight_layout()

# plt.show()
