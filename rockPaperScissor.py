player1 = input("player1 move your turn: ")
player2 =input("player2 move your turn: ")

if player1 =="rock" and player2=="scissor":
    print("player1 wins")
elif player1 == "rock" and player2 == "paper":
    print("player2 wins")
elif player1 == "paper" and player2 == "rock":
    print("player1 wins!")
elif player1 == "paper" and player2 == "scissor":
    print("player2 wins!")
elif player1 == "scissor" and player2 == "rock":
    print("player2 wins!")
elif player1 == "scissor" and player2 == "paper":
    print("player1 wins")
elif player1 == player2:
    print("barbaro")
else:
    print("something went wrong")      
    
