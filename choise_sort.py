def choise_sort(A):
	for winner_place in range(len(A) - 1):
		for i in range(winner_place + 1, len(A)):
			if A[i] < A[winner_place]:
				A[winner_place], A[i] = A[i], A[winner_place]
	return A


A = list(map(int, input().split()))	
print("Unsorted:", A)
A = choise_sort(A)
print("Sorted:", A)