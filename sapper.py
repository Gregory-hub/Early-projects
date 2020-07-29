from tkinter import *
from random import randint
from math import sqrt, floor

number_of_bombs = 20
number_of_buttons = 49

bombs = []
for k in range(0, int(sqrt(number_of_buttons))):
	local_bombs = []
	for i in range(int(sqrt(number_of_buttons))):
		local_bombs.append(0)
	bombs.append(local_bombs)
b = 0
while b < number_of_bombs:
	i = randint(0, len(bombs[0]) - 1)
	j = randint(0, len(bombs[0]) - 1)
	if bombs[i][j] == 0:
		bombs[i][j] = 1
		b += 1
print(bombs)


def clicked0():
	if bombs[0][0] == 0:
		btn0['bg'] = "gray"
		if bombs_around(0) > 0:
			btn0['text'] = bombs_around(0)
	else:
		btn0['bg'] = "red"

def clicked1():
	if bombs[0][1] == 0:
		btn1['bg'] = "gray"
		if bombs_around(1) > 0:
			btn1['text'] = bombs_around(1)
	else:
		btn1['bg'] = "red"

def clicked2():
	if bombs[0][2] == 0:
		btn2['bg'] = "gray"
		if bombs_around(2) > 0:
			btn2['text'] = bombs_around(2)
	else:
		btn2['bg'] = "red"

def clicked3():
	if bombs[0][3] == 0:
		btn3['bg'] = "gray"
		if bombs_around(3) > 0:
			btn3['text'] = bombs_around(3)
	else:
		btn3['bg'] = "red"

def clicked4():
	if bombs[0][4] == 0:
		btn4['bg'] = "gray"
		if bombs_around(4) > 0:
			btn4['text'] = bombs_around(4)
	else:
		btn4['bg'] = "red"

def clicked5():
	if bombs[0][5] == 0:
		btn5['bg'] = "gray"
		if bombs_around(5) > 0:
			btn5['text'] = bombs_around(5)
	else:
		btn5['bg'] = "red"

def clicked6():
	if bombs[0][6] == 0:
		btn6['bg'] = "gray"
		if bombs_around(6) > 0:
			btn6['text'] = bombs_around(6)
	else:
		btn6['bg'] = "red"

def clicked7():
	if bombs[1][0] == 0:
		btn7['bg'] = "gray"
		if bombs_around(7) > 0:
			btn7['text'] = bombs_around(7)
	else:
		btn7['bg'] = "red"

def clicked8():
	if bombs[1][1] == 0:
		btn8['bg'] = "gray"
		if bombs_around(8) > 0:
			btn8['text'] = bombs_around(8)
	else:
		btn8['bg'] = "red"

def clicked9():
	if bombs[1][2] == 0:
		btn9['bg'] = "gray"
		if bombs_around(9) > 0:
			btn9['text'] = bombs_around(9)
	else:
		btn9['bg'] = "red"

def clicked10():
	if bombs[1][3] == 0:
		btn10['bg'] = "gray"
		if bombs_around(10) > 0:
			btn10['text'] = bombs_around(10)
	else:
		btn10['bg'] = "red"

def clicked11():
	if bombs[1][4] == 0:
		btn11['bg'] = "gray"
		if bombs_around(11) > 0:
			btn11['text'] = bombs_around(11)
	else:
		btn11['bg'] = "red"

def clicked12():
	if bombs[1][5] == 0:
		btn12['bg'] = "gray"
		if bombs_around(12) > 0:
			btn12['text'] = bombs_around(12)
	else:
		btn12['bg'] = "red"

def clicked13():
	if bombs[1][6] == 0:
		btn13['bg'] = "gray"
		if bombs_around(13) > 0:
			btn13['text'] = bombs_around(13)
	else:
		btn13['bg'] = "red"

def clicked14():
	if bombs[2][0] == 0:
		btn14['bg'] = "gray"
		if bombs_around(14) > 0:
			btn14['text'] = bombs_around(14)
	else:
		btn14['bg'] = "red"

def clicked15():
	if bombs[2][1] == 0:
		btn15['bg'] = "gray"
		if bombs_around(15) > 0:
			btn15['text'] = bombs_around(15)
	else:
		btn15['bg'] = "red"

def clicked16():
	if bombs[2][2] == 0:
		btn16['bg'] = "gray"
		if bombs_around(16) > 0:
			btn16['text'] = bombs_around(16)
	else:
		btn16['bg'] = "red"

def clicked17():
	if bombs[2][3] == 0:
		btn17['bg'] = "gray"
		if bombs_around(17) > 0:
			btn17['text'] = bombs_around(17)
	else:
		btn17['bg'] = "red"

def clicked18():
	if bombs[2][4] == 0:
		btn18['bg'] = "gray"
		if bombs_around(18) > 0:
			btn18['text'] = bombs_around(18)
	else:
		btn18['bg'] = "red"

def clicked19():
	if bombs[2][5] == 0:
		btn19['bg'] = "gray"
		if bombs_around(19) > 0:
			btn19['text'] = bombs_around(19)
	else:
		btn19['bg'] = "red"

def clicked20():
	if bombs[2][6] == 0:
		btn20['bg'] = "gray"
		if bombs_around(20) > 0:
			btn20['text'] = bombs_around(20)
	else:
		btn20['bg'] = "red"

def clicked21():
	if bombs[3][0] == 0:
		btn21['bg'] = "gray"
		if bombs_around(21) > 0:
			btn21['text'] = bombs_around(21)
	else:
		btn21['bg'] = "red"

def clicked22():
	if bombs[3][1] == 0:
		btn22['bg'] = "gray"
		if bombs_around(22) > 0:
			btn22['text'] = bombs_around(22)
	else:
		btn22['bg'] = "red"

def clicked23():
	if bombs[3][2] == 0:
		btn23['bg'] = "gray"
		if bombs_around(23) > 0:
			btn23['text'] = bombs_around(23)
	else:
		btn23['bg'] = "red"

def clicked24():
	if bombs[3][3] == 0:
		btn24['bg'] = "gray"
		if bombs_around(24) > 0:
			btn24['text'] = bombs_around(24)
	else:
		btn24['bg'] = "red"

def clicked25():
	if bombs[3][4] == 0:
		btn25['bg'] = "gray"
		if bombs_around(25) > 0:
			btn25['text'] = bombs_around(25)
	else:
		btn25['bg'] = "red"

def clicked26():
	if bombs[3][5] == 0:
		btn26['bg'] = "gray"
		if bombs_around(26) > 0:
			btn26['text'] = bombs_around(26)
	else:
		btn26['bg'] = "red"

def clicked27():
	if bombs[3][6] == 0:
		btn27['bg'] = "gray"
		if bombs_around(27) > 0:
			btn27['text'] = bombs_around(27)
	else:
		btn27['bg'] = "red"

def clicked28():
	if bombs[4][0] == 0:
		btn28['bg'] = "gray"
		if bombs_around(28) > 0:
			btn28['text'] = bombs_around(28)
	else:
		btn28['bg'] = "red"

def clicked29():
	if bombs[4][1] == 0:
		btn29['bg'] = "gray"
		if bombs_around(29) > 0:
			btn29['text'] = bombs_around(29)
	else:
		btn29['bg'] = "red"

def clicked30():
	if bombs[4][2] == 0:
		btn30['bg'] = "gray"
		if bombs_around(30) > 0:
			btn30['text'] = bombs_around(30)
	else:
		btn30['bg'] = "red"

def clicked31():
	if bombs[4][3] == 0:
		btn31['bg'] = "gray"
		if bombs_around(31) > 0:
			btn31['text'] = bombs_around(31)
	else:
		btn31['bg'] = "red"

def clicked32():
	if bombs[4][4] == 0:
		btn32['bg'] = "gray"
		if bombs_around(32) > 0:
			btn32['text'] = bombs_around(32)
	else:
		btn32['bg'] = "red"

def clicked33():
	if bombs[4][5] == 0:
		btn33['bg'] = "gray"
		if bombs_around(33) > 0:
			btn33['text'] = bombs_around(33)
	else:
		btn33['bg'] = "red"

def clicked34():
	if bombs[4][6] == 0:
		btn34['bg'] = "gray"
		if bombs_around(34) > 0:
			btn34['text'] = bombs_around(34)
	else:
		btn34['bg'] = "red"

def clicked35():
	if bombs[5][0] == 0:
		btn35['bg'] = "gray"
		if bombs_around(35) > 0:
			btn35['text'] = bombs_around(35)
	else:
		btn35['bg'] = "red"

def clicked36():
	if bombs[5][1] == 0:
		btn36['bg'] = "gray"
		if bombs_around(36) > 0:
			btn36['text'] = bombs_around(36)
	else:
		btn36['bg'] = "red"

def clicked37():
	if bombs[5][2] == 0:
		btn37['bg'] = "gray"
		if bombs_around(37) > 0:
			btn37['text'] = bombs_around(37)
	else:
		btn37['bg'] = "red"

def clicked38():
	if bombs[5][3] == 0:
		btn38['bg'] = "gray"
		if bombs_around(38) > 0:
			btn38['text'] = bombs_around(38)
	else:
		btn38['bg'] = "red"

def clicked39():
	if bombs[5][4] == 0:
		btn39['bg'] = "gray"
		if bombs_around(39) > 0:
			btn39['text'] = bombs_around(39)
	else:
		btn39['bg'] = "red"

def clicked40():
	if bombs[5][5] == 0:
		btn40['bg'] = "gray"
		if bombs_around(40) > 0:
			btn40['text'] = bombs_around(40)
	else:
		btn40['bg'] = "red"

def clicked41():
	if bombs[5][6] == 0:
		btn41['bg'] = "gray"
		if bombs_around(41) > 0:
			btn41['text'] = bombs_around(41)
	else:
		btn41['bg'] = "red"

def clicked42():
	if bombs[6][0] == 0:
		btn42['bg'] = "gray"
		if bombs_around(42) > 0:
			btn42['text'] = bombs_around(42)
	else:
		btn42['bg'] = "red"

def clicked43():
	if bombs[6][1] == 0:
		btn43['bg'] = "gray"
		if bombs_around(43) > 0:
			btn43['text'] = bombs_around(43)
	else:
		btn43['bg'] = "red"

def clicked44():
	if bombs[6][2] == 0:
		btn44['bg'] = "gray"
		if bombs_around(44) > 0:
			btn44['text'] = bombs_around(44)
	else:
		btn44['bg'] = "red"

def clicked45():
	if bombs[6][3] == 0:
		btn45['bg'] = "gray"
		if bombs_around(45) > 0:
			btn45['text'] = bombs_around(45)
	else:
		btn45['bg'] = "red"

def clicked46():
	if bombs[6][4] == 0:
		btn46['bg'] = "gray"
		if bombs_around(46) > 0:
			btn46['text'] = bombs_around(46)
	else:
		btn46['bg'] = "red"

def clicked47():
	if bombs[6][5] == 0:
		btn47['bg'] = "gray"
		if bombs_around(47) > 0:
			btn47['text'] = bombs_around(47)
	else:
		btn47['bg'] = "red"

def clicked48():
	if bombs[6][6] == 0:
		btn48['bg'] = "gray"
		if bombs_around(48) > 0:
			btn48['text'] = bombs_around(48)
	else:
		btn48['bg'] = "red"


def bombs_around(index): 		
	count = 0
	for y in range(-1, 2):
		for x in range(-1, 2):
			try:
				if bombs[floor(index / int(sqrt(number_of_buttons))) + y][index % int(sqrt(number_of_buttons)) + x] == 1 and floor(index / int(sqrt(number_of_buttons))) + y >= 0 and index % int(sqrt(number_of_buttons)) + x >= 0:
					count += 1
					print(x, ",", -y, ":", count)
			except IndexError:
				continue
	return count

root = Tk()
root.title = "Sapper"

btn0 = Button(root, width = 3, command = clicked0)
btn1 = Button(root, width = 3, command = clicked1)
btn2 = Button(root, width = 3, command = clicked2)
btn3 = Button(root, width = 3, command = clicked3)
btn4 = Button(root, width = 3, command = clicked4)
btn5 = Button(root, width = 3, command = clicked5)
btn6 = Button(root, width = 3, command = clicked6)
btn7 = Button(root, width = 3, command = clicked7)
btn8 = Button(root, width = 3, command = clicked8)
btn9 = Button(root, width = 3, command = clicked9)
btn10 = Button(root, width = 3, command = clicked10)
btn11 = Button(root, width = 3, command = clicked11)
btn12 = Button(root, width = 3, command = clicked12)
btn13 = Button(root, width = 3, command = clicked13)
btn14 = Button(root, width = 3, command = clicked14)
btn15 = Button(root, width = 3, command = clicked15)
btn16 = Button(root, width = 3, command = clicked16)
btn17 = Button(root, width = 3, command = clicked17)
btn18 = Button(root, width = 3, command = clicked18)
btn19 = Button(root, width = 3, command = clicked19)
btn20 = Button(root, width = 3, command = clicked20)
btn21 = Button(root, width = 3, command = clicked21)
btn22 = Button(root, width = 3, command = clicked22)
btn23 = Button(root, width = 3, command = clicked23)
btn24 = Button(root, width = 3, command = clicked24)
btn25 = Button(root, width = 3, command = clicked25)
btn26 = Button(root, width = 3, command = clicked26)
btn27 = Button(root, width = 3, command = clicked27)
btn28 = Button(root, width = 3, command = clicked28)
btn29 = Button(root, width = 3, command = clicked29)
btn30 = Button(root, width = 3, command = clicked30)
btn31 = Button(root, width = 3, command = clicked31)
btn32 = Button(root, width = 3, command = clicked32)
btn33 = Button(root, width = 3, command = clicked33)
btn34 = Button(root, width = 3, command = clicked34)
btn35 = Button(root, width = 3, command = clicked35)
btn36 = Button(root, width = 3, command = clicked36)
btn37 = Button(root, width = 3, command = clicked37)
btn38 = Button(root, width = 3, command = clicked38)
btn39 = Button(root, width = 3, command = clicked39)
btn40 = Button(root, width = 3, command = clicked40)
btn41 = Button(root, width = 3, command = clicked41)
btn42 = Button(root, width = 3, command = clicked42)
btn43 = Button(root, width = 3, command = clicked43)
btn44 = Button(root, width = 3, command = clicked44)
btn45 = Button(root, width = 3, command = clicked45)
btn46 = Button(root, width = 3, command = clicked46)
btn47 = Button(root, width = 3, command = clicked47)
btn48 = Button(root, width = 3, command = clicked48)

btn0.grid(row = 0, column = 0)
btn1.grid(row = 0, column = 1)
btn2.grid(row = 0, column = 2)
btn3.grid(row = 0, column = 3)
btn4.grid(row = 0, column = 4)
btn5.grid(row = 0, column = 5)
btn6.grid(row = 0, column = 6)
btn7.grid(row = 1, column = 0)
btn8.grid(row = 1, column = 1)
btn9.grid(row = 1, column = 2)
btn10.grid(row = 1, column = 3)
btn11.grid(row = 1, column = 4)
btn12.grid(row = 1, column = 5)
btn13.grid(row = 1, column = 6)
btn14.grid(row = 2, column = 0)
btn15.grid(row = 2, column = 1)
btn16.grid(row = 2, column = 2)
btn17.grid(row = 2, column = 3)
btn18.grid(row = 2, column = 4)
btn19.grid(row = 2, column = 5)
btn20.grid(row = 2, column = 6)
btn21.grid(row = 3, column = 0)
btn22.grid(row = 3, column = 1)
btn23.grid(row = 3, column = 2)
btn24.grid(row = 3, column = 3)
btn25.grid(row = 3, column = 4)
btn26.grid(row = 3, column = 5)
btn27.grid(row = 3, column = 6)
btn28.grid(row = 4, column = 0)
btn29.grid(row = 4, column = 1)
btn30.grid(row = 4, column = 2)
btn31.grid(row = 4, column = 3)
btn32.grid(row = 4, column = 4)
btn33.grid(row = 4, column = 5)
btn34.grid(row = 4, column = 6)
btn35.grid(row = 5, column = 0)
btn36.grid(row = 5, column = 1)
btn37.grid(row = 5, column = 2)
btn38.grid(row = 5, column = 3)
btn39.grid(row = 5, column = 4)
btn40.grid(row = 5, column = 5)
btn41.grid(row = 5, column = 6)
btn42.grid(row = 6, column = 0)
btn43.grid(row = 6, column = 1)
btn44.grid(row = 6, column = 2)
btn45.grid(row = 6, column = 3)
btn46.grid(row = 6, column = 4)
btn47.grid(row = 6, column = 5)
btn48.grid(row = 6, column = 6)

root.mainloop()