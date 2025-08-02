

def isPalidrome(num):
    originalNum=num
    s=0
    while num>0:
        r=num%10
        s=r+s*10
        num=num//10
    if originalNum==s:
        return f"{originalNum} Number is Palindrome "
    else:
        return f"{originalNum} Number is not palindrome"
        
    