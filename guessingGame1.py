##import random
##random_num = random.randint(1,10) #number 1 - 10
##guess = None
##while guess != random_num:
##    guess = input("pick a number from 1 to 10: ")
##    guess = int(guess)
##    if guess < random_num:
##        print("TOO LOW")
##    elif guess > random_num:
##        print("TOO HIGH!")
##    else:
##        print("YOU WON!")
##
##print(random_num)        

import random
random_num = random.randint(1,4) #number 1 - 10
guess = None

while True:
    guess = input("pick a number from 1 to 10: ")
    guess = int(guess)
    if guess < random_num:
        print("TOO LOW")
    elif guess > random_num:
        print("TOO HIGH!")
    else:
        print("YOU WON!")
        play_again = None
        play_again = input("do you want play again? (yes/no) ")
        if play_agian == "yes":
            random_num = random.randint(1,4)
            guess = ""
        else:
            print("thank you for playing")
            break

        

