def square(n:int)->int:
    return n*n
def cube(n:int)->int:
    return n*n*n
def factorial(n:int)->int:
    if(n<0):
        raise ValueError("Factorial of negative numbers is invalid")
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
def is_prime(n:int)->bool:
    if n<2:
        return False
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return False
    return True
def gcd(a:int,b:int)->int:
    n=1
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            n=i
    return n
def lcm(a:int, b:int)->int:
    i=max(a,b)
    while True:
        if i%a==0 and i%b==0:
            return i
        i+=1
