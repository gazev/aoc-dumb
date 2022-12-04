import requests
import os

cookies = {
    "session": os.environ.get("AOC_SESSION") 
}

if __name__ == '__main__':
    raw_data = requests.get("https://adventofcode.com/2022/day/4/input", cookies=cookies)
    data = raw_data.text.strip("\n").split("\n")

    inserted_count = 0
    overlap_count = 0
    for line in data:
        first, second = line.split(",")
        #  ...a...b..... -> a,b first
        #  .c......d...  -> c,d second
        a, b = first.split("-")
        c, d = second.split("-")

        if (int(a) >= int(c) and int(b) <= int(d)) or\
                (int(a) <= int(c) and int(b) >= int(d)):
            inserted_count += 1
            overlap_count += 1
            continue
            
        #   c <= a <= d     c <= b <= d     a <= c <= b     a <= d <= b
        #   ...a...b..      .a....b...      ..a...b...      ....a..b..
        #   .c...b....      ....c...d.      ....c...d.      .c....d...
        if int(c) <= int(a) <= int(d) or int(c) <= int(b) <= int(d) or\
            int(a) <= int(c) <= int(b) or int(a) <= int(d) <= int(b):
            overlap_count += 1

    print(inserted_count)
    print(overlap_count)
