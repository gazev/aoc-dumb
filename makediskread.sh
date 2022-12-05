#! /bin/bash
# provide either relative or absolute path (relative from the dir where the script is called) 

if [ $# -lt 1 ]; then
    echo "Usage: $0 [aoc-day]"
    exit
fi


input_file="input.txt"

echo "$1"/aoc.py
sed -i "/requests/s/^/#/" "$1"/aoc.py
sed -e "/raw_data = requests.*/a \    with open(\"$input_file\", 'r') as file:\n        raw_data = file.read()\n" -i "$1"/aoc.py
sed "/raw_data.text/s/text.//" -i "$1"/aoc.py
echo "$1"/aoc.py
