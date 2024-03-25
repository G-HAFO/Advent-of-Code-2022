import numpy as np
import string  

def find_common_elements(s1, s2):
    result = list(set(s1)&set(s2))
    return ''.join(result)


 


def split_array(array):
    firstpart, secondpart = array[:int(len(array)/2)], array[int(len(array)/2):]
    return find_common_elements(firstpart, secondpart)

values = dict()
for index, letter in enumerate(string.ascii_lowercase):
    values[letter] = index +1
for index, letter in enumerate(string.ascii_uppercase):
    values[letter] = index +27





with open("data.txt", "r") as f:
    sum = 0
    for line in f:
        if line:
           sum += values[split_array(line)]
           print(split_array(line),values[split_array(line)])
        else:
            break

print(sum)

def test(data):
    result = 0
    for i in range(0, len(data), 3):
        tmp1 = find_common_elements(data[i], data[i+1])
        tmp2 = find_common_elements(tmp1, data[i+2])
        result  += values[(tmp2)]
    return result


#### read lines from file and split lines at new line ccharacters
with open("data.txt", "r") as f:
    data = []
    for line in f:
        if line.strip():
          data.append(line.strip())  
        else:
            break

print(test(data))