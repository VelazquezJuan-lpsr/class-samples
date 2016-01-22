import turtle

def drawRedSquare(myTurtle):
        myTurtle.color("red")
        count = 0
        while count < 4:
                myTurtle.forward(20)
                myTurtle.left(90)
                count = count + 1

def drawBlueSquare(myTurtle):
        myTurtle.color("blue")
        myTurtle.penup()
        myTurtle.forward(20)
        myTurtle.pendown()
        count = 0
        while count < 4:
                myTurtle.forward(20)
                myTurtle.left(90)
                count = count + 1

def drawGreenSquare(myTurtle):
        myTurtle.color("green")
        myTurtle.penup()
        myTurtle.forward(20)
	myTurtle.left(90)
        myTurtle.forward(20)
        myTurtle.pendown()
        count = 0
        while count < 4:
                myTurtle.forward(20)
                myTurtle.right(90)
                count = count + 1

def drawYellowSquare(myTurtle):
        myTurtle.color("yellow")
        myTurtle.penup()
        myTurtle.forward(20)
        myTurtle.left(90)
        myTurtle.pendown()
        count = 0
        while count < 4:
                myTurtle.forward(20)
                myTurtle.left(90)
                count = count + 1

def drawAllSquares(myTurtle):
        drawRedSquare(myTurtle)
        drawBlueSquare(myTurtle)
        drawGreenSquare(myTurtle)
        drawYellowSquare(myTurtle)
def drawSquarePattern(myTurtle):
        count = 0
        while count < 5:
                drawAllSquares(shawn)
                myTurtle.left(90)
                myTurtle.penup()
                myTurtle.forward(5)
                myTurtle.left(90)
                myTurtle.pendown()
                count = count + 1

shawn = turtle.Turtle()

drawSquarePattern(shawn)

turtle.exitonclick()
