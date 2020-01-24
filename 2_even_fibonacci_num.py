#  Even Fibonacci Numbers


#   Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
#  By starting with 1 and 2, the first 10 terms will be:

#  1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...


#  By considering the terms in the Fibonacci sequence that do not exceed the nth term, 
#  find the sum of the even-valued terms.

def even(n):
  fs = [1, 2]
  while len(fs)<n:
    x = fs[-1]+fs[-2]
    fs.append(x)
 
  a = []
  for i in fs:
    if i % 2 == 0:
      a.append(i)
  return sum(a)

print(even(23))

# fiboEvenSum(10) should return 44.
# fiboEvenSum(18) should return 3382.
# fiboEvenSum(23) should return 60696.
# fiboEvenSum(43) should return 350704366.
# Your function should return an even value.