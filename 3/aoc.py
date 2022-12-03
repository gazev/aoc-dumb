import requests

cookies = {
    "session": ""
}

# dynamic programming was useless here, but it still works
def lcs(s1: str, s2: str) -> str:
    m = len(s1)
    n = len(s2)
    dt = [[0]*(n + 1) for j in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dt[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                dt[i][j] = dt[i - 1][j - 1] + 1
            else:
                dt[i][j] = max(dt[i][j - 1], dt[i - 1][j])
    
    # at the point this was made,i could see strings would only have 1 character in common
    # even if the subsequence size is bigger than 2 (eg: "zz", "MM")
    # so my fear was accurate, this is useless, but we move forward
    i, j = m, n
    seq = ""
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            seq += s1[i - 1]
            i -= 1
            j -= 1
            break # only one in common, so we can cut some execution time 
        
        elif dt[i - 1][j] > dt[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return seq

if __name__ == '__main__':
    raw_data = requests.get("https://adventofcode.com/2022/day/3/input", cookies=cookies)
    data = raw_data.text.strip("\n").split("\n")

    total = 0
    for s in data:
        s1, s2 = [s[:len(s)//2], s[len(s)//2:]]
        seq = lcs(s1, s2)
        total += ord(seq) + ((- ord("a") + 1) if seq.islower() else (- ord("a") + 27))

    print(total)
    

    # i sweart i tried to apply DP, the LCS will not return all common characters,
    # changes to the second loop were required or a different PD algorithm
    # and i cant waste more time into this
    # here goes the good old O(n^3) pythonic solution 
    total = 0
    size = len(data)
    for i in range(0, size, 3):
        r = ""
        common_c = ""
        for c in data[i]:
            if c in data[i + 1]:
                common_c += c
            
        for c in common_c:
            if c in data[i + 2]:
                r = c
                break

        total += ord(r) + ((- ord("a") + 1) if r.islower() else (- ord("A") + 27))

    print(total)