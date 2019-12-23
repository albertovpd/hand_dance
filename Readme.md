# Final project at Ironhack Madrid: 

## An introduction to multiprocess libraries and tools in Pyhon and Linux Shell.

![alt](https://raw.githubusercontent.com/albertovpd/real-time_image-adudio_multiprocess/master/output/process.png "process")

My name is Alberto, I am Physicist and from my point of view, as well as the known work with data, a Data Scientist must know how to take the best of its software and hardware, minimizing deadtime between processes and maximizing the queue work of scripts.

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

### References:
    - The real-time image capturing script is based on this project:
        - https://github.com/sashagaz/Hand_Detection (Alexander Gazman).
        - It was written in Python 2 with deprecated code and I updated it to use it in Pyhon 3.6.

    - I used the recording_environment script just to check I could use all cores of my PC in the parallel process. The owner is:
        - https://gist.github.com/mabdrabo/8678538 (Mahmoud Abdrabo)
    
        
