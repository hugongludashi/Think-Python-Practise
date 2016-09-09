
def is_not_avoid(j, letter):
    for i in j:
        if i == letter:
            return True
    return False


def avoids(word, forbidden_letters):
    for k in forbidden_letters:
        if is_not_avoid(word, k):
            return False
    return True

input_letters = raw_input("Please enter some forbidden letters you want.")

fin = open('words.txt')

list = []

for line in fin:
    word = line.strip()
    if avoids(word, input_letters):
        list += word

x = len(list)

print x



    
