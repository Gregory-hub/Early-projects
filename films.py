import os

os.chdir('../Telegram downloads/')
filenames = os.listdir()
print("\nOld:", *filenames, sep='\n', end='\n\n')

newnames = []
for name in filenames:
	name, ext = os.path.splitext(name)
	name = name.replace(' ', '.')
	parts = name.split('.')
	if parts[0:3] == ['Better', 'Call', 'Saul']:
		parts = parts[:4]
	name = ''
	for part in parts:
		name += f'{part} '
	name = name.strip() + ext
	newnames.append(name)
print("New:", *newnames, sep='\n')

if input("Tap 'Y' to rename files, 'N' not to do this:\n") == 'Y':
	for i in range(len(filenames)):
		os.rename(filenames[i], newnames[i])