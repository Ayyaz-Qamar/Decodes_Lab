import random
import datetime

print("\n=======================================")
print("      DecodeLabs AI Assistant")
print("=======================================")
print("Type 'help' for commands")
print("Type 'bye' to exit\n")


# -----------------------------
# RESPONSE DATABASE
# -----------------------------

greetings = ["hello", "hi", "hey", "salam", "assalamualaikum"]

greeting_responses = [
    "Hello! How can I assist you?",
    "Hi there!",
    "Hey! What do you need?",
    "Welcome!"
]

joke_keywords = ["joke", "funny", "laugh"]

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Python devs don't sleep, they just wait for errors.",
    "AI will not replace humans, but humans using AI will replace others."
]

how_are_you_keywords = ["how are you", "how r you", "how you doing"]

motivation_keywords = ["motivate", "motivation", "inspire"]

motivations = [
    "Discipline beats motivation.",
    "Consistency creates success.",
    "Stop thinking, start building.",
    "Your future is created by what you do today."
]


# -----------------------------
# MAIN LOOP
# -----------------------------

while True:

    user_input = input("You: ").strip().lower()

    # -------------------------
    # EMPTY INPUT
    # -------------------------
    if not user_input:
        print("Bot: Please enter something.")
        continue


    # -------------------------
    # EXIT
    # -------------------------
    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Session ended.")
        break


    # -------------------------
    # GREETINGS (keyword based)
    # -------------------------
    elif any(word in user_input for word in greetings):
        print("Bot:", random.choice(greeting_responses))


    # -------------------------
    # HOW ARE YOU
    # -------------------------
    elif any(phrase in user_input for phrase in how_are_you_keywords):
        print("Bot: I'm functioning properly and ready to assist you.")


    # -------------------------
    # BOT NAME / IDENTITY
    # -------------------------
    elif "your name" in user_input or "who are you" in user_input:
        print("Bot: I am DecodeLabs AI Assistant built by Ayyaz Qamar using rule-based logic.")


    # -------------------------
    # TIME
    # -------------------------
    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print("Bot: Current time is", current_time)


    # -------------------------
    # DATE
    # -------------------------
    elif "date" in user_input:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", current_date)


    # -------------------------
    # JOKES
    # -------------------------
    elif any(word in user_input for word in joke_keywords):
        print("Bot:", random.choice(jokes))


    # -------------------------
    # MOTIVATION
    # -------------------------
    elif any(word in user_input for word in motivation_keywords):
        print("Bot:", random.choice(motivations))


    # -------------------------
    # PYTHON CODE REQUEST
    # -------------------------
    elif "python" in user_input and "code" in user_input:

        print("""
Bot: Example Python Code:

def greet():
    print("Hello World")

greet()
""")


    # -------------------------
    # PYTHON EXAMPLE
    # -------------------------
    elif "python example" in user_input:

        print("""
Bot: Simple Python Example:

name = input("Enter your name: ")
print("Hello", name)
""")


    # -------------------------
    # HELP MENU
    # -------------------------
    elif user_input == "help":

        print("""
================ COMMANDS ================

Greetings:
- hello / hi / hey

Info:
- how are you
- your name
- time
- date

Fun:
- joke
- motivate me

Programming:
- python code
- python example

System:
- bye / exit

=========================================
""")


    # -------------------------
    # FALLBACK (IMPORTANT FIX)
    # -------------------------
    else:
        print("Bot: I'm sorry, I can't understand that question.")