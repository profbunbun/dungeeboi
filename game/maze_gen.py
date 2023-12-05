import random

# Define dungeon dimensions (m x n)
m = 20
n = 20
num_floors = 5  # Total number of floors

def generate_floor(m, n, floor_num, num_floors):
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

    # Initialize player position if it's the first floor
    if floor_num == 0:
        dungeon[start_y][start_x] = 'I'

    # Place stairs
    if floor_num < num_floors - 1:
        # Place upstairs on all floors except the last
        up_stairs_x, up_stairs_y = random.randint(0, n - 1) * 2 + 1, random.randint(0, m - 1) * 2 + 1
        dungeon[up_stairs_y][up_stairs_x] = 'U'
    
    if floor_num > 0:
        # Place downstairs on all floors except the first
        down_stairs_x, down_stairs_y = random.randint(0, n - 1) * 2 + 1, random.randint(0, m - 1) * 2 + 1
        dungeon[down_stairs_y][down_stairs_x] = 'D'

    return dungeon

def generate_dungeons(m, n, num_floors):
    return [generate_floor(m, n, i, num_floors) for i in range(num_floors)]

def save_dungeons_to_files(dungeons, base_filename):
    for i, dungeon in enumerate(dungeons):
        filename = f"{base_filename}_floor_{i + 1}.txt"
        with open(filename, 'w') as file:
            file.write(f"{len(dungeon[0])} {len(dungeon)}\n")
            for row in dungeon:
                file.write(''.join(row) + '\n')
        print(f"Dungeon floor {i + 1} saved to {filename}")

if __name__ == "__main__":
    dungeons = generate_dungeons(m, n, num_floors)
    base_filename = "dungeon"
    save_dungeons_to_files(dungeons, base_filename)
