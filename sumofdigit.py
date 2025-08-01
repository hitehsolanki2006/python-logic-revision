def SumOfDigit(num):
  digit_sum = 0
  while num > 0:
    digit = num % 10
    digit_sum += digit
    num = num // 10
  return digit_sum
