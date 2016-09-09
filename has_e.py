def has_no_e(word):
    for letter in word:
        if letter == "e":
            return False
    return True

def has_e(n):
    for i in n:
        if i == "e":
            return True
    return False

fin = open('words.txt')

list_1 = []
list_2 = []

for line in fin:
    if has_no_e(line):
        list_1 += line
x = len(list_1)

fine = open('words.txt')        
for z in fine:
    if has_e(z):
        list_2 += z
y = len(list_2)

h = x + y

print x
print y
print h

print x/h
