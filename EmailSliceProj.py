# get user email address

email = input("what is your email address ?: ").strip()

# slice out user name

user =email[:email.index("@")]

#slice domain name

domain = email[email.index("@")+1:]

slicEmail = " your username is {} and your domain is {}".format(user, domain)
print(slicEmail)
