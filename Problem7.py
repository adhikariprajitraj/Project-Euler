def isPrime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
     
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True
def nthprime(num):
    j=1
    while num != 0:
        if isPrime(j)==True:
            num-=1
        j+=1
    return j-1
        

print(nthprime(10001))