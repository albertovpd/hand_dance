import subprocess
import sys
import argparse
import os                                                                       
from multiprocessing import Pool                                                
                                                                                
                                                                                
processes = ('just_video.py', 'just_audio.py', "base_sound.py","recording_environment.py","video_audio.py")   

def run_process(process):  
    os.system('python3 {}'.format(process))                                       


def program_config(): 
    parser = argparse.ArgumentParser(description='''TO RUN: if using python3, from src: python3 main.py -a "whatever argument"
    --------------------------------
    This script runs several parallel processes at the same time and
    shares memory between 2 of them. The real-time image-capturing script captures the area of hand each frame,
     storages it in memory and overwrites it continuously. The audio script reads that memory (when is not being written) and translates
    it into music. The other parallel scripts deliver other tasks (background music, recording the environment, etc)
    <=======> There is a multiprocess option between 2 scripts: The father process captures an area in a 
    frame and stop, the child process (tone) play a sound, the father captures another frame and the cycle 
    starts again. This is a python multiprocess under 3 parallel linux shell multiprocesses.''')

    parser.add_argument('-a',
                        help='''
                        Select: [ t / b / r / m].   
                        t = Test, give it a try. 
                        b = with Background drumset.
                        r = Recording from microphone your music and environment
                        m = using Multiprocess architecture, enjoy it.  
                        u = Upgrading stuff (for developers).
                        ''',
                        default="t"
                        )    
                    
    args = parser.parse_args()
    return args

def main():    
    config=program_config()
    print("Selected: ", config.a)

    if config.a=='t':

        print('''Starting Test. 
        \n Sharing memory between video and audio script while parallel running. 2 scripts''')
        #subprocess.run("python3 just_video.py & python3 just_audio.py", shell=True) #this is how it worked before
        pool = Pool(processes=3)                                                        
        pool.map(run_process, processes[0:2]) 
    
    elif config.a=="b":        
        print('''Starting with Background drums. 
        \n Sharing memory between video and audio script while parallel running. 3 scripts''')
        pool = Pool(processes=3)                                                        
        pool.map(run_process, processes[0:3])

    elif config.a=="r":
        print('''Do it awesome you funky beast. From now I am recording. 
        \n Sharing memory between video and audio script while parallel running. 4 scripts''')
        pool = Pool(processes=4)
        pool.map(run_process, processes[0:4])
    elif config.a=="m":
        print("Now using subprocesses from the multiprocess library")
        pool= Pool(processes=2)
        pool.map(run_process,[processes[2], processes[4]])

if __name__=="__main__":
    main()
