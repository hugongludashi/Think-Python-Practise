
fin = open('words.txt')

for line in fin:
    word = line.strip()
    t = {}
    for x in fin:
        word1 = x.strip()
        if word == word1[::-1]:
            t[word] = word1
        
    print t
    
