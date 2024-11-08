from pickle import TRUE
import turtle
#setting up the window
win = turtle.Screen()
win.title("Pong for idiots")
win.bgcolor("black")
win.setup(width=600, height=500)
win.tracer(0)

#left paddle
lpad = turtle.Turtle()
lpad.speed(0)
lpad.shape("square")
lpad.color("white")
lpad.shapesize(stretch_len=1, stretch_wid=3)
lpad.penup()  #this wont create a line as the object moves
lpad.goto(-290, 0)

#right paddle
rpad = turtle.Turtle()
rpad.speed(0)
rpad.shape("square")
rpad.color("white")
rpad.shapesize(stretch_len=1, stretch_wid=3)
rpad.penup()  #this wont create a line as the object moves
rpad.goto(280, 0) 

#scoreboard
score = turtle.Turtle()
score.speed(0)
score.penup()
score.color("white")
score.hideturtle()
score.goto(0, 220)
score.write("Left:0  Right: 0 ", align= "center", font=("arial", 15 ))
#score
lscore = 0
rscore = 0

#the ball
ball = turtle.Turtle()
ball.speed(2)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
#speed of the ball
ball.dx = 0.2 #the ball wil move along the x axis with 0.5 speed
ball.dy = 0.2 #the ball wil move along the y axis with 0.5 speed, 2 was too fast
speed_increment = 0.05

#functions
def lpadup():
    y = lpad.ycor()
    y += 20
    lpad.sety(y)

def lpaddo():
    y = lpad.ycor()
    y -= 20
    lpad.sety(y)

def rpadup():
    y = rpad.ycor()
    y += 20
    rpad.sety(y)

def rpaddo():
    y = rpad.ycor()
    y -= 20
    rpad.sety(y)

#key bindings
win.listen()
win.onkeypress(lpadup, "w")
win.onkeypress(lpaddo, "s")
win.onkeypress(rpadup, "Up")
win.onkeypress(rpaddo, "Down")


def close_window():
    global running
    running = False  # Stop the game loop
    win.bye()

win.onkeypress(close_window, "q")  # Press 'q' to quit
win.listen()

#game loop
running = True   #q will change this to false
while running:
    try:
        win.update()

        #moving the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        #border checking the ball
        if ball.ycor() > 240:
            ball.sety(240)
            ball.dy *= -1  #top

        if ball.ycor() < -230:
            ball.sety(-230)
            ball.dy *= -1  #bottom
        
        #when it goes out of bounds
        if ball.xcor() > 290:
            ball.goto(0, 0) 
            ball.dx *= -1  
            lscore += 1
            score.clear()
            score.write("Left: {} Right: {} ".format(lscore, rscore), align= "center", font=("arial", 15 ))
            #speed buff
            if lscore % 5 == 0:
                ball.dx += speed_increment if ball.dx > 0 else -speed_increment
                ball.dy += speed_increment if ball.dy > 0 else -speed_increment

        if ball.xcor() <  -290:
            ball.goto(0, 0)
            ball.dx *= -1
            rscore += 1
            score.clear()
            score.write("Left: {} Right: {} ".format(lscore, rscore), align= "center", font=("arial", 15 ))
            if rscore % 5 == 0:
                ball.dx += speed_increment if ball.dx > 0 else -speed_increment
                ball.dy += speed_increment if ball.dy > 0 else -speed_increment


        #when it hits the pad
        if (ball.xcor() > 260 and ball.xcor() < 290) and (ball.ycor() < rpad.ycor() + 40 and ball.ycor() > rpad.ycor() - 40):
            ball.setx(260)
            ball.dx *= -1

        if (ball.xcor() < -270 and ball.xcor() > -290) and (ball.ycor() < lpad.ycor() + 40 and ball.ycor() > lpad.ycor() - 40):
            ball.setx(-270)
            ball.dx *= -1
    except turtle.Terminator:
        break
    




