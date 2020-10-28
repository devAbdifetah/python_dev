square ={x**2 for x in range(10)}
#print(square)
string = 'sequoie'
def are_all_vowels_in_string(string):
     return len({char for char in string if char in 'aeiou'})==5
print(are_all_vowels_in_string(string))
##answer = len({char for char in string if char in 'aeiou'})
##print(answer)
##

#Generating evens using a list comprehension:
def generate_evens():
    return [x for x in range(1,50) if x%2 == 0]


#Generating evens using a loop:
def generate_evens():
    result = []
    for x in range(1,50):
        if x % 2 == 0:
            result.append(x)
    return result
print(generate_evens())
