import random

def shuffle(arr):
	"""Performs a Durstenfeld shuffle on the given list."""
	n = len(arr)
	for j in range(n-1):
		k = random.randint(j,n-1)
		arr[j], arr[k] = arr[k], arr[j]
	return arr

print shuffle(range(10))
