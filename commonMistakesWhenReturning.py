##def sum_odd_numbers(numbers):
##     total=0
##     for num in numbers:
##          if num % 2 !=0:
##               total+=num
##          return total #mistake is here(la sim for loop-ka fadlan)
##print(sum_odd_numbers([1,2,3,4,5,6,7]))#output will be 1
def sum_odd_numbers(numbers):
     total=0
     for num in numbers:
          if num % 2 != 0:
               total+=num
     return total
print(sum_odd_numbers([1,2,3,4,5,6,7]))

























