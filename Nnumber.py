def n_number(n):
  numlist = []
  if n <= 0:
    return "Enter valid input"
  for i in range(1, n + 1):
    numlist.append(i)

  return numlist
