# import turtle

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
# import random
# turtle.pensize(5)

# for i in range(0, 8):
#     turtle.color(random.choice(["red", "yelollow", "green", "blue", "black"]))
#     turtle.forward(100)
#     turtle.right(45)

# Розетка
# import random
# for x in range(0, 10):
#     for i in range(0, 8):
#         turtle.color(random.choice(
#             ["red", "green", "blue", "black"]))
#         turtle.forward(100)
#         turtle.right(45)
#     turtle.right(36)
# turtle.hideturtle()

# Рандомный Узор
# import random

# lines = random.randint(5, 50)

# for x in range(0, lines):
#     lenght = random.randint(25, 100)
#     rotate = random.randint(1, 365)
#     turtle.forward(lenght)
#     turtle.right(rotate)

# turtle.exitonclick()


# Кортеж
# country = ("USA", "China", "England")
# print(country)
# d = input("Введите любое название страны из списка country: ")
# print(country.index(d))
# b = int(input("Введите index из кортежа coutry: "))
# print(country[b])

# sport = ["Тенис", "Гребля"]
# sport.append(input("Ваш любимый вид спорта?: "))
# sport.sort()
# print(sport)

# items = ["математика", "физика", "химия", "литература", "физкультура"]
# print(items)
# dislike = (input("Выберите предметы каторые вым не нравятся: "))
# getrid = items.index(dislike)
# del items[getrid]
# print(items)

dishes = {}
food1 = input("Введите любимое блюдо: ")
dishes[1] = food1
food2 = input("Введите любимое блюдо: ")
dishes[2] = food2
food3 = input("Введите любимое блюдо: ")
dishes[3] = food3
food4 = input("Введите любимое блюдо: ")
dishes[4] = food4
food5 = input("Введите любимое блюдо: ")
dishes[5] = food5
print(dishes)
dislike = int(input("Какие блюда вам не нравятся?: "))
del dishes[dislike]
print(sorted(dishes.values()))
