from turtle import *

# speed(0)


# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# 1. Red Square   1, 1
penup()
goto(5,5)
pendown()
color("Magenta")
begin_fill()
for i in range(4):
    forward(200)
    left(90)
end_fill()

# 2. Yellow Square  -1, -1
penup()
goto(5, -5)
pendown()
color("DeepSkyBlue")
begin_fill()
for i in range(4):
    forward(160)
    right(90)
end_fill()

# 3. Green square -1, 1
penup()
goto(-5, 5)
pendown()
color("PeachPuff")
begin_fill()

for i in range(4):
    left(90)
    forward(140)
end_fill()


# 3. Blue square -1, -1
penup()
goto(-5 , -5)
pendown()
color("DarkGray")
begin_fill()

for i in range(4):
    right(90)
    forward(210)
end_fill()


# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# 1. Red Square   1, 1
penup()
goto(15,37)
pendown()
color("cyan")
begin_fill()
for i in range(4):
    forward(90)
    left(90)
end_fill()

# 2. Yellow Square  -1, -1
penup()
goto(54, -87)
pendown()
color("MistyRose")
begin_fill()
for i in range(4):
    forward(96)
    right(90)
end_fill()

# 3. Green square -1, 1
penup()
goto(-22, 45)
pendown()
color("Aquamarine")
begin_fill()

for i in range(4):
    left(90)
    forward(84)


for i in range(2):
    left(115)
    forward(60)

end_fill()


# 3. Blue square -1, -1
penup()
goto(-3 , -19)
pendown()
color("Violet")
begin_fill()

for i in range(2):
    right(90)
    forward(105)


for i in range(2):
    right(90)
    forward(75)

end_fill()










# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# 1. Red Square   1, 1
penup()
goto(5, 5)
pendown()
color("red")
begin_fill()
for i in range(4):
    forward(80)
    left(90)
end_fill()

# 2. Yellow Square  1, -1
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
goto(5, 5)
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
goto(-5, -5)
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


bgcolor("Skyblue")



























done()  # End

