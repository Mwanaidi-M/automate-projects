"""
Project: Simple Countdown Program

This is a countdown program that plays an alarm at the end of the countdown.

At a high level, here’s what your program will do:
• Count down from 60.
• Play a sound file (alarm.wav) when the countdown reaches zero.

This means your code will need to do the following:
• Pause for one second in between displaying each number in the countdown by calling time.sleep().
• Call subprocess.Popen() to open the sound file with the default application.
"""

import time, subprocess

time_left = 10

while time_left > 0:
    print(time_left)
    time.sleep(1)
    time_left -= 1

# At the end of the countdown, play a sound file.
subprocess.Popen(["start", "mixkit-classic-alarm-995.wav"], shell=True)



