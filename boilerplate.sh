#! /bin/bash

src="$1/aoc.py"
mkdir $1; touch $src; chmod +x $src; cat > $src <<EOF
import requests
import os

cookies = {
    "session": os.environ.get("AOC_SESSION")
}

if __name__ == '__main__':
    raw_data = requests.get("https://adventofcode.com/2022/day/$1/input")
EOF