import turtle


def kochOneSide(myTurtle, level, size):
    if level == 0:
        myTurtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            kochOneSide(myTurtle, level - 1, size / 3)
            myTurtle.left(angle)

def kochSnowFlake(level, size=300):

    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.setup(600, 600)

    myTurtle = turtle.Turtle()
    myTurtle.speed(0)
    myTurtle.penup()
    myTurtle.goto(-size / 2, 0)
    myTurtle.pendown()
    myTurtle.pencolor("green")

    for _ in range(3):
        kochOneSide(myTurtle, level, size)
        myTurtle.right(120)

    wn.mainloop()


try:
    level = int(input("Enter Koch Snowflake level: "))
    kochSnowFlake(level)
except ValueError:
    print('Enter positive number!')
