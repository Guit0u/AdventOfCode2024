import os
import re
from functools import reduce
from operator import mul

global must_mul

def mul_part_1(operation):
    return reduce(mul,list(map(int , re.findall(r"\d+", operation))))
 
def mul_part_2(operation):
    global must_mul
    if(re.match(r"do\(\)", operation)): 
        must_mul = True 
        return 0
    if(re.match(r"don\'t\(\)", operation)): 
        must_mul = False
        return 0
    if(must_mul): 
        return reduce(mul,list(map(int , re.findall(r"\d+", operation))))
    return 0

input_file = os.path.join('inputs', 'input_3.txt')

with open(input_file,"r") as outfile:
    data = " ".join(outfile.readlines())

pattern = r"mul\(\d+,\d+\)"
x = re.findall(pattern, data)
print("day one result is ", sum(list(map(mul_part_1,x))))

pattern = r"(?:do\(\)|don\'t\(\)|mul\(\d+,\d+\))"
x = re.findall(pattern, data)
must_mul = True
print("day two result is ", sum(mul_part_2(operation) for operation in x))