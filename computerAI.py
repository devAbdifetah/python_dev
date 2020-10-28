from random import randint
player = input("player, make your move: ").lower()
rand_num = randint(0,2)
if rand_num == 0:
    computer ="rock"
elif rand_num ==1:
    computer = "paper"
else:
    computer = "scissors"

print(f"computer plays {computer} ")

if player == computer:
    print("Its a tie")
elif player =="rock":
    if computer == "scissors":
        print("player wins")
    else:
        ("computer wins")

elif player == "paper":
    if computer == "rock":
        print("player wins")
    else:
         print("comoputer wins")
elif player == "scissors":
    if computer == "paper":
        print("player wins")
    else:
        print("computer wins")
else:
    print("please enter a valid move")
