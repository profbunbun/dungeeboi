import random

# Define dungeon dimensions (m x n)
m = 20
n = 20

def generate_dungeon(m, n):
    # Initialize the dungeon grid with walls
    dungeon = [['#'] * (2 * n + 1) for _ in range(2 * m + 1)]

    def carve(x, y):
        dungeon[y][x] = ' '
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(directions)

        for dx, dy in directions:
            new_x, new_y = x + dx * 2, y + dy * 2
            if 0 <= new_x < 2 * n and 0 <= new_y < 2 * m and dungeon[new_y][new_x] == '#':
                dungeon[y + dy][x + dx] = ' '  # Carve path between cells
                carve(new_x, new_y)  # Recursively carve from the new cell

                # Optionally, randomly create rooms adjacent to the carved path
                if random.random() < 0.1:  # 10% chance to create a room
                    room_width, room_height = random.randint(2, 4), random.randint(2, 4)
                    for rw in range(room_width):
                        for rh in range(room_height):
                            room_x, room_y = new_x + rw, new_y + rh
                            if 0 <= room_x < 2 * n and 0 <= room_y < 2 * m:
                                dungeon[room_y][room_x] = ' '

    # Start carving from a random point
    start_x, start_y = random.randint(0, n - 1) * 2 + 1, random.randint(0, m - 1) * 2 + 1
    carve(start_x, start_y)

    # Initialize player position
    player_x, player_y = start_x, start_y
    dungeon[player_y][player_x] = 'I'  # Mark the player's initial position

    # Randomly place stairs
    stairs_x, stairs_y = random.randint(0, n - 1) * 2 + 1, random.randint(0, m - 1) * 2 + 1
    dungeon[stairs_y][stairs_x] = 'S'

    return dungeon

def save_dungeon_to_file(dungeon, filename):
    with open(filename, 'w') as file:
        file.write(f"{len(dungeon[0])} {len(dungeon)}\n")
        for row in dungeon:
            file.write(''.join(row) + '\n')

if __name__ == "__main__":
    dungeon = generate_dungeon(m, n)
    filename = "dungeon.txt"
    save_dungeon_to_file(dungeon, filename)
    print(f"Dungeon saved to {filename}")