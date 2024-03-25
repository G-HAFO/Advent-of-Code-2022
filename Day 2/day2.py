score1 = 0 
score2 = 0

def check_my_choice(choice):
    if choice[2]== 'X' :
        return 1
    elif choice[2] == 'Y' :
        return 2
    elif choice[2] == 'Z' :
        return 3
    else:
        print("Error: Invalid user choice")
    return 0

win = ["A Y","B Z","C X"] 
draw = ["A X","B Y","C Z"] 
loss = ["A Z","B X","C Y"]

pickings = ["X","Y","Z"]

def change_result(choice):
    i = 0
    if choice[2] == 'Z':
        while choice[0] != win[i][0]:
            i += 1
        return win[i]
    elif choice[2] == 'Y':
        while choice[0] != draw[i][0]:
            i += 1
        return draw[i]
    elif choice[2] == 'X':
        while choice[0] != loss[i][0]:
            i += 1
        return loss[i]
    else:
        print("Error: Invalid user choice")

def check_result(choice):
    if choice in win:
        return 6
    elif choice in draw:
        return 3
    elif choice in loss:
        return 0
    else:
        print("Error: Invalid user choice")


with open("data.txt", "r") as f:
    for line in f:
        if line.strip():
            score1 += check_my_choice(line.strip())
            score1 += check_result(line.strip())
            line = change_result(line.strip())
            score2 += check_my_choice(line.strip())
            score2 += check_result(line.strip())
        else:
            break
print(score1, score2)
