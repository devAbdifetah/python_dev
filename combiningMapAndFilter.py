names = ['tony','lucky','dhoore']
teacher=list(map(lambda name: f"your instructor is {name}",
         filter(lambda value: len(value)< 5,names)))
print(teacher)
