names = [
     {'first':'Rusty','last':'steele'},
     {'first':'colt','last':'steele'},
     {'first':'dhoore','last':'steele'}
     
]
first_names =list(map(lambda x: x['first'],names))
print(first_names)

#making upper casing the list of people
people = ["yasir","osman", "sayid","nooradin"]
peeps = list(map(lambda name: name.title(), people))
print(peeps)
     
