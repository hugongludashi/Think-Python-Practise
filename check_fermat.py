import math

def check_fermat(a, b, c, n):
    if n >= 2:
        if a**n + b**n == c**n:
            print "Holy smokes, Fermat was wrong!"
        else:
            print "No, that doesn't work."
    else:
        print "No, that doesn't work."

def user_input():
    print "Hi, here is the test for Fermat's Last Theorem that there are no positive integers a, b, and c such that a**n + b**n = c**n, for any values of n greater than 2."
    a = raw_input("What is the value of 'a' do you want to input?")
    b = raw_input("What is the value of 'b' do you want to input?")
    c = raw_input("What is the value of 'c' do you want to input?")
    n = raw_input("What is the value of 'n' do you want to input? Please remember that 'n' need to be greater than 2.")
    x = int(a)
    y = int(b)
    z = int(c)
    t = int(n)
    check_fermat(x, y, z, t)


user_input()
