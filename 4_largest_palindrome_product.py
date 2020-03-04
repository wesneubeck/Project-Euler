# Largest palindrome product

# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of 
# two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two n-digit numbers.
# n = number of digits

def largest_palindome_product(n):
  # get the range
  x = int('9' * n)
  print(x)
  a = int('1' + ('0' * (n-1)))
  print(a)
  
  # create the list of range numbers
  lst = [i for i in range(x, a-1, -1)]
  print(lst) 
  
  # list of palindrome #s
  pal = []
  for o in range(x-a):
    multi_num = lst.pop(0)
    for ele in lst:
      result = multi_num * ele
      rev = str(result)
      if rev == rev[::-1]:
        pal.append(result)
  pal.sort()
  return pal[-1]


print(largest_palindome_product(4))

# largestPalindromeProduct(2) should return 9009.
# largestPalindromeProduct(3) should return 906609.
