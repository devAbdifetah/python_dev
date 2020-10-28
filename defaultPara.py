def exponent(num, power=2):
     return num ** power
print(exponent(2,3))#left is number and right is power total: 8
print(exponent(3))#9
print(exponent(7))#49

#switching arguments is not problem at all
print(exponent(power=3, num=4))
print(exponent(num=3, power=4))

def full_name(first="Abdifetah", last="Hassan"):
     return f"your full name is {first} {last}".title()
print(len(full_name()))
