import turtle
def draw_rectangle(color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for   _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_circle(color, x, y, radius):
    turtle.penup()
    turtle.goto(x,  y - radius)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_rama():
    # Draw Body
    draw_rectangle("blue", -50, 0, 100, 200) #body
    draw_rectangle("orange", -70, 200, 140, 20) #waist
    draw_rectangle("orange", -90, 220, 180, 20) #chest
    # Draw Head
    draw_circle("blue", 0, 260, 30)  #head
    draw_circle("black", 0, 260, 10) #eyes
    #Draw bow
    turtle.penup()
    turtle.goto(-50, 150)
    turtle.pendown()
    turtle.setheading(90)
    turtle.pensize(5)
    turtle.circle(50, 180)  #Draw Bow
    turtle.pensize(1)
    #Draw Arrows
    turtle.penup()
    turtle.goto(0, 150)
    turtle.pendown()
    turtle.goto(50, 150)#Arrow line
    turtle.goto(50, 145)#Arrow tip
    turtle.goto(50, 155)#Arrow tip
    turtle.goto(20, 150) #back to center
#Setup turtle
turtle.speed(3)
turtle.bgcolor("white")
# draw lord rama
draw_rama()
#finish
turtle.hideturtle()
turtle.done()