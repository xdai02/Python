import turtle

turtle.hideturtle()
turtle.pensize(20)
turtle.bgcolor("black")

pos = [(0, 0), (-5, 13), (-5, 5)]
colors = ["red", "cyan", "white"]

for (x, y), color in zip(pos, colors):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.left(180)
    turtle.circle(50, 270)
    turtle.forward(120)
    turtle.left(180)
    turtle.circle(50, 90)

turtle.mainloop()