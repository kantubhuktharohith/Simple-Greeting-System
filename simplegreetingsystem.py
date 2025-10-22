import datetime

now = datetime.datetime.now()

current_hour = now.hour

name = input("what is your name? ")

if current_hour < 12:
    greeting = "Good Morning"

elif current_hour < 18:
    greeting = "Good Afternoon"

else:
    greeting = "Good Evening"

print(f"Hello, {greeting} {name} It's nice to meet you.")     