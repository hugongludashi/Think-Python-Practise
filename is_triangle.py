def is_triangle(a, b, c):
    if a + b < c:
        print "No"
    else:
        print "Yes"


def user_input():
    print "Hi, here is a test whether the value of the three sticks you input can form a triangle."
    a = raw_input("Please enter the value of first stck.")
    b = raw_input("Please enter the value of second stck.")
    c = raw_input("Please enter the value of three stck.")
    x = int(a)
    y = int(b)
    z = int(c)
    is_triangle(x, y, z)

user_input()
