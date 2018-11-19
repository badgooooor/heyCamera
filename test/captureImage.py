import subprocess
import os
import signal
import time


def capture():
    os.chdir("C:\Program Files (x86)\Java\jdk1.8.0_74\\bin")
# subprocess.run(["dir"], shell=True, check=True)
    capture = subprocess.Popen(["java","code.SimpleRead"]).pid
    time.sleep(processTime)
    os.kill(capture, signal.SIGTERM)

capture()