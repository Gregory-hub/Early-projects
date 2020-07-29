def insert_sort(A):
	for last_i in range(1, len(A)):
		for i in range(last_i, 0, -1):
			if A[i] < A[i - 1]:
				A[i], A[i - 1] = A[i - 1], A[i]
	return A


A = list(map(int, input().split()))	
print("Unsorted:", A)
A = insert_sort(A)
print("Sorted:", A)