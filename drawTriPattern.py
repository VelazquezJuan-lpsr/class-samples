import turtle

def drawTriangle(myTurtle):
        count = 0
        while count < 3:
                myTurtle.forward(10)
                myTurtle.left(120)
                count = count + 1

def drawMoreTriangles(myTurtle):
        count = 0
        while count < 4:
                myTurtle.penup()
                myTurtle.forward(10)
                myTurtle.pendown()
                drawTriangle(myTurtle)
count = count + 1

def drawTriAlligned(myTurtle):
        count = 0
        while count < 3:
                drawMoreTriangles(myTurtle)
                myTurtle.penup()
                myTurtle.goto(0,0)
                myTurtle.pendown()
count = count + 1
 myTurtle.penup()
        myTurtle.goto(0,0)
        myTurtle.pendown()
        myTurtle.left(260)
        number = 0
        while number < 3:
                drawMoreTriangles(myTurtle)
                myTurtle.penup()
                myTurtle.goto(0,0)
                number = number + 1

shawn = turtle.Turtle()

drawTriAlligned(shawn)

turtle.exitonclick()
