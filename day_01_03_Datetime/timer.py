"""
This script crete a timer.
Pressing the spacebar will start the timer.
Pressing the spacebar again will stop the timer.
Successfull "laps" will be displat until the reset button is pressed.
"""
from datetime import datetime

lap = 1
start = True

while lap < 100:
    print("Press spacebar to start and stop the timer")
    input()
    start = datetime.today() 
    print("Lap", lap, "Starting time:",start)
    input()
    stop = datetime.today()
    print("Lap", lap, "Stop time:",stop)
    print("Lap", lap, "Total time:", stop-start)
    print("")

    lap += 1
