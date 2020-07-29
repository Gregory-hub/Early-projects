from tkinter import *
from random import *

color = "gray"


def clicked1():
	
	btn1['text'] = bombs[0]


def clicked2():
	btn2['text'] = bombs[1]


def clicked3():
	btn3['text'] = bombs[2]


def clicked4():
	btn4['text'] = bombs[3]


def clicked5():
	btn5['text'] = bombs[4]


def clicked6():
	btn6['text'] = bombs[5]


def clicked7():
	btn7['text'] = bombs[6]


def clicked8():
	btn8['text'] = bombs[7]


def clicked9():
	btn9['text'] = bombs[8]


def clicked10():
	btn10['text'] = bombs[9]


def clicked11():
	btn11['text'] = bombs[10]


def clicked12():
	btn12['text'] = bombs[11]


def clicked13():
	btn13['text'] = bombs[12]


def clicked14():
	btn14['text'] = bombs[13]


def clicked15():
	btn15['text'] = bombs[14]


def clicked16():
	btn16['text'] = bombs[15]


# generates array of bombs with indexes of bombs
bombs = []
for k in range(0, 16):
	bombs.append(0)
number_of_bombs = 5
b = 0
while b < number_of_bombs:
	i = randint(0, len(bombs) - 1)
	if bombs[i] == 0:
		bombs.pop(i)
		bombs.insert(i, 1)
		b += 1
print(bombs)

root = Tk()
root.title("Sapper")

btn1 = Button(root, width = 3, command = clicked1)
btn2 = Button(root, width = 3, command = clicked2)
btn3 = Button(root, width = 3, command = clicked3)
btn4 = Button(root, width = 3, command = clicked4)
btn5 = Button(root, width = 3, command = clicked5)
btn6 = Button(root, width = 3, command = clicked6)
btn7 = Button(root, width = 3,command = clicked7)
btn8 = Button(root, width = 3, command = clicked8)
btn9 = Button(root, width = 3, command = clicked9)
btn10 = Button(root, width = 3, command = clicked10)
btn11 = Button(root, width = 3, command = clicked11)
btn12 = Button(root, width = 3, command = clicked12)
btn13 = Button(root, width = 3, command = clicked13)
btn14 = Button(root, width = 3, command = clicked14)
btn15 = Button(root, width = 3, command = clicked15)
btn16 = Button(root, width = 3, command = clicked16)

btn1.grid(row = 0, column = 0)
btn2.grid(row = 0, column = 1)
btn3.grid(row = 0, column = 2)
btn4.grid(row = 0, column = 3)
btn5.grid(row = 1, column = 0)
btn6.grid(row = 1, column = 1)
btn7.grid(row = 1, column = 2)
btn8.grid(row = 1, column = 3)
btn9.grid(row = 2, column = 0)
btn10.grid(row = 2, column = 1)
btn11.grid(row = 2, column = 2)
btn12.grid(row = 2, column = 3)
btn13.grid(row = 3, column = 0)
btn14.grid(row = 3, column = 1)
btn15.grid(row = 3, column = 2)
btn16.grid(row = 3, column = 3)

root.mainloop()