# Largerst

def findLargerst(list1):
    size=len(list1)
    largerst=list1[0]
    for i in range(0,size):
        if list1[i]>largerst:
            largerst=list1[i]
            
    return largerst



# Smallerst

def findSmallerst(list1):
    size=len(list1)
    smallerst=list1[0]
    for i in range(0,size):
        if list1[i] < smallerst:
            smallerst=list1[i]
    
    return smallerst
   