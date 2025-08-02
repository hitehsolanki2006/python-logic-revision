def swepUsethirdVar(num1,num2):
  
    temp=num1
    num1=num2
    num2=temp
    
    return f"After Swep Num1 {num1} and Num2{num2} " 


def swepWithoutthirdVar(var1,var2):
    var1=var1+var2
    var2=var1-var2
    var1=var1-var2
    return f"After Swep Num1 {var1} and Num2{var2} " 
