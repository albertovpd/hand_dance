# Final project at Ironhack Madrid: 

Play music with your hand in front of your webcam, thanks to sharing memory between processes and multiprocess library

# Hand-dance. Final project at Ironhack Madrid.

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

    This is an example of how subprocesses work:
    ![alt]("subpro")

2. Sharing memory:

    What if I start researching about the technical features of my PC and develop exquisite async functions with clockwork precision? One script writes, another read in miliseconds. Could be, but it could be faster: What if each frame I pickle the area of hand, overwrite it continuously and when the area is not being written, I read it? (You can not write and read the same file at exactly the sae time).
    That is what I did.

    Writing memory:

    ![alt]("writing")

    Reading memory:

    ![alt]("Reading")

Finally, I used argparse and an init function to develop my main script as follows (I removed the config function, just to visualize other elements of the script):
![alt]("parallel")


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

























-------------------------------------------------

### An introduction to multiprocess libraries and tools in Pyhon and Linux Shell to perform real-time image-capturing with audio outputs in function of the captured image.

![alt](https://raw.githubusercontent.com/albertovpd/real-time_image-adudio_multiprocess/master/output/process.png "process")

My name is Alberto, I am Physicist and from my point of view, as well as the known work with data, a Data Scientist must know how to take the best of its software and hardware, minimizing deadtime between processes and the queue of processes in scripts.

For this reason, I invested the week we had for deliver our final project in learning how to run parallel scripts, how to write synchronized and asynchronized scripts and how to feed a process with the output of other that is not "completely finished" yet, in a programming language, Python, which works performing just one single task at time.

From all I learn about Multiprocessing, Async IO and integrated Python tools, my resulting scripts are the simplest I could find for the task I needed to solve.

-------------------------------

# The project:

As shown in the first picture, main.py initializes 3 parallel running scripts. Maybe this commit can shed some light:

![alt](https://raw.githubusercontent.com/albertovpd/real-time_image-audio_multiprocess/master/output/Screenshot%20from%202019-12-23%2018-51-53.png "commit")

As sketched in the beginning:

- Process 1 locates where is the hand in each frame and draw a green square on it.

- Subprocess receives the area of this square and emits a tone proportional to the area (the greater area the higher pitch). When the sound is finished (0.14 msecs), Process 1 starts again capturing another frame, and so on.

- Process 2 plays a background music, to try to follow it with your hand.

- Process 3 records all sounds from the microphone as long as the scripts are active.

- When the script is finished, the output are the following:
    - The recording in .wav.
    - A pdf where all notes played are registered .
    - Your score trying to reproduce with your hand the song "When Mama isn't Home" (https://www.youtube.com/watch?v=CgHW02YF50s)
    - An email with your pdf and score.

# Used libraries:

- Real-time image-capturing:
    - cv2 (openCV), numpy, time
    
- Sound feedback:
    - multiprocessing, time, synthesizer, wave
    
- Background music:
    - pyaudio, simpleaudio
    
- Email and graphs:
    - matplotlib, dotenv,email, smtplib

- Main.py
    - subprocess, sys, arparse, os
    
# Further improvements:

- Keep learning about multiprocess and async libraries. It should be compulsary when you are working with heavy datasets.

- Keep learningh how to share memory from 2 scripts at the same time (there is a wonderful option available for python 3.8.rc1 with Multiprocess library, but I do want to check it out in Python 3.6 with the tools I have).

- Improve the subprocess to avoid the lag in camera each time the tone is played.

- Use a trained neural network like https://github.com/CMU-Perceptual-Computing-Lab/openpose or https://github.com/victordibia/handtracking to play with both hands in real-time, instead of just one.

- One of the outputs of PROCESS 1 is the hand area detected on each frame. I am obsessed with the following idea:

    -A: In a loop, use pickle library to constantly save in memory that area and overwrite it with the next frame.
    
    -B: In another script (lets say SCRIPT 2), inside a While True, unpick the pickle continously, so I will have the area each frame in other script.
    - Problems: The process of write in memory, overwrite and read it can not be done at the same time, you get errors.
    
    - Cheapest solution: Build SCRIPT 2 inside a Try-Except, which is not desirable, but useful (You have a lot of frames per second, so it is not important to miss some of them in the way).
    
    - Great solution: Program the scripts with Async IO, or use a timer so every milisecond is running one of the scripts without interfering with the others when reading/writing in memory.


    
        
