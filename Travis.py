known_users = ["Ahmed", "Xasan", "Marwa", "dhoore", "Osman", "sayid"]
while True:
    print("hi name is  travis")
    name = input("What is your name? ").strip().capitalize()
    if name in known_users:
        print("Hello {}! ".format(name))
        remove = input("Would you like to be removed from the system(y/n)?: ").lower()
        if remove == "y":
            print(known_users)
            known_users.remove(name)
            print(known_users)
            
    else:
        print("Hmmmm, i don't  thinks i met you yet {} ")
        add_me = input("would you like to be added to the list?: ")
        if add_me =="y":
             print(known_users)
             known_users.append(name).strip().lower()
             print(known_users)
       
        
