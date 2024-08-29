def countdown(i):
  print i
  # base case
  if i <= 0:
    return
  # recursive case
  # for any number greater than 0
  else:
    countdown(i-1)

countdown(5)
