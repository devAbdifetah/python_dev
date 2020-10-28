answer = all([char for char in 'eio' if char in 'eiku'])
answer1 = all([char for char in 'eio' if char in 'aeou'])
print(answer1)#
answer2 = all([num for num in [2,4,6,8,10] if num % 2 ==0])
answer3 = all([num for num in [1,4,6,7,10] if num % 2 ==0])
#print(answer3)
def is_all_strings(lst):
    return all(type(l) == str for l in lst)
#print(is_all_strings(['a','y','u','b',4]))
