### 
###  Provides list of beautiful numbers in given range
###

def isBeautifulNumber(l, r):

    ### check the given range for beautiful numbers
    for num in range(l, r):  
        i = 0
        myList = []
    
    
        while (num > 0 & i < 6):
            ### Example Data: Num = 32
            ### sum = 3, rem = 2
            sum = 0 
            rem = num % 10
            sum = sum + (rem * rem)
            num = num - rem / 10
            
            ### calculate if number is beautiful
            result = (num ** 2) + (rem ** 2)
    
            if(result == 1):
                myList.apprend()

            ### if not beautiful add a counter up to 6 attempts

            else:
                i +=1 
        

    ### return list of beautiful numbers
    return sum(myList)
