from random import *


def insert_sort(A):
	"""insert sort"""
	for last_i in range(1, len(A)):
		for i in range(last_i, 0, -1):
			if A[i] < A[i - 1]:
				A[i], A[i - 1] = A[i - 1], A[i]
	return A


def choise_sort(A):
	"""choise sort"""
	for winner_place in range(len(A) - 1):
		for i in range(winner_place + 1, len(A)):
			if A[i] < A[winner_place]:
				A[winner_place], A[i] = A[i], A[winner_place]
	return A


def bubble_sort(A):
	"""bubble sort"""
	for i in range(1, len(A)):
		f = 0
		for bubble in range(len(A) - i):
			if A[bubble] > A[bubble + 1]:
				A[bubble], A[bubble + 1] = A[bubble + 1], A[bubble]
				f = 1
		if f == 0:
			return A
	return A


def test_sort(algorithm):
	print("Algorithm:", algorithm.__doc__)

	ok = True
	print("Tests result: ", end='')
	for i in range(50):
		A = [i for i in sample(range(100), 20)]
		if algorithm(A) != sorted(A):
			ok = False
			break
	print("Ok" if ok == 1 else "Fail", end='\n\n')


test_sort(insert_sort)
test_sort(choise_sort)
test_sort(bubble_sort)