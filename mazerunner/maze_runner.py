from typing import List, Tuple, Optional
from maze import get_walls, get_dimensions, create_maze, add_vertical_wall, add_horizontal_wall


def shortest_path(
    maze: List[List[Tuple[bool, bool, bool, bool]]],
    starting: Optional[Tuple[int, int]] = None,
    goal: Optional[Tuple[int, int]] = None
) -> List[Tuple[int, int]]:

    # Default starting and goal positions
    if starting is None:
        starting = (0, 0)  # Bottom-left corner
    if goal is None:
        width, height = get_dimensions(maze)
        goal = (width - 1, height - 1)  # Top-right corner

    # Initialize BFS
    queue = [(starting, [starting])]  # (current_position, path_so_far)
    visited = set()

    while queue:
        current_position, path = queue.pop(0)
        x, y = current_position

        # If we've reached the goal, return the path
        if current_position == goal:
            return path

        # Mark the current position as visited
        visited.add(current_position)

        # Get wall information at the current position
        walls = get_walls(maze, x, y)

        # Explore neighbors (North, East, South, West)
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # (dx, dy)
        for i, (dx, dy) in enumerate(directions):
            if not walls[i]:  # No wall in the direction
                neighbor = (x + dx, y + dy)
                if neighbor not in visited and 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]):
                    queue.append((neighbor, path + [neighbor]))

    # If no path is found, return an empty list
    return []

# Some implementation for testing
# Create a 5x5 maze
maze = create_maze(5, 5)

# Add some walls
add_horizontal_wall(maze, 2, 1)  # Add a horizontal wall below (2, 1)
add_vertical_wall(maze, 3, 2)    # Add a vertical wall to the left of (3, 2)

# Find the shortest path from (0, 0) to (4, 4)
path = shortest_path(maze, starting=(0, 0), goal=(4, 4))
print("Shortest Path:", path)