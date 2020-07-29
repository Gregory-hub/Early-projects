class A(Exception):
	pass

class B(Exception):
	pass

try:
	mon = int(input("Enter a number of month: "))
	if mon > 0 and mon < 3 or mon == 12:
		print("Winter")
	elif 2 < mon < 6:
		print("Spring")
	elif 5 < mon < 9:
		print("Summer")
	elif 8 < mon < 12:
		print("Autumn")
	elif mon < 1: 
		raise A
	elif mon > 12:
		raise B
except A:
	print("ERRORRR!!! Month cannot be less than 1")
except B:
	print("EEEERRORRRR!!! Month cannot be more than 12!")
except ValueError:
	print("ERRRROR! Enter a number please")