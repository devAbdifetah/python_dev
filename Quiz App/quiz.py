score = 0
#Question
answer1 = input("What is the capital city Djihbouti? \na. ali sabih \nb. tajorah \nc Djibouti \nAnswer: ")
if answer1 == "c" or answer1 == "Djibouti":
    score += 1
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect!")
    print("Score: ", score)
    print("\n")