age = input("how old are you: ")

if age:
    age = int(age)
    if age >=18 and age<=21:
        print("you can enter but need wrisband")
    elif age >=21:
        print("you are goood to enter and drink")
    else:
        print("you cant come in, little one")
else:
    print("please enter valid number")          
              
