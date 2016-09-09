def is_sorted(list):
    i = 0
    while i < len(list)-1:
        if list[i] > list[i+1]:
            return False
        i +=1
    return True


    
print is_sorted([1,2,1])


