import pyaudio
import wave

print("RECORDING ENGAGED")
def recording_all():       
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 35
    WAVE_OUTPUT_FILENAME = "../output/song_and_environment.wav"
    
    audio = pyaudio.PyAudio()
    
    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    frames = []
    
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    
    
    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
    
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    print("RECORDING FINISHED")
recording_all()

# record video and mix all  
# import cv2

# if __name__ == "__main__":
#     # find the webcam
#     capture = cv2.VideoCapture(0)

#     # video recorder
#     fourcc = cv2.VideoWriter_fourcc(*'XVID')  # cv2.VideoWriter_fourcc() does not exist
#     video_writer = cv2.VideoWriter("output.avi", fourcc, 20, (680, 480))

#     # record video
#     while (capture.isOpened()):
#         ret, frame = capture.read()
#         if ret:
#             video_writer.write(frame)
#             cv2.imshow('Video Stream', frame)

#         else:
#             break

#     capture.release()
#     video_writer.release()
#     cv2.destroyAllWindows()
