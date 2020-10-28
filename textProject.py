# Ask user for name

name = input("what is your name?: ")

# Ask user for age

age = input("how old are you?: ")

# Ask user for city

city = input("what city do you live in?: ")

# Ask user what they love

love = input("what do you love doing?: ")

# create output text

string = "Your name is {} and you are {} years old. you live in {} and you love {}"
output = string.format(name, age, city, love)
# Print output to screen
print(output)


