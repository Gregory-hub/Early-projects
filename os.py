import os

os.chdir('directory')

with open('test1.txt', 'w') as f:
	for i in range(10000):
		f.write(i)
print(os.stat('test1.txt'))
print(os.listdir())