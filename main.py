import subprocess
import sys
import argparse


#subprocess.run("python3 ./src/video_audio.py & python3 ./src/base_sound.py & python3 ./src/recording_environment.py", shell=True)    

# subprocess.run("python3 ./src/recording_environment.py", shell=True)    

# # --- my funcions ---

#from processing_functions import working, enriching, decimals, results
#from web_enriching import web_scraping
# -------------------


# def program_config():
#     parser = argparse.ArgumentParser(description='''This is a linux shell multiprocess combining a
#     background music, a real-time image-capturing and a recording script. The second one is the father
#     of another child subprocess which receives the area captured each frame and send a tone proportional
#     to the area. The father captures an area in a frame and stop, the child process play a sound, 
#     the father captures another frame and the cycle starts again. This is a python multiprocess 
#     under a parallel linux shell multiprocess.''')
    

#     parser.add_argument('-t',
#                         help='Select: Test (to get used to the game) or Song (to play some funky tunes)',
#                         default=None
#                         )
#     parser.add_argument('-g',
#                         help='Play the game. Try to neal "When mama isnt at home song',
#                         default=None
#                         )
                        
#     args = parser.parse_args()
#     # print(args)
#     return 

a=input("Select the mode, test or game [t/g]: ")
if a=="g":
    subprocess.run("python3 ./src/video_audio.py & python3 ./src/base_sound.py & python3 ./src/recording_environment.py", shell=True)    
elif a=="t":
    subprocess.run("python3 ./src/video_audio.py")
else:
    print("Non valid argument.")

    # working(data)
    # dataset=enriching(data)
    # finaldataset=decimals(dataset)


    #print(finaldataset)

    #results(finaldataset, config.a, config.b)

# if __name__=="__main__":
#     main()