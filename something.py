#Imports
import random
import turtle
#Turtles/Variables
ref = turtle.Turtle()
t1 = turtle.Turtle()
t2 = turtle.Turtle()
w = 980
h = 810
#Questions


#Screen
s = turtle.Screen()
s.setup (w,h)
#Ref Settings
ref.hideturtle()
ref.color('gray')
ref.pensize(5)
ref.speed(6)
#Drawing the court
ref.up()
ref.goto(w/2.5, 0)
ref.down()
ref.lt(90)
for _ in range (2):
    ref.fd(h/2.5)
    ref.lt(90)
    ref.fd((w/2.5) * 2)
    ref.lt(90)
    ref.fd(h/2.5)
ref.up()
ref.goto(0, h/2.5)
ref.down()
ref.lt(180)
ref.fd((h/2.5) * 2)
ref.up()
ref.goto(-75, 0)
ref.down()
ref.circle(75)
#Placing the turtles
t1.up()
t2.up()
t1.goto(-196,0)
t2.goto(196,0)
t2.left(180)
t1.down()
t2.down()
while True:
    t1.fd(50)
    t2.fd(50)
    turn = random.randint (1,7)
    turn2 = random.randint (1,7)
    t1.lt(60 * turn)
    t2.rt(60 * turn2)
    x,y = t1.pos()
    x2,y2 = t2.pos()
    if x >= 460 or x <= -460 or y >= 405 or y <= -405:
        break
    if x2 >= 460 or x2 <= -460 or y2 >= 405 or y2 <= -405:
        break
#Output
s.exitonclick()
