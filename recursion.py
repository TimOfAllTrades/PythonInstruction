
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

#AppendPerm(charlist, 0, [])


def AppendComb(charlist,currentstring):
    if len(charlist)>1:
        for char in charlist:
            currentstring.append(char)
            AppendComb(charlist[1:],currentstring)
            currentstring.remove(char)
    else:
        print(currentstring)
        

AppendComb(charlist,[])
