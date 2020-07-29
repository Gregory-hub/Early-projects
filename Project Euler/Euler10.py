import time
from math import *


start = time.time()
def primeCheck(num):
	if num == 2:
		return True
	if num < 2 or num % 2 == 0:
		return False
	for i in range(3, int((num**1/2)) - 1, 2):
		if num % i == 0:
			return False
	return True


array = []
num = 100
for i in range(1, num + 1):
	array.append(i)

print(array)




print(array)

end = time.time()
print("timerange: ", end - start)