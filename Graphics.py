from graphics import *
from time import *


def draw_eye(pt, r, win):
	eye = Circle(pt, r)
	eye.setFill("black")
	eye.draw(win) 


def draw_snowman_circle(pt, r, win):
	cir = Circle(pt, r)	
	cir.setFill(color_rgb(255, 255, 255))
	cir.setOutline(color_rgb(255, 255, 255))
	cir.setWidth(5)
	cir.draw(win)


def draw_snowman(x, y, r, win):
	draw_snowman_circle(Point(x, y-r*1.66), int(r*0.66), win)
	draw_snowman_circle(Point(x, y), r, win)
	draw_snowman_circle(Point(x, y+2.66*r), int(r*1.66), win)

	draw_eye(Point(x-r*0.30, y - r*1.74), r/6, win)
	draw_eye(Point(x+r*0.30, y - r*1.74), r/6, win)


def draw_snowflake(x, y, r, win):
	X = [r, -0.707*r, 0, 0.707*r]
	Y = [0, 0.707*r, r, 0.707*r]
	for (st_x, st_y) in (X[0], Y[0]), (X[1], Y[1]), (X[2], Y[2]), (X[3], Y[3]):
		ln = Line(Point(x - st_x, y + st_y), Point(x + st_x, y - st_y))
		ln.setFill('white')
		ln.draw(win)


win = GraphWin("First window", 500, 500)
win.setBackground("black")

draw_snowman(100, 25, 10, win)
draw_snowman(350, 300, 30, win)
draw_snowman(250, 150, 20, win)
draw_snowman(50, 400, 5, win)
draw_snowman(150, 250, 40, win)

sleep(0.3)
draw_snowflake(50, 50, 6, win)
sleep(0.3)
draw_snowflake(20, 10, 6, win)
sleep(0.3)
draw_snowflake(70, 150, 6, win)
sleep(0.3)
draw_snowflake(90, 350, 5, win)
sleep(0.3)
draw_snowflake(350, 130, 4, win)
sleep(0.3)
draw_snowflake(340, 80, 4, win)
sleep(0.3)
draw_snowflake(420, 60, 5, win)
sleep(0.3)
draw_snowflake(390, 10, 4, win)
sleep(0.3)
draw_snowflake(225, 470, 4, win)
sleep(0.3)
draw_snowflake(270, 20, 3, win)
sleep(0.3)
draw_snowflake(280, 350, 3, win)

win.getMouse()	