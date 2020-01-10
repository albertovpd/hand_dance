# Hand Dance. Final project at Ironhack Madrid.

This is a real-time video-capturing script that frames the area of your hand. That area is the input of another real-time script, this time for audio, and delivers a tone proportional to the area, each frame captured. This are 2 parallel processes, one being fed by the other, running with other parallel processes. 

Personally, I learnt a lot studying options of the multiprocess library (subprocess, pool...) and my real challenge was to share memory in real-time between processes that have not finished yet (something not so obvious in Python).


# Introduction:

This is an individual project to comprehend and research about:

    - OpenCV.
    - Multiprocesses and subprocesses.
    - Sharing memory between Python scripts
    - Argparse

I wanted to develop a script to play music with both hands, so I started looking for trained neural networks (there are some great ones to detect hands). Then reality struck me: The normal queue of work in Python is to perform a task, finish it, perform other task, repeat... What about performing several tasks at the same time?

The concept of "real-time", which is necessary in order to perform the idea, has been tricky until I found some ways of getting what I wanted:

1. Subprocesses:

    Defining several functions, when a function finishes, another start and so on. That implies if you are displaying a webcam video, the screen freezes every time another scripts works. So you have a frame, it freezes and emit a tone, and so on.

    This is an example of how subprocesses work (the father process is not shown, but it is there):
    
    ![alt](https://raw.githubusercontent.com/albertovpd/real-time_image-audio_multiprocess/master/output/worker.png "subpro")
    
    This was the workflow working with subprocesses:
    
    ![alt](https://raw.githubusercontent.com/albertovpd/real-time_image-audio_multiprocess/master/output/process.png "subpro")

2. Sharing memory:

    What if I start researching about the technical features of my PC and develop exquisite async functions with clockwork precision? One script writes, another read in miliseconds. Could be, but it could be faster: What if each frame I pickle the area of hand, overwrite it continuously and when the area is not being written, I read it? (You can not write and read the same file at exactly the sae time).
    That is what I did.

    Writing memory:

    ![alt](https://raw.githubusercontent.com/albertovpd/real-time_image-audio_multiprocess/master/output/writing_memory.png "writing")

    Reading memory:

    ![alt](https://raw.githubusercontent.com/albertovpd/real-time_image-audio_multiprocess/master/output/reading%20memory.png "Reading")
    

Finally, I used argparse and an init function to develop my main script as follows (I removed the config function, just to visualize other elements of the script):

![alt](https://github.com/albertovpd/real-time_image-audio_multiprocess/blob/master/output/parallel%20processes.png "parallel")

It is not the fanciest init function, it is just the init function I needed.

# Libraries:

        multiprocessing, subprocess, time, os, pickle, argparse, cv2, pyaudio, wave, numpy, matplotlib, synthesizer, simpleaudio.


# Description:

- Main.py starts the scripts in parallel process
- just_video.py open a frame where is shown is recording the webcam, draws a green square in your hand, also display the frequency associated and writes in memory the area captured each 2 frames.
- just_audio.py reads that piece of memory, use functions storaged in my_functions.py to emit sounds and plot a final graph with the notes played. 
- base_sound.py provides a background drums to make some funky tunes with motivation.
- recording_environment records everything from your microphone.

- Through terminal are also displayed the frequencies emitted. Sometimes appears "hand frame casualty", which mean that area of hand was read at the same time that was being written and is not usable. Thankfully there are a lot of frames per second, so it is not possible for humans to realize if there were some "hand frame casualty" or not.

### How it works:

In case you are using Python 3, from /src:

    python3 main.py -a "optional argument"

# Conclusion

### Accomplished goals:

- Share memory between not finished scripts.
- Share tasks between all cores available in my PC.
- Learn about OpenCV and all its possibilities.
- Work with video-audio in real-time.

### Future improvements:

- Optional parameters in init function to choose what scale do  you want to play.
- Change audio libraries to have better sounds.
- Find a way to minimize the "hand area casualties".
- Get a trained neural work that detects hands, to play both hands in function of the distance.

### References:

    - The real-time image capturing script is based on this project:
        - https://github.com/sashagaz/Hand_Detection (Alexander Gazman).
        - It was written in Python 2. I updated to Python 3.6 and used part of it to my purpose.

    - I used the recording_environment script just to check if I could use all cores of my PC in the parallel process. The owner is:
        - https://gist.github.com/mabdrabo/8678538 (Mahmoud Abdrabo)

        
