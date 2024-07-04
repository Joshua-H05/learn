import turtle

turtle.color("red")
a = 0
b = 0
turtle.speed(0)

while True:
    a += 5
    b += 2
    turtle.forward(a)
    turtle.right(b)
    if b == 360:
        break

turtle.done()