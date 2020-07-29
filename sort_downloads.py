from shutil import move
import os

os.chdir('F:\\Downloads')

for file in os.listdir():
	src = os.getcwd() + '\\' + file
	name, ext = os.path.splitext(file)
	if ext == '.mp3' or ext == '.flac':
		move(src, '..\\Music')
	else:
		move(src, '..\\Videos')
print(*os.listdir(), sep='\n')