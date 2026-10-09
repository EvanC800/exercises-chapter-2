def isprime(n):
    prime_status = 1

    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            prime_status = 0

    if n == 1:
        return False
    
    elif prime_status == 0:
        return False
    
    else:
        return True
    
