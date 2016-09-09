def has_duplicates(list):
    t= list[::1]
    t.sort()
    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            return True
    return False

import random

def check_bdays(n):
    res = []
    for i in range(n):
        bdays = random.randint(1, 365)
        res.append(bdays)
    return res



def check_matches(students, samples):
    count = 0
    for k in range(samples):
        t = check_bdays(students)
        if has_duplicates(t):
            count += 1
    return count

num_students = 23
num_samples = 1000
count = check_matches(num_students, num_samples)

print "After %d times test" % num_samples
print " for %d students" % num_students
print "%d of students has the same birthday" % count

