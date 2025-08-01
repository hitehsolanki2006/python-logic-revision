def FactRecusion(num):
  if (num >= 1):
    return num * FactRecusion(num - 1)
  else:
    return 1


def FactItertion(num):
  fact = 1
  for i in range(1,num + 1):
    fact = fact * i
  return fact
