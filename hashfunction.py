import time


def make_dictionary1(h):
    res = []
    i = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        res.append(word)
        res = i.keys()
    return h in i
    




from bisect import bisect_left

def make_dictionary2(h):
    res = []
    i = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        res.append(word)
        res = i.keys()
        g = bisect_left(res, h)
        if g != len(res) and res[g] == h:
            return True
        return False
    

start_time = time.time()
t =make_dictionary1('eafe')
past_time = time.time() - start_time
print past_time


start_time = time.time()
t =make_dictionary2('eafe')
past_time = time.time() - start_time
print past_time

    
    
