import random


def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p**2 <= n:
        if is_prime[p]:
            for i in range(p*2, n+1, p):
                is_prime[i] = False
        p += 1
    primes=[]
    for i in range(0,n+1):
        if is_prime[i]==False and i>=2:
            primes.append(i)
    return primes

def selectKey():
    primes=sieve(random.randint(300,500))
    p=random.choice(primes)
    primes.remove(p)
    q=random.choice(primes)
    n=p*q
    fi=(p-1)*(q-1)
    print(f"N is {n} and fi is {fi}")

# print(f"n is {n} and list is {sieve(n)}")
