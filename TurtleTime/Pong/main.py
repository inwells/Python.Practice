from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_pad = Paddle((350, 0))
l_pad = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(l_pad.go_up, "w")
screen.onkey(l_pad.go_down, "s")
screen.update()
screen.tracer(8, 1)

game_on = True
while game_on:
    
    ball.move()

    #Wall Collision
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce("wall")
    
    #Left Paddle Collision
    if ball.distance(l_pad) < 50 and ball.xcor() < -340:
        ball.bounce("paddle")
    
    #Right Paddle Collision
    if ball.distance(r_pad) < 50 and ball.xcor() > 340:
        ball.bounce("paddle")

    #Left Paddle Miss
    if ball.xcor() > 380:
        ball.reset_pos()
    
    if ball.xcor() < -380:
        ball.reset_pos()


screen.exitonclick()