users =[
     {"username": "hasen", "tweets": ["i love cake", "i love pie"]},
     {"username": "dhoore", "tweets":["i love my car"]},
     {"username": "nuuradin", "tweets": []},
     {"username": "sayid", "tweets": []},
     {"username": "xuseen", "tweets":["camels are the best","I'm hungry"]},
     {"username": "osman", "tweets": []}
]
usernames = list(map(lambda user: user['username'].upper(),
                     filter(lambda u: not u['tweets'],users)))
print(usernames)
