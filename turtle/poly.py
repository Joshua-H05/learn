import turtle

turtle.speed(0)

def draw_star(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("red", "yellow")

    turtle.begin_fill()

    for i in range(36):
        turtle.forward(150)
        turtle.left(170)

    turtle.end_fill()

turtle.getscreen().onclick(draw_star)
turtle.done()
