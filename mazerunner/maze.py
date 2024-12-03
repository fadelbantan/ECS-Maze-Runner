from typing import Tuple, List


def create_maze(width: int, height: int) -> List[List[Tuple[bool, bool, bool, bool]]]:
    return [[(False, False, False, False) for _ in range(height)] for _ in range(width)]


def get_dimensions(maze: List[List[Tuple[bool, bool, bool, bool]]]) -> Tuple[int, int]:
    width = len(maze)
    height = len(maze[0]) if width > 0 else 0
    return width, height


def get_walls(maze: List[List[Tuple[bool, bool, bool, bool]]], x: int, y: int) -> Tuple[bool, bool, bool, bool]:
    return maze[x][y]


def add_horizontal_wall(maze: List[List[Tuple[bool, bool, bool, bool]]], x: int, y: int) -> List[List[Tuple[bool, bool, bool, bool]]]:

    # Get the current cell and set the South wall
    current = maze[x][y]
    maze[x][y] = (current[0], current[1], True, current[3])

    # Update the cell below, if it exists
    if y + 1 < len(maze[0]):
        below = maze[x][y + 1]
        maze[x][y + 1] = (True, below[1], below[2], below[3])

    return maze

def add_vertical_wall(maze: List[List[Tuple[bool, bool, bool, bool]]], x: int, y: int) -> List[List[Tuple[bool, bool, bool, bool]]]:
    current = maze[x][y]
    maze[x][y] = (current[0], current[1], current[2], True)  # Set West wall for (x, y)

    # Update East wall of the left cell if it exists
    if x > 0:
        left_cell = maze[x - 1][y]
        maze[x - 1][y] = (left_cell[0], True, left_cell[2], left_cell[3])

    return maze