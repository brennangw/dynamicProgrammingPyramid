import random

class PNum:
    value = 0
    minimumPathValue = 0
    def __init__(self, val):
        self.minimumPathValue = val
        self.value = val
    def __repr__(self):
        return str("v: " + str(self.value) +",mpv: " + str(self.minimumPathValue))
        

class Pyramid:
    nums = []
    height = None
    def makeList(self,height):        
        for h in range (1,height+1):
            newRow = []
            index = 0
            while (index < h):
                newRow.append(PNum(random.randint(0,9)))
                index += 1
            self.nums.append(newRow)
        print("made pyramid:\n" + str(self) )

    def __init__(self, height):
        self.height = height
        self.makeList(height)
    def __repr__(self):
        toReturn = ""
        for row in self.nums:
            toReturn = toReturn + "\n" + str(row)
        return toReturn