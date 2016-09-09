def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

def capitalize_nested(i):
    les = []
    for k in i:
        if type(k) == str:
            les.append(k.capitalize())
        if type(k) == list:
            les.append(capitalize_all(k))
    return les
            
print capitalize_nested(["faefae", "dafeaef", ["eafe", "wewf", "wewe"],
                         ["eafefa", "dfaef", "efae"]])
