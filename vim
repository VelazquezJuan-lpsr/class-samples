import turtle

buzz = turtle.Turtle()
buzz.color("blue")
lines = 0

while lines < 24:
	buzz.left(15)
	buzz.forward(30)
	lines = lines + 1
turtle.exitonclick()

