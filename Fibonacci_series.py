def FeboItrative(num):
  num1 = 1
  num2 = 0
  fibo_list = [0, 1]

  for i in range(3, num + 1):
    temp = num1 + num2
    num2 = num1
    num1 = temp
    fibo_list.append(temp)
  return fibo_list

def FiboRecursive(n):
  def fib(n):
      if n <= 1:
          return n
      return fib(n - 1) + fib(n - 2)

  fibo_list = []
  for i in range(n):
      fibo_list.append(fib(i))
  return fibo_list

