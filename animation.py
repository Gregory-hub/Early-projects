from graphics import *
from time import *



def draw_snowflake(x, y, r, win):
	X = [r, -0.707*r, 0, 0.707*r]
	Y = [0, 0.707*r, r, 0.707*r]
	for (st_x, st_y) in (X[0], Y[0]), (X[1], Y[1]), (X[2], Y[2]), (X[3], Y[3]):
		ln = Line(Point(x - st_x, y + st_y), Point(x + st_x, y - st_y))
		ln.setFill('white')
		ln.draw(win)


win = GraphWin("Anemi", 500, 500)
win.setBackground(color_rgb(200, 0, 200))


x, y = 50, 50
n = 0
while n <= 400:
	ln1 = Line(Point(x + n, y), Point(x + n, 450))
	ln1.draw(win)
	
	ln2 = Line(Point(x, y + n), Point(450, y + n))
	ln2.draw(win)
	sleep(0.1)
	n += 40

for ys in range(1, 11):
	for xs in range(1, 11):
		draw_snowflake(xs*40 + 30, ys*40 + 30, 10, win)
		sleep(0.02)

win.getMouse()