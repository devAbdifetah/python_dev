##for i in range(1,11):
##     print("the value is {:03}".format(i))
##
##pi = 3.14159265
##sentence = 'Pi is equal to {:.2f}'.format(pi)
##print(sentence)
##
##     
class BankAcc:
     def __init__(self):
          self.balance=0
          print("Hello,!!! Welcome to the deposit and withdrawn machine")
     def deposit(self):
          amount = float(input("Enter amount to be deposited: "))
          if amount <=0:
              print("please Enter valid amount")
          else:
               
              self.balance+=amount
              print("you deposited ",amount,'Rubees')
         
     def withdraw(self):
          amount = float(input("Enter the Amout to be withdrawn: "))
          if self.balance > amount:
               if amount < 0:
                    print("please Enter valid amount")
               else:     
                    self.balance-=amount
                    print("you withdrawn ",amount,'Rubees')

          else:
               print("insificient money")

     def display(self):
          print("the net availabe balance = ",self.balance,'rubees')

#creating an object of the class
s = BankAcc()
s.deposit()
s.withdraw()
s.display()
#s.withdraw()
