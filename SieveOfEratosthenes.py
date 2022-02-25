import time

# Implement Sieve of Eratosthenes algorithm to find all prime numbers up to a given limit.
def sieve_of_eratosthenes(limit):
	start_time = time.perf_counter()

	# Create a list of booleans, where True represents a prime number.
	# Initially, all numbers are prime.
	is_prime = [True] * (limit + 1)
	# Set the 0 and 1 numbers to False.
	is_prime[0] = is_prime[1] = False
	# Loop through all numbers from 2 to the limit.
	for i in range(2, int(limit ** 0.5) + 1):
		# If the number is prime, loop through all multiples of the number.
		if is_prime[i]:
			# Loop through all multiples of the number.
			for j in range(int(i ** 2), limit + 1, i):
				# Set the number to False.
				is_prime[j] = False

	prime_array = [i for i in range(limit + 1) if is_prime[i]]

	process_time = time.perf_counter() - start_time

	# print(prime_array)
	# print(len(prime_array), "primes found in", process_time, "seconds.")
	
	# Return the list of prime numbers.
	return prime_array

def time_f(times, func, *args):
	total_time = 0;
	for i in range(times):
		start_time = time.perf_counter_ns()
		func(*args)
		total_time += time.perf_counter_ns() - start_time
	print(len(func(*args)))
	return total_time / times;

print("Primes found in", time_f(50, sieve_of_eratosthenes, 1000000) / 1000000000, "seconds on average.")