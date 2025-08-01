def isprime(num):
  if num < 2:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % 2 == 0:
      return False
  return True


def Nprime(n):
  primelist = []
  for num in range(2, n + 1):
    if isprime(num):
      primelist.append(num)
  return primelist
