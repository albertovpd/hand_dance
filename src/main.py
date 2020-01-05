import subprocess
import sys
import argparse

# If you have python3, to run it, from src: python3 main.py -a "whatever argument"

def program_config(): 
    parser = argparse.ArgumentParser(description='''This script runs several parallel processes at the same time and
    shares memory between 2 of them. The real-time image-capturing script captures the area of hand each frame,
     storages it in memory and overwrites it continuously. The audio script reads that memory (when is not being written) and translates
    it into music. The other parallel scripts deliver other tasks (background music, recording the environment, etc)
    <=======> There is a multiprocess option between 2 scripts: The father process captures an area in a 
    frame and stop, the child process (tone) play a sound, the father captures another frame and the cycle 
    starts again. This is a python multiprocess under 3 parallel linux shell multiprocesses.''')

    parser.add_argument('-a',
                        help='''
                        Select: [ t / b / u / m]  
                        t = Test, give it a try. 
                        b = with Background drumset.
                        u = testing to Upgrade.
                        m = using Multiprocess architecture, enjoy it.  
                        ''',
                        default="t"
                        )                        
    args = parser.parse_args()
    
    return args

def main():
    
    config=program_config()
    if config.a=='t':

        print("Starting Test")
        subprocess.run("python3 just_video.py & python3 just_audio.py", shell=True)

    elif config.a=="b":        
        print("Starting Background drums")
        subprocess.run("python3 just_video.py & python3 just_audio.py & python3 base_sound.py", shell=True)

    elif config.a=="u":
        print("Upgrading script")
        subprocess.run("python3 video_audio.py & python3 test.py", shell=True)
    
    elif config.a=="m":
        print("Multiprocess workflow \n Enjoy it")
        subprocess.run("python3 video_audio.py & python3 base_sound.py", shell=True)

if __name__=="__main__":
    main()
