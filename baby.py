from random import choice

questions = ["where are you bro?: ",
             "what is your name?: ",
             "how many children have you?: "
             ]
question = choice(questions).strip().lower()
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("why?")

print("Oh.. ok")
