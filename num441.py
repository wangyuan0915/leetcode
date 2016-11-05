def arrangeCoins(n):
	i = 1
	sumUp = 1
	while sumUp <= n:
		i += 1
		sumUp += i
	#print(i - 1)
	return i - 1

if __name__ == "__main__":
	arrangeCoins(5)