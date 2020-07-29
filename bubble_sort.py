def bubble_sort(A):
	for i in range(1, len(A)):
		f = 0
		for bubble in range(len(A) - i):
			if A[bubble] > A[bubble + 1]:
				A[bubble], A[bubble + 1] = A[bubble + 1], A[bubble]
				f = 1
		if f == 0:
			return A
	return A


A = list(map(int, input().split()))	
print("Unsorted:", A)
A = bubble_sort(A)
print("Sorted:", A)