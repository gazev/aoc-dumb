#! /bin/bash

src="$1/aoc.py"
mkdir $1; touch $src; chmod +x $src; cat > $src <<'EOF'
import requests

cookies = {
    "session": ""
}

if __name__ == '__main__':
    pass
EOF