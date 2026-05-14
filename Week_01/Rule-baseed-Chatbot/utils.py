import datetime
import random
import string


# TIME

def current_time():
    return datetime.datetime.now().strftime("Current time: %I:%M %p")


# DATE

def current_date():
    return datetime.datetime.now().strftime("Today's date: %d-%m-%Y")


# CALCULATOR

def calculate(num1, operator, num2):

    if operator == "+":
        return num1 + num2

    elif operator == "-":
        return num1 - num2

    elif operator == "*":
        return num1 * num2

    elif operator == "/":

        if num2 == 0:
            return "Cannot divide by zero"

        return num1 / num2

    else:
        return "Invalid operator"


# PASSWORD GENERATOR

def generate_password(length=12):

    characters = string.ascii_letters + string.digits + "@#$%"

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return f"Generated Password: {password}"


# NUMBER GAME
    print("Bot: Invalid input")