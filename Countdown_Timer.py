#This code defines a CountdownTimer class with an _init_ method to initialize the timer with a given number of seconds, and a start_countdown method to begin the countdown. The get_user_input function is used to get a valid integer input from the user.

#When you run this script, it will prompt you to enter the number of seconds for the countdown, and then it will start the countdown. During the countdown, the script will print the time remaining every second.

import time

class CountdownTimer:
    def __init__(self, seconds):
        self.seconds = seconds

    def start_countdown(self):
        print(f"Countdown started for {self.seconds} seconds.")
        while self.seconds > 0:
            print(f"Time remaining: {self.seconds} seconds")
            time.sleep(1)
            self.seconds -= 1
        print("Countdown complete!")

def get_user_input():
    try:
        seconds = int(input("Enter the number of seconds for the countdown: "))
        return seconds
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return get_user_input()

if __name__ == "__main__":
    seconds = get_user_input()
    timer = CountdownTimer(seconds)
    timer.start_countdown()

    