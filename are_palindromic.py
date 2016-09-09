"""first to check if a digit have palindromic letters with length "len",
when written with str()
"""
def is_palindromic(i, start, len):
    s =  str(i)[start:start+len]
    return s == s[::-1]

"""use the writer's description to set condition for the palindromic digits"""
def are_palindromic(i):
    return (is_palindromic(i, 2, 4) and
            is_palindromic(i+1, 1, 5) and
            is_palindromic(i+2, 1, 4) and
            is_palindromic(i +3, 0, 6))

"""check all the six digits to see if we can find which has this spec"""
def check_all():
    i =100000
    while i <= 999996:
        if are_palindromic(i):
            print i
        i += 1

print "What I first looked on the odometer are as following:"
print check_all()
