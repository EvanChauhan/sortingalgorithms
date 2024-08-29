def fact(x):
  if x == 1:
    return 1
  else:
    return x * fact(x-1)

print fact(5)

# O(n) time complexity where n is the input as we have n recursive calls as n is only decremrented by 1 each time until we reach the base case