import requests
import os

cookies = {
    "session": os.environ.get("AOC_SESSION")
}

if __name__ == '__main__':
    raw_data = requests.get("https://adventofcode.com/2022/day/5/input", cookies=cookies)
    data = raw_data.text.strip("\n").split("\n")
    
    stacks = [[] for i in range(9)]

    #parse initial configuration
    while (line := data.pop(0)) != "":
        for i in range(1, len(line), 4):
            if 'A' <= line[i] <= 'Z':
                stacks[i // 4].append(line[i])

    for line in data:
        amount, orig, dest = [int(x) for x in line.split() if x.isnumeric()]
        moved = [] 
        while (amount := amount - 1) > -1:
            moved.append(stacks[orig - 1].pop(0))
        stacks[dest - 1] = moved + stacks[dest - 1]

    for s in stacks:
        print(s[0])
        