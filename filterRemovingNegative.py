def removeNegative(nums):
     return list(filter(lambda l: l>0,nums ))
print(removeNegative([1,234,-6,4,-9]))
