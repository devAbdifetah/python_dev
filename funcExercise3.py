#program that multiplies all even numbers
def multiply_even_numbers(lst):
    total = 1
    for val in lst:
        if val % 2 == 0:
            total = total * val
    return total
print("the total of even numbers are: ",multiply_even_numbers([2,3,4,5,6]))
