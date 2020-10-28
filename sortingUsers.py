users =[
     {"username": "hasen", "tweets": ["i love cake", "i love pie"]},
     {"username": "dhoore", "tweets":["i love my car"]},
     {"username": "nuuradin", "tweets": [],"color": "teal"},
     {"username": "sayid", "tweets": [],"color":"purple"},
     {"username": "xuseen", "tweets":["camels are the best","I'm hungry"]},
     {"username": "osman", "tweets": []}
]
#print(sorted(users, key=len))
print(sorted(users, key=lambda user: user["username"]))
print()
print(sorted(users, key=lambda user: len(user["tweets"])))
