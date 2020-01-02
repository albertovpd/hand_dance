import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pyaudio
import wave

def transforming_to_tones(area):

    # SIGNAL NORMALISATION. min and max area found
    max_area=300000
    min_area=32000
    tone_range = max_area - min_area
    areatone = (area - min_area ) / tone_range

    if areatone >= 0.1 and areatone < 0.25:
        areatone = 290 
        note="D4"
    elif areatone >=0.25 and areatone < 0.4:
        areatone = 329.63
        note="E4"
    elif areatone >= 0.4 and areatone < 0.55:
        areatone = 349.23
        note="F4"
    elif areatone >= 0.55 and areatone < 0.7:
        areatone = 392.00 
        note="G4"
    elif areatone >= 0.7 and areatone < 0.85:
        areatone = 440.00
        note="A4"  
    elif areatone >= 0.85 and areatone < 1:
        areatone = 493.88
        note="B4"
    elif areatone >= 1: #you can create an area greater than describing above
        areatone = 523.25
        note="C5"
    else:
        areatone=0
        note="Rest"
        
    return areatone,note

#mamahomething
    # if areatone > 0.2 and areatone < 0.32:
    #     areatone = 342
    #     note="F4"
    # elif areatone >=0.32 and areatone < 0.44:
    #     areatone = 380
    #     note="G4"
    # elif areatone >= 0.44 and areatone < 0.56:
    #     areatone = 412
    #     note="G#"
    # elif areatone >= 0.56 and areatone < 0.68:
    #     areatone = 500 
    #     note="B4"
    # elif areatone >= 0.68 and areatone < 0.80:
    #     areatone = 542 
    #     note="C#"  
    # elif areatone >= 0.8 and areatone < 1:
    #     areatone = 612
    #     note="D#"
    # elif areatone >= 1:
    #     areatone = 676
    #     note="E5"
    # else:
    #     note="Rest"
    #     areatone=0
    # return note, areatone


# notes_mama=[342,0,500,676,0,676,0,676,0,676,0,676,0,500, 0,542,0,612,0,672,0,542,0,500,0,0,
#         0,0,0,0,0,342,0,676,0,676,0,676,0,500, 0,542,0,500,0,412]

def accuracy_to_mama(notes):
    '''
    It comparises the notes you play with the original riff
    https://www.youtube.com/watch?v=CgHW02YF50s
    '''
    
    mama_isnt_home= ["F4","Rest","B4","E5","Rest","E5","Rest","E5","Rest","E5","Rest","E5","Rest","B4","Rest","C#","Rest","D#","Rest","E5","Rest","C#","Rest","B4","Rest","Rest",
        "Rest","Rest","Rest","Rest","Rest","F4","Rest","B4","E5","Rest","E5","Rest","E5","Rest","E5","Rest","E5","Rest","B4", "Rest","C#","Rest","B4","Rest","G#","Rest","G4","Rest","F4","Rest"]
    if len(mama_isnt_home) < len(notes):
                notes = notes[0:len(mama_isnt_home)]
    else:
        mama_isnt_home = mama_isnt_home[0:len(notes)]

    count=0
    for x,y in zip(mama_isnt_home,notes):
        if x==y:
            count+=1
    accuracy_song=round(count/len(mama_isnt_home),3)
    return accuracy_song, mama_isnt_home


def plotting_notes(notes):
    interval=[]
    for e in range(len(notes)):
        interval.append(e)

    # the function above is to get the accuracy and the list to the reference graph (mama song)
    accuracy_song, mama_isnt_home = accuracy_to_mama(notes)

    plt.plot(interval, notes, "s")
    plt.title("This is your art playing When Mama isnt at Home")
    labels=set(notes)
    plt.ylabel('Notes')
    plt.xlabel('Frames \n Your accuracy is more or less {}%. Keep working on it'.format(accuracy_song))
    plt.savefig("../output/music_report.pdf")
    return plt.show()

