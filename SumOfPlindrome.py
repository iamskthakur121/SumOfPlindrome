sum = 0
for num in range(10000,100000):# take the range of the 5 digit number
    
    string = str(num) #change the string to number
    
    k = string[::-1] # reverse the string
    
    if(string==k): 
        sum+=num
        
    else:
        sum=sum
        


print(sum) #print sum