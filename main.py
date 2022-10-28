import turtle


def draw_eye(x, y):
    turtle.penup()
    turtle.home()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.left(90)
    turtle.fd(8)

    turtle.left(90)
    turtle.fd(2)

    turtle.left(45)
    turtle.fd(20)

    turtle.left(45)
    turtle.fd(8)

    turtle.left(90)
    turtle.fd(30)

    turtle.left(90)
    turtle.fd(8)

    turtle.left(90)
    turtle.fd(8)

    turtle.left(75)
    turtle.circle(-5, 250)


def draw_nose(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.left(90)
    turtle.circle(-5, 180)

    turtle.left(180)
    turtle.fd(5)

    turtle.circle(5, 180)
    turtle.fd(5)


def draw_mouse(x, y):
    turtle.left(45)
    turtle.circle(80, 90)
    # print(turtle.pos()) (43.14,-5.00)

    turtle.penup()
    position_end = turtle.pos()
    turtle.goto(position_end[0]-3, position_end[1]+5)
    turtle.pendown()

    turtle.right(130)
    turtle.circle(10, 90)

    turtle.penup()
    turtle.goto(x+3, y+3)
    turtle.pendown()

    turtle.right(110)
    turtle.circle(-10, 90)

    turtle.penup()
    turtle.home()
    turtle.goto(x + position_end[0], y + position_end[1]-18)
    turtle.pendown()

    turtle.fillcolor("black")
    turtle.begin_fill()

    turtle.right(10)
    turtle.circle(70, 50)

    turtle.left(60)
    turtle.circle(30, -170)
    turtle.end_fill()

    turtle.penup()
    turtle.home()


turtle.speed(10000)

turtle.penup()
turtle.goto(-60, 50)
turtle.pendown()

turtle.write("KDK", font=("Arial", 14, "bold"))

turtle.penup()
turtle.goto(-50, 50)
turtle.pendown()



turtle.fillcolor("orange")
turtle.begin_fill()
turtle.circle(-60, -170)
turtle.left(10)

turtle.back(20)

turtle.right(90)
turtle.circle(-5, 180)
turtle.left(90)

turtle.fd(40)
# print(turtle.pos()) (9.58,-69.09)

turtle.circle(60, 170)
turtle.left(10)

turtle.fd(40)

turtle.left(90)
turtle.circle(-5, 180)
turtle.right(90)
# print(turtle.pos()) (-30.00,50.00)

turtle.back(20)
turtle.end_fill()

turtle.penup()
turtle.goto(-20.00, 50.00)
turtle.pendown()

turtle.fillcolor("#36E830")
turtle.begin_fill()
turtle.left(45)
turtle.fd(40)

turtle.right(65)
turtle.fd(8)
# print(turtle.pos()) (15.80,75.55)

turtle.right(115)
turtle.fd(38)
turtle.left(180)
position = turtle.pos()
turtle.end_fill()

turtle.penup()
turtle.home()
turtle.pendown()


turtle.penup()
turtle.goto(15.80, 75.55)
turtle.pendown()
turtle.fillcolor("green")
turtle.begin_fill()
turtle.right(25)
turtle.fd(8)
turtle.right(160)
turtle.circle(11, 160)
turtle.right(155)
turtle.fd(25)
turtle.right(135)
turtle.fd(35)
turtle.end_fill()


turtle.penup()
turtle.home()
turtle.pendown()

turtle.penup()
turtle.goto(-45.00, 20.00)
turtle.pendown()

turtle.fillcolor("black")
turtle.begin_fill()
draw_eye(-45.00, 20.00)
turtle.end_fill()
turtle.penup()
turtle.home()
turtle.pendown()

turtle.penup()
turtle.goto(10, 20.00)
turtle.pendown()

turtle.fillcolor("black")
turtle.begin_fill()
draw_eye(10, 20.00)
turtle.end_fill()
turtle.penup()
turtle.home()
turtle.pendown()


turtle.fillcolor("black")
turtle.begin_fill()
draw_nose(-25, -10)
turtle.end_fill()


turtle.penup()
turtle.goto(-70, -5)
turtle.pendown()


draw_mouse(-70, -5)

turtle.penup()
turtle.goto(12, -69)
turtle.pendown()

turtle.left(150)
turtle.circle(-8, 170)

turtle.penup()
turtle.goto(30, -50)
turtle.pendown()

turtle.left(150)
turtle.circle(-12, 170)

turtle.penup()
turtle.goto(40, -55)
turtle.pendown()

turtle.left(150)
turtle.circle(-8, 170)

turtle.penup()
turtle.goto(-70, -45)
turtle.pendown()

turtle.left(90)
turtle.circle(-11, 210)

turtle.penup()
turtle.goto(-80, -35)
turtle.pendown()

turtle.left(90)
turtle.circle(-8, 150)

turtle.penup()
turtle.goto(-75, 25)
turtle.pendown()

turtle.left(90)
turtle.circle(-8, 200)

turtle.penup()
turtle.goto(45, 15)
turtle.pendown()

turtle.left(90)
turtle.circle(-8, 190)


turtle.done()
