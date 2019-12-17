import subprocess

subprocess.run("python3 ./src/video_audio.py & python3 ./src/base_sound.py", shell=True)    

import psutil
import subprocess
subp = subprocess.Popen(['./src/video_audio.py'])

p = psutil.Process(subp.pid)
try:
    p.wait(timeout=20)
except psutil.TimeoutExpired:
    p.kill()
    raise