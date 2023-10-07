from turtle import *

speed(60)

# Grass

bgcolor("Green")

# SKY
penup()
goto(-400, -100)
pendown()
color("DeepSkyBlue")
begin_fill()


for i in range(2):
    forward(800)
    left(90)
    forward(500)
    left(90)
end_fill()

#sun
penup()
goto(-320,225)
pendown()
color("Yellow")
begin_fill()
circle(35)
end_fill()

# clouds
penup()
goto(200,200)
pendown()
color("White")
begin_fill()
circle(25)
end_fill()

penup()
goto(220, 240)
pendown()
color("White")
begin_fill()
circle(25)
end_fill()

penup()
goto(215, 195)
pendown()
begin_fill()
circle(28)
end_fill()

# House
penup()
goto(-100, -100)
pendown()
pensize(3)
color("chocolate", "Orange")  # (stroke, fill)
begin_fill()
for i in range(4):
    forward(170)
    left(90)
end_fill()

# chimney
penup()
goto(20, 130)
pendown()
color("brown", "firebrick")
begin_fill()

for i in range(2):
    forward(40)
    left(90)
    forward(100)
    left(90)
end_fill()

# Roof
penup()
goto(-127, 70)
pendown()
begin_fill()

for i in range(3):
    forward(225)
    left(120)
end_fill()

# Window 1
penup()
goto(0, 0)
pendown()
color("black", "White")
begin_fill()

for i in range(4):
    forward(50)
    left(90)
end_fill()

# Window cross  # My Way
penup()
goto(0, 25)
pendown()
color("black")
forward(50)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(50)



# Window 2
penup()
goto(-80, 50)
pendown()
# right(90)  # <-new line
color("black", "White")
begin_fill()

for i in range(4):
    forward(50)
    left(90)
end_fill()

# Tutorial way
# cross 2  -horizontal line
penup()
goto(-55, 50)

pendown()
color("black")
forward(50)

# cross 2  -vertical line
penup()
goto(-80, 25)
pendown()
left(90)    # <-new line
# color("black")
forward(50)

# Door
penup()
goto(-50, -25)
pendown()
right(90)
color("darkred", "red")
begin_fill()

for i in range(2):
    forward(80)
    left(90)
    forward(50)
    left(90)
end_fill()

# Door Handle
penup()
goto(-15, -65)
pendown()
color("black")
begin_fill()
circle(5)
end_fill()













hideturtle()
exitonclick()

done()








