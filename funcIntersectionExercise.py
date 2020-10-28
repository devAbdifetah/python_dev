def intersection(l1,l2):
     in_comon=[]
     for val in l1:
          if val in l2:
               in_comon.append(val)
               return in_comon
     return in_comon.count(val)
print(intersection([1,2,2,2],[1,2,2,2]))

#using list comprehension
def intersection(l1,l2):
     return {val for val in l1 if val in l2}
print(intersection(["cali","dhoore","axmed"],["cali","xasan","muuse"]))
