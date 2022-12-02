#! /usr/bin/env python3
import requests

cookies = {
    "session": ""
}

if __name__ == '__main__':
    raw_data = requests.get("https://adventofcode.com/2022/day/1/input", cookies=cookies)
    data = raw_data.text.strip("\n").split("\n\n")

    elfs = []
    for e in data:
        arr = map(int, e.split("\n"))
        elfs.append(sum(arr))
    
    total = 0
    for i in range(3):
        total += max(elfs)
        elfs.remove(max(elfs))
    
    print(total)
