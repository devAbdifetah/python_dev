def display_names(first, second):
     print(f"{first} says hello to {second}".title())

#names = {"first": "abdifetah", "second": "osman dhoore"}
#display_names(first="abdifetah", second="sayid")
#display_names(names) error
#display_names(**names)

def add_and_multiply_numbers(a,b,c, **kwargs):
     print(a+b*c)
     print("OTHER STUFF....")
     print(kwargs)

data =dict(a=1,b=2,c=3, d=55, name="tony")
add_and_multiply_numbers(**data, cat="blue")
