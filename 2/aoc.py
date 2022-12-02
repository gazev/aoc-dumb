import requests

cookies = {
    "session": ""
}

def first(data: str) -> int:
    total = 0
    for line in data:
        player_play = ord(line[2]) - ord("X")
        elf_play = ord(line[0]) - ord("A")

        if player_play == elf_play:
            total +=  3 
        elif player_play == (elf_play + 1) % 3:
            total += 6 
        else:
            total += 0

        total += player_play + 1
    
    return total
    
def second(data: str) -> int:
    total = 0
    for line in data:
        outcome = ord(line[2]) - ord("X")
        elf_play = ord(line[0]) - ord("A")
        player_play = 0

        if outcome == 1:                        # Draw
            total += 3
            player_play = elf_play
        elif outcome == 2:                      # Win
            total += 6
            player_play = (elf_play + 1) % 3
        else:                                   # Lose
            total += 0
            player_play = (elf_play - 1) % 3
        
        total += player_play + 1
    
    return total

if __name__ == '__main__':
    raw_data = requests.get("https://adventofcode.com/2022/day/2/input", cookies=cookies)
    data = raw_data.text.strip("\n").split("\n")

    print(first(data), second(data))