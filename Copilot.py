import time

def main(n:int):
  # find all primes up to n
  #time the execution
  # return a list of primes, time, and number of primes
  startTime = time.time()
  primes = [2]
  for i in range(3, n):
    for j in primes:
      if i % j == 0:
        break
      elif j > int(i**0.5):
        primes.append(i)
        break
    else:
      primes.append(i)
  print('Slow:', time.time() - startTime, 's')
  return primes, time.time() - startTime, len(primes)

print(main(10000))
