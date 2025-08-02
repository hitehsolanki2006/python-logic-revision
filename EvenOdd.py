def EvenOdd(x):
  if (x % 2 == 0):
    return True
  else:
    return False

def countEvenOdd(list1):
  
  counteven=0
  countodd=0  
  for i in list1:
    if EvenOdd(i)==True:
      counteven+=1
    else :
      countodd+=1
  countEvenOdd={"Even Count":counteven,"Odd Count":countodd}
  return countEvenOdd