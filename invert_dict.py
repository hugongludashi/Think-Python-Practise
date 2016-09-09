def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        t = inverse.setdefault(val, [])
        t.append(key)
    return inverse


def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


j = histogram('brontosaurus')


if __name__ == '__main__':
    inverse = invert_dict(j)
    for val, keys in inverse.iteritems():
        print val, keys
