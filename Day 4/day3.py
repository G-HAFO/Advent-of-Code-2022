import numpy as np
import string  

with open('data.txt', 'r') as file:
    data = file.readlines()

result = []
for line in data:
    pairs = line.strip().split(',')
    for pair in pairs:
        result.append(list(map(int, pair.split('-'))))

### compares two lists of ranges and check if one completely overlaps the other, example: [4, 6] and [6, 6] completely overlap
def check_overlap(result):
    nmb_of_overlaps = 0
    for i in range(0, len(result), 2):  # iterate through the list in steps of 2
        if result[i][0] >= result[i+1][0] and result[i][1] <= result[i+1][1]:
            nmb_of_overlaps += 1
        elif result[i][0] <= result[i+1][0] and result[i][1] >= result[i+1][1]:
            nmb_of_overlaps += 1
    return nmb_of_overlaps

print(check_overlap(result)) 
###same ad check_overlap but check if even one number overlaps, example: [4, 6] and [1, 4] overlap      
def check_overlap2(result):
    nmb_of_overlaps = 0
    for i in range(0, len(result), 2):  
        range1 = np.arange(result[i][0], result[i][1]+1)
        range2 = np.arange(result[i+1][0], result[i+1][1]+1)
        if any(np.in1d(range1, range2)):
            nmb_of_overlaps += 1
    return nmb_of_overlaps        
print(check_overlap2(result))