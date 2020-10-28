###using dictionary comprehension
##list1 = ["CA", "NJ", "RI"]
##list2 = ["Colifornia", "New jersey", "Rhode island"]
##answer = {list1[i]:list2[i] for i in range(0,3)}
##print(answer)
                # second solution with list indexes
person =[["name", "jared"],["job","musician"],["city","berlin"]]
answer = {thing[0]:thing[1] for thing in person}
print(answer)
         #secong solution without any reference to list indexes

answer = {k:v for k,v in person}
print(answer)         

             #last simple solution with dict
answer = dict(person)
print(answer)         
            #vowels dictionary exercise
answer = {char:"is a vowel" for char in "aeiou"}
print(answer)
print()
            #secon solution for vowels exercise
answer = dict.fromkeys("aeiou",0)
print(answer)

            #ASCII CODE EXERCISE for list cmprhnsion
answer ={count:chr(count) for count in range(65,91)}
print(answer)

for count in range(65,91):
     for char in chr(count):
         print(char)

         
