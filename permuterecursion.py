def permute(s):
    out = []
    if len(s) == 1:
        print("hit the end")
        return s
    else:
        for i, let in enumerate(s):
            print("letter", let)
            print("Current index", i)
            print(s[:i] + s[i+1:])
            for perm in permute(s[:i] + s[i+1:]):
                print("permutation",perm)
                out += [let + perm]
                print("out", out)
    return out

plist = permute(["a","b","c"])
print(plist)