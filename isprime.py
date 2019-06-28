def isprime(n):
    if n <=1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
        else:
            return True

def list_primes():
    for n in range(1000):
        if isprime(n):
            print(n, end=' ', flush= True)
        print()

list_primes()        
