import subprocess
from sensors import *

subprocess.run(["npm",  "--prefix", "/home/peter/bot_car/app/client", "run", "build"])
subprocess.run(["python3", "/home/peter/bot_car/app/server/server.py"])

on = True
while on:
    print(ultrasonic())
