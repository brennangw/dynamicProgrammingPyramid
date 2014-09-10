from pyramidGen import Pyramid
from _operator import attrgetter
def dynSolve (p):

    for row in range(p.height -2 ,-1,-1):
        #print(str(row) + ":")
        for i in range(0,len(p.nums[row])):
            p.nums[row][i].minimumPathValue += min(p.nums[row+1][i].minimumPathValue,p.nums[row+1][i+1].minimumPathValue)

    print("after finding path values:" + str(p))
    
    
    i = 0
    for h in range(0,len(p.nums)-1):
        row = p.nums[h+1]
        i = row.index(min(row[i],row[i+1],key=attrgetter('minimumPathValue')))
        print (str(i))

"""
Start at bottom row
    Get next row (if not already at the top)
    for each element in next row the matching elements are the same index and index + 1
    find out which 
"""