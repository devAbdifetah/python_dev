age = (input("What is your age please? "))
if age:
     age=int(age)
     if age >= 18 and age <=21:
          #18-21
          print("you can't enter but need wristband")
     elif age >=21:
          #21+drink, normal entry
          print('you are good to enter and drink!')
     else:
          print("you can't enter, a little one stay at home")

else:
     print('Enter the exact age')

