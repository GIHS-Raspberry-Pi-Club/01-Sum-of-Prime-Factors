https://codeshare.io/aYby4L

"""
For this week's challenge
Write a function that finds the sum of all prime factors of a given number (n)

Advanced Extension: Try to write your function without using trial division!
	- https://en.wikipedia.org/wiki/Fermat's_factorization_method
  - https://en.wikipedia.org/wiki/Quadratic_sieve
  - http://en.wikipedia.org/wiki/Pollard's_rho_algorithm
  - https://en.wikipedia.org/wiki/Dixon's_factorization_method

"""
def primeFactor(n):
  pFact = []
  for i in range(1, n):
    remainder = n%i
  	if remainder == 0:
      pFact.append(i)
  return pFact

print(primeFactor(int(input("Give us a number!!!:)"))))
