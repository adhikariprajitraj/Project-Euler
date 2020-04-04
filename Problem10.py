def isPrime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # we are doing this to decrease the time complexity
    if (n % 2 == 0 or n % 3 == 0 ) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True
total =2
for i in range(3,2000000,2):
    if isPrime(i) == True:
        total+= i
        
        
print(total)