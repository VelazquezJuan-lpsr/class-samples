import turtle

def makeSquare(myTurtle,side):
	myTurtle.forward(side)
	myTurtle.left(90)
	myTurtle.forward(side)
	myTurtle.left(90)
	myTurtle.forward(side)
	myTurtle.left(90)
	myTurtle.forward(side)
	myTurtle.left(90)
def makeTriangle(myturtle,side):
	myturtle.forward(side)
	myturtle.left(120)
	myturtle.forward(side)
        myturtle.left(120)
	myturtle.forward(side)
        myturtle.left(120)
soso = turtle.Turtle()
rara = turtle.Turtle()
rara.forward(150)
soso.color("red")
rara.color("blue")
length = 50
while length > 0:
	makeSquare(soso, length)
	soso.right(30)
	makeTriangle(rara, length)
	rara.right(30)
	length = length - 1
