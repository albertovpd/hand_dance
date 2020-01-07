# Final project at Ironhack Madrid: 

Play music with your hand in front of your webcam, thanks to sharing memory between processes and multiprocess library

# Hand-dance
This script pe
Depending on the options you select while running the script, this program perform several task
This program receives inputs through terminal, deliver custom graphs and save it in PDF. 
I have been working with datasets and performing web scraping to show the mean price of electricity per year, the mean price one day ahead per year (due to forecast changes and other factors the price of energy one day ahead is important, affects the price the day after) and the rise of minimum salary income. 

- Help and display through terminal
![alt text](https://github.com/albertovpd/pipelines-project/blob/master/output/terminal%20example.png "final result")

- Popup graphs through terminal
![alt text](https://github.com/albertovpd/pipelines-project/blob/master/output/output%20example.png "terminal")

- Web scraping
![alt text](https://raw.githubusercontent.com/albertovpd/pipelines-project/master/output/web-enriching.png "web enriching")

# Introduction:

This is an individual project to comprehend and research about:

    - OpenCV.
    - Multiprocesses and subprocesses.
    - Sharing memory between Python scripts without having finished in real-time (that was the milestone)

I wanted to develop some script to play music with both hands, so I started looking for trained neural networks, there are some great ones to detect hands... Then reality struck me... The normal queue of work in Python is to perform a task, finish it and perform other task. Repeat. What about performing several tasks at the same time?

The concept of "real-time", which is necessary in order to perform the idea, has been tricky until I found some ways of getting what I wanted:
1. subprocesses:

# Libraries:

        uncertain_panda,pandas, numpy, requests, bs4, matplotlib, sys, argparse,subprocess.


# Description and results:

The main idea was to create a huge dataset relating price of electric energy depending of its source (oil, coal, renewables), per hour, with the climate historic. It was hard to find a for free weather API for all request I need to perform, so finally, I did the following:

- Take all registers of price of energy per hour within the last 4 years (I could not find a bigger dataset with this info).
    https://www.kaggle.com/nicholasjhana/energy-consumption-generation-prices-and-weather

- Perform the mean  per year <b>with its associated uncertainty</b>, in order to have a real measure.

- Web scraping: relate this 4 years of average electric price with the average salary in Spain.
    https://datosmacro.expansion.com/mercado-laboral/salario-medio/espana

- Pipelines. Save related functions in the same script and call them when necessary.
    - From main.py: calling functions in other scripts, creating my function to work through terminal.
    - From web_enriching: performing web scraping.
    - From processing_functions.py: cleaning the dataset, calling functions from the file web_enriching.py to enrich my dataset, developing my key function, the ultimate one which takes arguments through terminal (it is called from main.py and work with the input arguments plotting columns of the dataset).

### How it works:

In case you are using Python 3, from /src:

    python3 main.py -a "first optional argument" -b "second optional argument"

# Conclusion

### Accomplished goals:

- Develop an effective pipeline with clean code.
- Run a script with different optional parameters through terminal.
- Understand the basics of web scraping.
- Show uncertainties associated with measures or statistic methods.
- Display graphs through terminal.
- Save your plots

### Future improvements:

- Better plot labellings 
- Enlarge the dataset.
- Apply ML to predict future prices.
- Finish the graph results with proper label and legends.
- Send by mail the asked results.



























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

### References:
    - The real-time image capturing script is based on this project:
        - https://github.com/sashagaz/Hand_Detection (Alexander Gazman).
        - It was written in Python 2 with deprecated code and I updated it to use it in Pyhon 3.6.

    - I used the recording_environment script just to check I could use all cores of my PC in the parallel process. The owner is:
        - https://gist.github.com/mabdrabo/8678538 (Mahmoud Abdrabo)
    
        
