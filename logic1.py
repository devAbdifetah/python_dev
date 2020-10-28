ticket = int(input('Enter your price: '))
#adult_price=int(input(''))
if ticket >0 and ticket <= 2:
     print('you paid child price')
elif ticket > 0 and ticket <=5:
     print('you paid adult price')
     
else:
     print('that price is not availabe')
