import simpleaudio as sa
import os

print("BASE SOUND ENGAGED")
filename = './input/base120.wav'
wave_obj = sa.WaveObject.from_wave_file(filename)
play_obj = wave_obj.play()
play_obj.wait_done()  # Wait until sound has finished playing
