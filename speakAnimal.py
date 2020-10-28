def speak(animal="dog"):
    if animal=="dog":
        return "woof"
    elif animal=="pig":
        return "oink"
    elif animal=="duck":
        return "quak"
    elif animal=="cat":
        return "meow"
    else:
        return "?"
print(speak("cat"))
