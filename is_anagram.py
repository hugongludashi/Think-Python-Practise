def is_anagram(i, j):
    return i == j[::-1]

print is_anagram('sfaefae', 'eafeafs')
print is_anagram('sdfae', 'faefae')
        
