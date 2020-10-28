#my solution for  these exercise     
##lst = [1,2,3]
##decrement_list = list(map(lambda n: n-1,lst))
##print(decrement_list)
##
##def decrement_list(l):
##    return list((map(lambda n: n-1, l)))
##print(decrement_list([4,5,6]))
import functools
lst = [1,2,3,4]
lst1=functools.reduce(lambda x,y: x*y, lst)
print(lst1)
 

