def gcd(a,b):
    if b == 0:
        return a
    if b !=0:
        return gcd(b,a%b)



print gcd( 4, 2)
