import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pyaudio
import wave

def transforming_to_tones(area):

    # SIGNAL NORMALISATION
    # min and max area found empirically
    max_area=300000
    min_area=32000
    tone_range = max_area - min_area
    areatone = (area - min_area ) / tone_range

    if areatone > 0.2 and areatone < 0.4:
        areatone = 440
        note="A4"
    elif areatone >=0.4 and areatone < 0.6:
        areatone = 523
        note="C5"
    elif areatone >= 0.6 and areatone < 0.7:
        areatone = 587
        note="D5"
    elif areatone >= 0.7 and areatone < 0.8:
        areatone = 659
        note="C5"
    elif areatone >= 0.8 and areatone < 0.9:
        areatone = 698
        note="F5"
    elif areatone >= 0.9 and areatone < 1:
        areatone = 784
        note="G5"
    elif areatone >= 1:
        areatone = 880
        note="A5"
    else:
        note="Rest"
        areatone=0
    return note, areatone

def plotting_notes(notes):
    interval=[]
    for e in range(len(notes)):
        interval.append(e)
    plt.plot(interval, notes, "s")
    labels=set(notes)
    plt.ylabel('Notes')
    plt.xlabel('''Frame number \n
    You resemblance with the original song''')
    #ax.set_xlabel('time [s] \n This was a long experiment')
    plt.savefig('../output/music_report.pdf')  
    return plt.show()

def init_text():
    print('''
        This is a linux shell multiprocess combining a background music, a real-time image-capturing and a recording script. The second one is the father of another child subprocess which receives the area captured each frame and send a tone proportional to the area. \n
        The father captures an area in a frame and stop, the child process play a sound, the father captures another frame and the cycle starts again. \n 
        This is a python multiprocess under a parallel linux shell multiprocess.
        \n 
        MODES: \n
        - test [t] => git it a try \n
        - game [g] => play some funky tunes
        \n''')
   

