import turtle
my_turtle = turtle.Turtle()
my_turtle.speed(0)

def square(length, angle):
   for i in range(4):
       my_turtle.forward(lenght)
       my_turtle.right(angle)


for i in range(40):
    square(100, 90)
    my_turtle.right(10)
