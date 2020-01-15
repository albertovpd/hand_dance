# Hand Dance. Final project at Ironhack Madrid.

Hand Dance is an app that allows you to play music with your hand in front of a camera.

The app processes the position of the hand each frame, draws a square highlighting it and delivers a tone each 2 frames depending on the size of that square.

![alt](https://raw.githubusercontent.com/albertovpd/real-time_image-audio_multiprocess/master/output/mainpic2.png "mainpic")

Quick demo: https://youtu.be/0ksWsoNuMvk


### How it works:

In case you are using Python 3, from /src:

    python3 main.py -a "optional argument"

# Introduction:

This is an individual project to comprehend and research about:

    - OpenCV.
    - Sharing memory between not-finished Python scripts.
    - Multiprocesses and subprocesses.
    - Argparse.

The "normal" queue of work in Python is to perform a task, finish it, perform other task, repeat... What about performing several tasks at the same time while one of them is feeding others? For this, several parallel processes start, the most important ones:

    - just_video captures each frame and draws a square highlighting your hand, printing the corresponding tone and calculating the area of the square. This area is also written in memory constantly using pickle.

    - just_audio constantly reads in memory, unpick the area and prints the tone associated. Trying to read memory while writing provokes an error, so memory is read inside a try/except structure which prints "Hand frame casualty" when memory was read and written at the same time (the probability of happening is under 5%).

# Development.

The concept of "real-time", which is necessary in order to perform the idea, has been achieved in 2 different ways:

1. Sharing memory:


    Writing memory:

    ![alt](https://raw.githubusercontent.com/albertovpd/real-time_image-audio_multiprocess/master/output/writing_memory.png "writing")

    Reading memory:

    ![alt](https://raw.githubusercontent.com/albertovpd/real-time_image-audio_multiprocess/master/output/reading%20memory.png "Reading")
    
2. Subprocesses:

    Using the subprocess associated to the multiprocessing library, when a function finishes, another starts. That implies if you are displaying a webcam video, the screen freezes every time another scripts works. So it displays a frame, freezes, emits a tone, and so on.

    This is the workflow with subprocesses:
    
    ![alt](https://raw.githubusercontent.com/albertovpd/real-time_image-audio_multiprocess/master/output/process.png "subpro")

- All your music can be recorded and saved in a .mp3 file.

- All the notes played are displayed in a final plot, and saved it in .PDF format.

# Libraries:

        multiprocessing, subprocess, time, os, pickle, argparse, cv2, pyaudio, wave, numpy, matplotlib, synthesizer, simpleaudio.


# Conclusion

### Accomplished goals:

- Share memory between not finished scripts.
- Share tasks between all cores available in my PC.
- Working with multiprocessing library.
- Working with OpenCV.
- Work with video-audio in real-time.

### Future improvements:

- Optional parameters in init function to choose a concrete music scale to play.
- Increase the audio libraries to have different sounds.
- Find a way to minimize the "hand area casualties".
- Get a trained neural work that detects hands, to play both hands in function of the distance between them.

### References:

    - The real-time image capturing script is based on this project:
        - https://github.com/sashagaz/Hand_Detection (Alexander Gazman).
        - It was written in Python 2. I updated to Python 3.6 and used part of it to my purpose.

    - I used the recording_environment script just to check if I could use all cores of my PC in the parallel process. The owner is:
        - https://gist.github.com/mabdrabo/8678538 (Mahmoud Abdrabo)

        
