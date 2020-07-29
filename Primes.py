def is_prime(n):
	for divisor in range(2, n // 2 + 1):
		if n % divisor == 0:
			return False
	return True


A = [i if is_prime(i) else 0 for i in range(2, 100)]
for i in A:
	print(str(i) + ' ' if i != 0 else '', end = '')