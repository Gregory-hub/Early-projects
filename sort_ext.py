import os
import shutil

os.chdir('F:\\Music')

for file in os.listdir():
	name, ext = os.path.splitext(file)
	if ext == '.flac':
		shutil.move(file, 'Flac')
	elif ext == '.mp3':
		shutil.move(file, 'MP3')