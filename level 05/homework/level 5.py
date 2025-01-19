from turtle import *

speed(100)
width(2)

#drawing a rectang
right(90)
forward(200)
right(90)
forward(250)
right(90)
forward(200)
right(90)
forward(250)

#end rectang

#next  rectang (biger than this rectang)

left(90)
forward(90)
right(90)
forward(120)
right(90)
forward(290)
right(90)
forward(120)

#next rectang 

penup()
goto(0,  0)
pendown()
forward(250)
right(90)
forward(90)
left(90)
forward(120)
left(90)
forward(290)
left(90)
forward(120)

#end to drawing rectangs
 
#drawing roof 

penup()
goto(0, 0)
pendown()
right(180)
forward(20)
right(90)
forward(15)
left(90)
forward(25)
left(90)
forward(15)

right(90)
forward(20)
right(90)
forward(15)
left(90)
forward(25)
left(90)
forward(15)

right(90)
forward(20)
right(90)
forward(15)
left(90)
forward(25)
left(90)
forward(15)


right(90)
forward(20)
right(90)
forward(15)
left(90)
forward(25)
left(90)
forward(15)

right(90)
forward(20)
right(90)
forward(15)
left(90)
forward(25)
left(90)
forward(15)
right(90)
forward(20)

#drawing roof

penup()
goto(0, 0)
pendown()
right(90)
forward(90)
color("brown")
begin_fill()
right(30)
forward(120)
right(120)
forward(120)
end_fill()

color("black")
penup()
goto(0, 0)
pendown()
right(120)
forward(250)
right(90)
forward(90)
color("brown")
begin_fill()
left(30)
forward(120)
left(120)
forward(120)
end_fill()
#end  drawing 

#drawing a door 
color("black")
penup()
goto(0, 0)
pendown()
left(30)
forward(200)
right(90)
forward(90)
color("brown")
begin_fill()
right(90)
forward(50)
left(20)
forward(10)
left(20)
forward(10)
left(20)
forward(10)
left(20)
forward(10)
left(10)
forward(20)
left(20)
forward(10)
left(20)
forward(10)
left(20)
forward(10)
left(20)
forward(10)
left(8)
forward(47)
end_fill()
#end to drawing door

#drawing window 
penup()
goto(0, 0)
right(90)
forward(40)
left(90)
forward(40)
pendown()
color("red")
begin_fill()
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)

penup()
left(92)
forward(140)
pendown()
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()
#end  drawing


#drawing path
penup()
goto(0, 0)
right(180)
forward(200)
right(90)
forward(95)
pendown()
left(90)
color("grey")
forward(50)
right(20)
forward(20)
right(20)
forward(20)
forward(30)
left(20)
forward(20)
left(20)
forward(20)
left(20)
forward(20)
left(20)
forward(20)
right(20)
forward(20)
right(20)
forward(90)

penup()
goto(0, 0)
pendown()
color("black")
forward(200)
right(90)
forward(160)
left(90)
color("grey")

forward(50)
right(20)
forward(20)
right(20)
forward(20)
forward(30)
left(20)
forward(20)
left(20)
forward(20)
left(20)
forward(20)
left(20)
forward(20)
right(20)
forward(20)
right(20)
forward(90)
#end to drawing a path

#drawing a 2 smal window
penup()
goto(0, 0)
pendown()
color("black")
right(180)
forward(40)
penup()
right(90)
forward(50)
pendown()
color("red")
begin_fill()
left(90)
forward(20)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(20)

penup()
left(90)
forward(50)
pendown()
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
end_fill()


#drawing a next 2 smal window
penup()
goto(0, 0)
forward(250)
right(90)
forward(60)
left(90)
forward(50)
pendown()
begin_fill()
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)

penup()
right(180)
forward(70)
pendown()
forward(20)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(20)
end_fill()

#drawing flag
width(1)
color("black")
penup()
goto(0, 0)
left(90)
forward(90)
right(30)
forward(120)
pendown()
begin_fill()
left(30)
forward(110)
right(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()
#flag text (GOA)
#G
width(2.5)
color("green")
penup()
goto(80,  270)
pendown()
right(90)
forward(5)
right(90)
forward(10)
right(90)
forward(10)
right(90)
forward(20)
right(90)
forward(30)
right(90)
forward(20)

#O
penup()
forward(10)
pendown()
forward(10)
right(40)
forward(5)
right(48)
forward(25)
right(50)
forward(5)
right(40)
forward(10)
right(50)
forward(5)
right(40)
forward(25)
right(40)
forward(5)

#A
penup()
goto( 125,   265)
pendown()
left(20)
forward(35)
right(140)
forward(35)
right(180)
forward(10)
left(70)
forward(20)


exitonclick()