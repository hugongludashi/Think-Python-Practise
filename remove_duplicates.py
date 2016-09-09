def remove_duplicates(list):
    k = []
    t = list[::1]
    f = list[::1]
    f.sort()
    t.sort()
    print t
    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            f.remove(t[i])
    return f
        
    
    
print remove_duplicates([1,3,5,1,5,1,5,2,4,2])
