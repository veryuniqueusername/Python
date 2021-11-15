import time

#import list from PrimesList.py
# from PrimesList import primes

slowPrimes = [2]
fastPrimes = [2]

def slow():
	startTime = time.time()

	for i in range(3, 1000000):
		print(i)
		for j in range(2, i):
			if i % j == 0:
				break
		else:
			slowPrimes.append(i)

	print('Slow:', time.time() - startTime, 's')

def fast():
	startTime = time.time()

	for i in range(3, 5000000, 2):
		for j in fastPrimes:
			if i % j == 0:
				break
			elif j > i ** 0.5:
				# print(i)
				fastPrimes.append(i)
				break
		else:
			# print(i)
			fastPrimes.append(i)

	print('Fast:', time.time() - startTime, 's')

# slow()
fast()

# print(slowPrimes == fastPrimes)
# shortPrimes = primes[0:(primes.index(99991)+1)]
# print(shortPrimes)
# print(fastPrimes == shortPrimes)
# for i in range(0, len(shortPrimes)):
# 	if shortPrimes[i] != fastPrimes[i]:
# 		print(i)
# 		print(shortPrimes[i], fastPrimes[i])