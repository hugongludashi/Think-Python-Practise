
def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


j = histogram('brontosaurus')
print j

def print_hist(h):
    k = h.keys()
    k.sort()
    for i in k:
        print i, h[i]


print print_hist(j)
