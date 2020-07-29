from math import sqrt, floor
number_of_buttons = 49
number_of_bombs = 20
with open("sapper.py", 'w') as file:
# Generates list of bombs
	file.write(f"""from tkinter import *
from random import randint
from math import sqrt, floor

number_of_bombs = {number_of_bombs}
number_of_buttons = {number_of_buttons}

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


""")
# Generating functions
	for fun in range(0, number_of_buttons):
		index1 = floor(fun / int(sqrt(number_of_buttons)))
		index2 = fun % int(sqrt(number_of_buttons))
		file.write(f"""def clicked{fun}():
	if bombs[{index1}][{index2}] == 0:
		btn{fun}['bg'] = "gray"
		if bombs_around({fun}) > 0:
			btn{fun}['text'] = bombs_around({fun})
	else:
		btn{fun}['bg'] = "red"

""")
	file.write(f"""
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
""")
	file.write("""
root = Tk()
root.title = "Sapper"

""")
	for button in range(0, number_of_buttons):
		file.write(f"""btn{button} = Button(root, width = 3, command = clicked{button})
""")
	file.write("\n")
	for row in range(0, int(sqrt(number_of_buttons))):
		for column in range(0, int(sqrt(number_of_buttons))):
			file.write(f"""btn{column + int(sqrt(number_of_buttons)) * row}.grid(row = {row}, column = {column})
""")
	file.write("\nroot.mainloop()")