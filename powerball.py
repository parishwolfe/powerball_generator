####################################
#     Pwrball Number Generator     #
####################################

#import / installation
try:
    import pytz
    from tzlocal import get_localzone
    from colorama import init
    from termcolor import colored
    init(autoreset=True)
except ModuleNotFoundError:
    import sys
    import subprocess

    def install(package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
    install("colorama")
    install("termcolor")
    install("pytz")
    install("tzlocal")
    print("\n\n\ninstalled missing dependencies, please run again!")
    exit()
import random
from datetime import datetime, timedelta


#global variables
repeat = 5
local_tz = get_localzone()
draw_tz = pytz.timezone('America/New_York')

#global functions
def fmt(n):
    """format number with a space in front if it is single digit"""
    if n < 10:
        return " " + str(n)
    else:
        return str(n)

def _w_():
    """generate a white number"""
    return random.randint(1, 69)
        
def _r_():
    """generate a red number"""
    return random.randint(1, 26)
    
def generate():
    """generate numbers"""
    numbers = []
    while len(numbers) < 5:
        j = _w_()
        if j not in numbers:
            numbers.append(j)
    numbers.append(_r_())
    return numbers


def show_numbers(numbers=None, show_lucky=False):
    """format and print numbers"""
    if numbers == None: numbers = generate()
    lucky = False
    for i in range(len(numbers) - 1):
        if numbers[i] == numbers[-1]:
            lucky = True
        numbers[i] = colored(fmt(numbers[i]), "white")
    numbers[-1] = colored(fmt(numbers[-1]), "red")
    output = "  ".join(numbers)
    if lucky == True and show_lucky == True: output += colored(" *", "yellow")
    return print(output)

def next_drawing():
    for i in range(4):
        t = (datetime.now(tz=local_tz) + timedelta(days=i)).astimezone(draw_tz)
        if t.weekday() == 2 or t.weekday() == 5:
            t = t.replace(hour=22, minute=59, second=0, microsecond=0)
            return t
    raise EnvironmentError

def time_till_next_drawing():
    difference = next_drawing() - datetime.now(tz=local_tz)
    return difference



if __name__ == "__main__":
    print("Good Luck!")
    while repeat != 0:
        show_numbers(show_lucky=True)
        repeat -= 1
    print("until next drawing: ", time_till_next_drawing())
    print("next drawing: ", next_drawing())


#cspell:ignore astimezone pytz tzlocal Pwrball
