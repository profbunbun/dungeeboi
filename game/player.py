class Player:
    def __init__(self, dungeon):
        self.dungeon = dungeon
        self.x, self.y = self.find_start()
        self.just_transported = False  # Initialize player's position to the start point

    def find_start(self):
        # Adjust to find the start position in the dungeon
        for y, row in enumerate(self.dungeon.dungeon):
            for x, cell in enumerate(row):
                if cell == 'I':  # Assuming 'S' is the start point
                    return x, y
        return 0, 0  # Default start position if 'S' is not found

    def find_stairs(self, stair_type):
        """Find the position of specified stairs ('U' or 'D') on the current floor."""
        for y, row in enumerate(self.dungeon.dungeon):
            for x, cell in enumerate(row):
                if cell == stair_type:
                    return x, y
        return None

    def can_move(self, dx, dy):
        new_x, new_y = self.x + dx, self.y + dy
        if 0 <= new_x < self.dungeon.n and 0 <= new_y < self.dungeon.m:
            # Check for walls and doors
            cell = self.dungeon.dungeon[new_y][new_x]
            if cell == '#':  # Wall
                return False
            elif cell == 'D':  # Door
                # Add logic here if you want specific interaction with doors
                return True
            return True  # Open path
        return False

    def move(self, dx, dy):
        if self.can_move(dx, dy):
            self.x += dx
            self.y += dy
            self.just_transported = False
    def reset_position(self):
        self.x, self.y = self.find_start()

    # Add any additional methods for dungeon-specific interactions
