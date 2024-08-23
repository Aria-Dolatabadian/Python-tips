# import the time module and the notification module from plyer
import time
from plyer import notification

# define the countdown function
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    # Pop-up notification when the countdown ends
    notification.notify(
        title="Time to !",
        message="Message",
        timeout=10  # duration in seconds
    )
    print("Time's Up!")

# input time in seconds
t = input("Enter the time in seconds: ")

# function call
countdown(int(t))
