import turtle

# turtle.color("black", "red")
# turtle.begin_fill()
# for i in range(0, 4):
#     turtle.forward(50)
#     turtle.right(90)
# turtle.penup()
# turtle.end_fill()
# turtle.forward(100)
# turtle.pendown()

# turtle.color("black", "green")
# turtle.begin_fill()
# for i in range(0, 4):
#     turtle.forward(50)
#     turtle.right(90)
# turtle.penup()
# turtle.end_fill()
# turtle.forward(100)
# turtle.pendown()

# turtle.color("black", "yellow")
# turtle.begin_fill()
# for i in range(0, 4):
#     turtle.forward(50)
#     turtle.right(90)
# turtle.penup()
# turtle.end_fill()
# turtle.forward(100)
# turtle.pendown()

# Звезда
# for i in range(0, 5):
#     turtle.forward(150)
#     turtle.right(144)

# Цифры
# turtle.penup()
# turtle.right(180)
# turtle.forward(500)
# turtle.left(90)
# turtle.forward(200)
# turtle.right(180)
# turtle.pendown()
# turtle.forward(200)
# turtle.right(90)
# turtle.penup()
# turtle.forward(100)
# turtle.pendown()
# turtle.forward(150)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(150)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(150)
# turtle.penup()
# turtle.forward(100)
# turtle.pendown()
# turtle.forward(150)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(70)
# turtle.left(180)
# turtle.forward(70)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(150)
# turtle.hideturtle()

# Восмиугольник
import random
turtle.pensize(5)

for i in range(0, 8):
    turtle.color(random.choice(["red", "yelollow", "green", "blue", "black"]))
    turtle.forward(100)
    turtle.right(45)

turtle.exitonclick()
