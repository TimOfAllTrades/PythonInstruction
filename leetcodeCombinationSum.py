

numlist = [2,3,5]

class combsumobj:

    masterlist = []
    numlist = [2,3,4]

    def __init__(self):
        self.masterlist = []
        self.mastersumlist = []

    def AppendPerm(self, numlist, depth, currentstring, target, sumlist):
        if currentstring < target:
            for i in numlist:
                #print("current index",i)
                currentstring += i
                sumlist.append(i)
                result = self.AppendPerm(numlist, depth + 1, currentstring, target, sumlist)
                print("list",result[0])
                #sumlist.append(result[0])
                print("current sum",result[1])
                
                currentstring -= i
                sumlist.pop()
        
        return sumlist,currentstring
        

    def AppendPerm1(self, numlist, depth, currentstring, target, sumlist):
        
        for i in numlist:
            if currentstring < target:
                currentstring += i
                sumlist.append(i)
                sum = self.AppendPerm(numlist, depth + 1, currentstring, target, sumlist)
                if sum == target:
                    print(sumlist)
                    self.masterlist.append([sumlist])
                    self.mastersumlist.append(sum)
                    #print(self.masterlist)
                currentstring -= i
                sumlist.pop()
        
            else:
                return currentstring

combsuminstance = combsumobj()


combsuminstance.AppendPerm(numlist, 0, 0, 8, [])
