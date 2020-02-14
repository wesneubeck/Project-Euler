# Project Euler: Problem 3: Largest prime factor

########    lpf = Least Prime Factor


# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the given number

#  factors = I have to find the numbers that multipled together = n
#  append prime numbers in factors?
#  pop from prime list

def least_prime_factor(number):
  fact = []

  for i in range(2, number+1):
    if number % i == 0:
      fact.append(i)


  '''find the prime numbers in fact list '''
  prime = []
  for x in fact:
    if x > 1:
      for i in range(2,x):
        if (x % i) == 0:
          break
      else:
        prime.append(x)

  lpf= prime.pop()
  return lpf

print(least_prime_factor(7))

# largestPrimeFactor(2) should return 2.
# largestPrimeFactor(3) should return 3.
# largestPrimeFactor(5) should return 5.
# largestPrimeFactor(7) should return 7.
# largestPrimeFactor(13195) should return 29.
# largestPrimeFactor(600851475143) should return 6857
