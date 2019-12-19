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
#{0,, , ,, , ,, }

    if areatone > 0.2 and areatone < 0.32:
        areatone = 342
        note="342"
    elif areatone >=0.32 and areatone < 0.44:
        areatone = 380
        note="C5380"
    elif areatone >= 0.44 and areatone < 0.56:
        areatone = 412
        note="D5412"
    elif areatone >= 0.56 and areatone < 0.68:
        areatone = 500 
        note="500"
    elif areatone >= 0.68 and areatone < 0.80:
        areatone = 542 
        note="542"
    elif areatone >= 0.8 and areatone < 0.9:
        areatone = 412
        note="412"    
    elif areatone >= 0.9 and areatone < 1:
        areatone = 612
        note="612"
    elif areatone >= 1:
        areatone = 676
        note="676"
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


def accuracy_to_mama(notes):
    '''
    This scrip tells you how good are you playing "when mama ist at home.
    https://www.youtube.com/watch?v=CgHW02YF50s
    '''
    mama_isnt_home= [342,0,500,676,0,676,0,676,0,676,0,676,0,500, 0,542,0,612,0,672,0,542,0,500,0,0,
        0,0,0,0,0,342,0,500,676,0,676,0,676,0,676,0,676,0,500, 0,542,0,500,0,412,0,380,0,342,0]
   

    print(len(mama_isnt_home))
    return
accuracy_to_mama(2)