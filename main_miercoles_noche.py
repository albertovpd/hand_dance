import subprocess
import sys
import argparse

from src.my_functions import init_text


def program_config(): # argparse currently unfinished
    parser = argparse.ArgumentParser(description='''This is a linux shell multiprocess combining a
    background music, a real-time image-capturing and a recording script. The second one is the father
    of another child subprocess which receives the area captured each frame and send a tone proportional
    to the area. The father captures an area in a frame and stop, the child process play a sound, 
    the father captures another frame and the cycle starts again. This is a python multiprocess 
    under a parallel linux shell multiprocess.''')
    

    parser.add_argument('-a',
                        help='Select: [t / g]  (t = test, give it a try; g = game, to play some funky tunes.)',
                        
                        )
                        
    args = parser.parse_args()
    print(args)
    return 

def main():
    config=program_config()
    init_text()
    a=input("Please, select mode [t/g]: ")
    if a=="t":
        subprocess.run("python3 ./src/video_audio.py & python3 ./src/base_sound.py", shell=True)    
    elif a=="g":
        subprocess.run("python3 ./src/video_audio.py & python3 ./src/base_sound.py & python3 ./src/recording_environment.py", shell=True)    

if __name__=="__main__":
    main()