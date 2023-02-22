import datetime

today = datetime.datetime.today()
today = today.strftime("%d/%m/%Y")


def greeting(name):
    print(f"Hello {name}, Welcome to our project!")


def datetime_request():
    date_input = input("Would you like to know what the date is? (y/n): ")
    if date_input.lower() == "y" or date_input.lower() == "yes":
        print(f"Okay, Today is {today}")
    else:
        print("Okay, Have a great day :)")


name = input("What is your name? ")

greeting(name)
datetime_request()
