#! /bin/bash
# provide either relative or absolute path (relative from the dir where the script is called) 
input_file="input.txt"

A=$(ls -d */)
for dir in $A
do
    sed "/requests/s/^/#/" -i "$dir"aoc.py
    sed -e "/raw_data = requests.*/a \    with open(\"$input_file\", 'r') as file:\n        raw_data = file.read()\n" -i "$dir"aoc.py
    sed "/raw_data.text/s/text.//" -i "$dir"aoc.py
done