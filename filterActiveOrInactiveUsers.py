user =[
     {"username": "hasen", "tweets": ["i love cake", "i love pie"]},
     {"username": "dhoore", "tweets":["i love my car"]},
     {"username": "nuuradin", "tweets": []},
     {"username": "sayid", "tweets": []},
     {"username": "xuseen", "tweets":["camels are the best","I'm hungry"]},
     {"username": "osman", "tweets": []}
]

##inactiveUsers = list(filter(lambda u: len(u["tweets"])==0,user))
##print(inactiveUsers)
activeUsers = list(filter(lambda u: u["tweets"],user))
inactiveUsers = list(filter(lambda u: not u["tweets"],user))
print(activeUsers)
