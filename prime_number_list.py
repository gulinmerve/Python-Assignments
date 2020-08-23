n = 100
prime_list=[]
for x in range(2,n + 1):
    for y in range(2,x):     
        if (x % y) == 0:
            break
    else:
        prime_list.append(x)
print(prime_list)  ####This is First Answer

def primes(n):
    return [x for x in range(2, n+1) if all(x % y != 0 for y in range(2, x))]  
print(primes(100))     #####This is Second Answer