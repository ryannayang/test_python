import datetime

today = datetime.datetime.today()
today = today.strftime("%d/%m/%Y")


def greeting(name):
    print(f"Hello {name}, welcome to our project! Today is {today}")


name = input("What is your name?")

greeting(name)
