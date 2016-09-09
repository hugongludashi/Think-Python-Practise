def nested_sum(i):
    total = 0
    for k in i:
        if type(k) == int:
            total += k
        if type(k) == list:
            total += sum(k)
    return total


print nested_sum([2, 3, [4, 5, 6], [4, 2, 4, 5], [3, 2, 5]])
        
