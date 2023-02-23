import calendar
import datetime
from time import sleep

today = datetime.datetime.today()
today = today.strftime("%d/%m/%Y")
day_of_week = datetime.datetime.today().strftime("%A")


def greeting(name, color):
    print(f"Hello {name}, Welcome to our project!")
    sleep(1)
    print(f"{color} is a great color!")


def datetime_request():
    date_input = input("Would you like to know what the date is? (y/n): ")
    if date_input.lower() == "y" or date_input.lower() == "yes":
        print(f"Okay, Today is {day_of_week} {today}")
    else:
        print("Okay, Have a great day :)")

        

name = input("What is your name? ")
color = input("What is your favorite color? ")

greeting(name, color)
datetime_request()
