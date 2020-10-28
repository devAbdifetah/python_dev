def yell(word):
     return "{}!".format(word.upper())
print(yell("hello"))

def yell(word):
     return word.upper()+"1"
print(f"hello".upper(),yell("dhoore"))

#colt's personal favorite string formating just not works fo usemy
def yell(word):
     return f"{word.upper()}!"
print(f"war yaa".upper(),yell("dhoore"))
