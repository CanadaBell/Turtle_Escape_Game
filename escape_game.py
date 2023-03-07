#Imports
import random
import turtle
#Turtles/Variables/Functions
ref = turtle.Turtle() # Sets up the court and prints the winner 
t1 = turtle.Turtle() # First turtle
t2 = turtle.Turtle() # Second Turtle
w = 980 #Width of screen (Change if you want)
h = 810 #Height of screen (Change if you want)
t = 0 #Times
def go(p,rx,ry): #Function for lifting up the pen and going to a location
    p.up()
    p.goto(rx, ry)
    p.down()
def text(p,w,m): #Funtion to write who wins at the end
    ref.color(p)
    go(ref,0,320)
    ref.write(f'Winner: {w} | Time: {m} Seconds', False, align='center', font=('Comic Sans MS', 30, 'normal'))
#Screen
s = turtle.Screen() #Creates screen
s.setup (w,h) #Makes the screen the width and height (Change the wariables if you want the w and h to change)
#Ref settings
ref.hideturtle()        # \
ref.color('black')      #  \
ref.fillcolor('orange') #   > Settings that change the ref 
ref.pensize(5)          #  /
ref.speed(6)            # /
#Drawing the court
go(ref, w/2.5, 0) # Teleports ref to make 1 edge
ref.begin_fill()
ref.lt(90)
for _ in range (2): #Makes the court
    ref.fd(h/2.5)
    ref.lt(90)
    ref.fd((w/2.5) * 2)
    ref.lt(90)
    ref.fd(h/2.5)
ref.end_fill()
ref.color('white')  #  Makes the white line and circle 
go(ref, 0, h/2.5)   #  
ref.lt(180)         #   
ref.fd((h/2.5) * 2) #    
go(ref, -75,0)      #  
ref.circle(75)      # 
#Setting up the 2 turtles
t1n = s.textinput('Turtle 1 Name', 'Type the name of turtle 1:') 
t1c = s.textinput('Turtle 1 Color', 'Type the hex code of the color of turtle 1:')
go(t1,-196,0)
if t1c is None or t1c == '':
    t1c = 'red'
t1.color(t1c)
t2n = s.textinput('Turtle 2 Name', 'Type the name of turtle 2:')
t2c = s.textinput('Turtle 2 Color', 'Type the hex code of the color of turtle 2:')
go(t2,196,0)
t2.left(180)
if t2c is None or t2c == '':
    t2c = 'blue'
t2.color(t2c)
show = s.textinput('Show','Do you want the pen lines to be shown?')
if show is None or show == '' or show.lower().startswith('y'):
    t1.down(),t2.down()
elif show.lower().startswith('n'):
    t1.up(),t2.up()
else:
    s.bye()
    print ('Closed window and calling 911, as you are having a stroke')
#Random movements
while True:
    t1.fd(50)
    t2.fd(50)
    turn = random.randint (1,7)
    turn2 = random.randint (1,7)
    t1.lt(60 * turn)
    t2.rt(60 * turn2)
    x,y = t1.pos()
    x2,y2 = t2.pos()
    if x >= 392 or x <= -392 or y >= 324 or y <= -324:
        text(t2c,t2n,t) 
        break
    if x2 >= 392 or x2 <= -392 or y2 >= 324 or y2 <= -324:
        text(t1c,t1n,t)
        break
    t += 1
#Output
s.exitonclick()
