import subprocess
import sys
import argparse
#from my_functions import init_text


def program_config(): # currently unfinished
    parser = argparse.ArgumentParser(description='''This sript runs a 3 paralell processes:
    A background music, a real-time image-capturing and a recording script. The second one (real-time) contains a
     subprocess which receives the area captured each frame and send a tone proportional
    to the area. The father (main script) captures an area in a frame and stop, the child process (tone) play a sound, 
    the father captures another frame and the cycle starts again. This is a python multiprocess 
    under 3 parallel linux shell multiprocesses.''')
    parser.add_argument('-a',
                        help='Select: [t / g]  (t = test, give it a try; g = game, to play some funky tunes.)',
                        default="t"
                        )                        
    args = parser.parse_args()
    
    return args

def main():
    
    config=program_config()
    if config.a=='t':

        print("Starting test")
        subprocess.run("python3 video_audio.py & python3 base_sound.py", shell=True)

    elif config.a=="g":
         print("Starting game")
         subprocess.run("python3 video_audio.py & python3 base_sound.py & python3 recording_environment.py", shell=True)


if __name__=="__main__":
    main()