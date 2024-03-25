sums = []
sum_ = 0

with open("data.txt", "r") as f:
    for line in f:
        if line.strip():
            sum_ += int(line.strip())
        else:
            sums.append(sum_)
            sum_ = 0

sums.sort()
print(sums[-1] + sums[-2] + sums[-3])
