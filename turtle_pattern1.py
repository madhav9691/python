import turtle
win=turtle.Screen()
win.bgcolor("light blue")
t=turtle.Turtle()
t.color("red")
size=10
for i in range(20):
    t.forward(size)
    t.right(90)
    size+=5
turtle.exitonclick()
