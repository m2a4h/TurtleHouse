from turtle import *

speed(60)
bgcolor("Skyblue")

# 1. Red Square   1, 1
penup()
goto(5,5)
pendown()
color("red")
begin_fill()
for i in range(4):
    forward(80)
    left(90)
end_fill()

# 2. Yellow Square  -1, -1
penup()
goto(5, -5)
pendown()
color("Yellow")
begin_fill()
for i in range(4):
    forward(50)
    right(90)
end_fill()

# 3. Green square -1, 1
penup()
goto(-5, 5)
pendown()
color("green")
begin_fill()

for i in range(2):
    left(90)
    forward(60)


for i in range(2):
    left(90)
    forward(60)

end_fill()


# 3. Blue square -1, -1
penup()
goto(-5 , -5)
pendown()
color("blue")
begin_fill()

for i in range(2):
    right(90)
    forward(50)


for i in range(2):
    right(90)
    forward(50)

end_fill()

# Borders Now   *First maximize the window



# Horizontally
penup()
goto(0,0)
pendown()
pensize(3)
color("Black")
forward(665)     #670 maximum

# Vertically
penup()
goto(0,0)
pendown()
pensize(3)
color("Black")
left(90)
forward(340)    # 350 maximum

# Horizontally
penup()
goto(0,0)
pendown()
pensize(3)
color("Black")
left(180)
forward(330)     #670 maximum

# Vertically
penup()
goto(0,0)
pendown()
pensize(3)
color("Black")
left(90)
backward(665)    # 350 maximum

# An upper circle
# # A Circle
# penup()
# goto(0, 0)
# pendown()
# circle(200)

# On the upper left
# # A Circle
# penup()
# goto(-330, 0)
# pendown()
# circle(200)

#  mostly  the better circle
# A Circle
penup()
goto(0, -330)
pendown()
circle(335)








done()

