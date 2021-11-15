import time

#import list from PrimesList.py
from PrimesList import primes

slowPrimes = [2]
fastPrimes = [2]

def slow():
	startTime = time.time()

	for i in range(3, 100000):
		for j in range(2, i):
			if i % j == 0:
				break
		else:
			slowPrimes.append(i)

	print(time.time() - startTime, 's')

def fast():
	startTime = time.time()

	for i in range(3, 100000, 2):
		for j in fastPrimes:
			if i % j == 0:
				break
			elif j > i ** 0.5:
				fastPrimes.append(i)
				break
		else:
			fastPrimes.append(i)

	print(time.time() - startTime, 's')

slow()
fast()

print(slowPrimes == fastPrimes)
shortPrimes = primes[0:1229]
print(slowPrimes == shortPrimes)
for i in range(0, len(shortPrimes)):
	if shortPrimes[i] != slowPrimes[i]:
		print(i)
		print(shortPrimes[i], slowPrimes[i])