import os

input_file = os.path.join('inputs', 'input_1.txt')

with open(input_file,"r") as outfile:
    data = outfile.readlines()
    left_list = []
    right_list = []
    for line in data:
        split = line.strip().split(' ') 
        split.remove('')
        split.remove('')
        right_list.append(split.pop())
        left_list.append(split.pop())

sum = 0
while(len(left_list) > 0):
  sum += abs(int(left_list.pop(left_list.index(min(left_list)))) - int(right_list.pop(right_list.index(min(right_list)))))

print("day one result is ",sum)

occurences = {'0': 0}
with open(input_file,"r") as outfile:
    data = outfile.readlines()
    left_list = []
    for line in data:
        split = line.strip().split(' ') 
        split.remove('')
        split.remove('')
        key = split.pop()
        if key not in occurences.keys():
            occurences[key] = 0
        occurences[key] += 1
        left_list.append(split.pop())

sum = 0
for element in left_list:
    if element in occurences.keys():
        sum += (int(element)*occurences[element])

print("day two result is",sum)