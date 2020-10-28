class Student:
     #the below block defines the attributes
     def __init__(self,name,age,marks):
          self.name=name
          self.age=age
          self.marks = marks
     def talk(self):
          print("hi my name",self.name)
          print("hello my age is ",self.age)
          print("my marks are ",self.marks)

#creating objects and instances
ss = Student('dhoore',34,890)
ss.talk()
##print(ss.name)
##print(ss.age)
##print(ss.marks)
