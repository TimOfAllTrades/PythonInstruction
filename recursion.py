
#Permutations by recursion simple output.  This will output all 27 three letter permutations from the character set a b and c
charlist = ["a","b","c","d"]
def AppendPerm(charlist, depth, currentstring):
    if depth < 3:
        for char in charlist:
            currentstring.append(char)
            AppendPerm(charlist, depth + 1, currentstring)
            currentstring.pop()
    else:
        print(currentstring)
        return 0

AppendPerm(charlist, 0, [])

#Permutations by recursion simple output.  return as a list

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

#plist = permute(["a","b","c"])
#print(plist)

#With repetition now
def repetitionpermute(s, depth):
    out = []
    if depth > 1:
        print("hit the end")
        return s
    else:
        for i, let in enumerate(s):
            print("letter", let)
            print("Current index", i)
            print(s[:i] + s[i+1:])
            for perm in repetitionpermute(s, depth + 1):
                print("permutation",perm)
                out += [let + perm]
                print("out", out)
    return out

plist = repetitionpermute(["a","b","c"],0)
print(plist)
print(len(plist))







def AppendComb(charlist,currentstring):
    if len(charlist)>1:
        for char in charlist:
            currentstring.append(char)
            AppendComb(charlist[1:],currentstring)
            currentstring.remove(char)
    else:
        print(currentstring)
        

#AppendComb(charlist,[])
