import math
import turtle as t
import time


def shape_shell(edge=100,sides=3):
    angle = 360/sides
    t.rt(angle)
    t.fd(edge)
    for i in range(sides-1):
        t.lt(angle)
        t.fd(edge)


def triangle(edge=100):
    t.fd(edge)
    t.rt(120)
    t.fd(edge)
    t.rt(120)
    t.fd(edge)
    t.rt(120)
    t.fd(edge)
    t.rt(120)


def rectangle(edge=100):
    for i in range(4):
        t.rt(90)
        t.fd(edge)


def straight_line(edge=100, angle=0):
    t.home()
    t.lt(angle)
    t.fd(edge)
    t.home()
    t.lt(angle)
    t.bk(edge)


def star_hex(edge=100):

    straight_line(100,60)
    straight_line(100,120)
    straight_line(100,0)
    shape_shell(100, 6)


def mouse_face():
    t.hideturtle()
    t.color('Black', '#6e5f57')
    t.begin_fill()
    rectangle(100)
    t.end_fill()
    t.color('Black', '#6e5f57')
    t.begin_fill()
    t.circle(25)
    t.end_fill()
    t.color('Black', '#DCDCDC')
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.bk(100)
    t.color('Black', '#6e5f57')
    t.begin_fill()
    t.circle(25)
    t.end_fill()
    t.color('Black', '#DCDCDC')
    t.begin_fill()
    t.circle(15)
    t.end_fill()

    #draw L eye
    t.penup()
    t.setpos(-75, -35)
    t.pendown()
    t.color('Black', 'White')
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.penup()
    t.setpos(-75, -30)
    t.pendown()
    t.color('Black', '#E2DFD2')
    t.begin_fill()
    t.circle(3)
    t.end_fill()

    # #draw R eye
    t.penup()
    t.setpos(-25, -35)
    t.pendown()
    t.color('Black', 'White')
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.penup()
    t.setpos(-25, -30)
    t.pendown()
    t.color('Black', '#E2DFD2')
    t.begin_fill()
    t.circle(3)
    t.end_fill()

    #draw nose
    t.penup()
    t.setpos(-50,-50)
    t.pendown()
    t.color('Black', 'Red')
    t.begin_fill()
    shape_shell(15,3)
    t.end_fill()

    #draw mouth
    t.penup()
    t.setpos(-15, -55)
    t.pendown()
    t.rt(210)
    t.circle(-33,180)

    time.sleep(10000)



mouse_face()

