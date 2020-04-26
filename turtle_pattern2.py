import turtle
win=turtle.bgcolor("light yellow")
t=turtle.Turtle()
t.color("red")
def my_func(size):
    t.circle(size)
    t.circle(-size)

x=10
for i in range(8):
    my_func(x)
    x+=5
turtle.done()
