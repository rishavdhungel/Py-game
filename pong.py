import turtle
import os

window = turtle.Screen()
window.title("Pong by Rishav")
window.bgcolor("green")
window.setup(width=800, height=600)
window.tracer(0)

#adding paddle left
paddleLeft = turtle.Turtle()
paddleLeft.speed(0)
paddleLeft.shape("square")
paddleLeft.color("red")
paddleLeft.shapesize(stretch_wid=5,stretch_len=1)
paddleLeft.penup()
paddleLeft.goto(-350,0)

#adding paddle right
paddleRight = turtle.Turtle()
paddleRight.speed(0)
paddleRight.shape("square")
paddleRight.color("red")
paddleRight.shapesize(stretch_wid=5,stretch_len=1)
paddleRight.penup()
paddleRight.goto(350,0)

#adding ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx = 0.04
ball.dy = -0.04


#gamecontrol left
def paddleLeftUp():
    y = paddleLeft.ycor()
    y += 20
    paddleLeft.sety(y)

def paddleLeftDown():
    y = paddleLeft.ycor()
    y -=20
    paddleLeft.sety(y)

#gamecontrol right
def paddleRightUp():
    y = paddleRight.ycor()
    y += 20
    paddleRight.sety(y)

def paddleRightDown():
    y = paddleRight.ycor()
    y -=20
    paddleRight.sety(y)

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 | Player B: 0", align="center", font=("Courier", 24, "normal"))

#score
scoreLeft = 0
scoreRight = 0



#keyboard mapping
window.listen()
#left paddle
window.onkeypress(paddleLeftUp,"w")
window.onkey(paddleLeftDown,"s")

#right paddle
window.onkeypress(paddleRightUp,"Up")
window.onkey(paddleRightDown,"Down")




#Main Game loop
while True:
    window.update()
    #ball movement
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #paddle border check
    if paddleLeft.ycor() >= 270:
        paddleLeft.sety(250)
    if paddleRight.ycor() >= 270:
        paddleRight.sety(250)

    if paddleLeft.ycor() <= -270:
        paddleLeft.sety(-250)
    if paddleRight.ycor() <= -270:
        paddleRight.sety(-250)



    #border check
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        scoreLeft += 1
        os.system('afplay /bounce.mp3&')
        pen.clear()
        pen.write("Player A: {} | Player B:{}".format(scoreLeft,scoreRight), align="center", font=("Courier", 24, "normal"))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *= -1
        scoreRight += 1
        os.system('afplay /bounce.mp3&')
        pen.clear()
        pen.write("Player A: {} | Player B:{}".format(scoreLeft,scoreRight), align="center", font=("Courier", 24, "normal"))

#paddle and ball collisions

    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()< paddleRight.ycor()+40 and ball.ycor()> paddleRight.ycor()-40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()< paddleLeft.ycor()+40 and ball.ycor()> paddleLeft.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1