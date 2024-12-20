def find_word_in_all_directions(grid, word):
    rows = len(grid)
    if rows == 0:
        return 0
    cols = len(grid[0])
    counter = 0
    
    directions = [
        (0, 1),
        (0, -1),
        (-1, 0),
        (1, 0),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]
    
    def is_valid_position(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    def check_word(x, y, dx, dy):
        if not is_valid_position(x + dx * (len(word)-1), y + dy * (len(word)-1)):
            return False
            
        for i in range(len(word)):
            if grid[x + dx * i][y + dy * i] != word[i]:
                return False
        return True
    
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if check_word(i, j, dx, dy):
                    counter += 1
    
    return counter

counter = 0
grid = []

with open("adventday4.txt", "r") as file:
    for line in file:
        clean_line = line.strip().replace("\t", "")
        if clean_line:
            grid.append(clean_line)

total_occurrences = find_word_in_all_directions(grid, "XMAS")

print("First few lines of the grid:")
for line in grid[:5]:
    print(line)

print(f"\nThere are a total of {total_occurrences} XMASes.")
