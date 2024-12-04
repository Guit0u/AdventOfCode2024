import os
import re

def SumXmas(data,i,j):
    xMasStrings = []
    xMasStrings.append(''.join(data[x][j] for x in range(i, min(i+4, len(data)))))
    xMasStrings.append(''.join(data[x][j] for x in range(i, max(i-4, -1),-1)))
    xMasStrings.append(''.join(data[i][x] for x in range(j, min(j+4, len(data[0])))))
    xMasStrings.append(''.join(data[i][x] for x in range(j, max(j-4, -1),-1)))
    xMasStrings.append(''.join(data[i+x][j+x] for x in range(0,min(len(data)-i,len(data[0])-j,4))))
    xMasStrings.append( ''.join(data[i+x][j-x] for x in range(0,min(len(data)-i,j+1,4))))
    xMasStrings.append(''.join(data[i-x][j+x] for x in range(0,min(i+1,len(data[0])-j,4))))
    xMasStrings.append(''.join(data[i-x][j-x] for x in range(0,min(i+1,j+1,4))))
    return sum(x == "XMAS" for x in xMasStrings)

def isCrossMax(data,i,j):
    pattern = r"(?:MAS|SAM)"
    leftString = ''.join(data[i+x][j+x] for x in range(-1,2))
    rightString = ''.join(data[i+x][j-x] for x in range(-1,2))
    return re.match(pattern,leftString) and re.match(pattern,rightString)

input_file = os.path.join('inputs', 'input_4.txt')
resultPartOne = 0
resultPartTwo = 0
with open(input_file,"r") as outfile:
    data = list(map(str.rstrip,outfile.readlines()))

for i in range(len(data)):
    for j in range(len(data[0])):
        if(data[i][j] == "X"): resultPartOne+= SumXmas(data,i,j)
        if(data[i][j] == "A" and i > 0 and j > 0 and i < len(data) - 1 and j < len(data[0])-1):
            if(isCrossMax(data,i,j)) : resultPartTwo+=1
print("day one result is ", resultPartOne)
print("day two result is ", resultPartTwo)