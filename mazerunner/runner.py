from maze import get_walls, get_dimensions
DIRECTIONS = ['N', 'E', 'S', 'W'] # North, East, South, West


def create_runner(x: int = 0, y: int = 0, orientation: str = 'N'):
    """
    Create a runner
    param x: The x position in the grid
    param y: The y position in the grid
    param orientation: Which direction the runner is facing
    return: The runner's position as coordinates and orientation
    """
    return {'position': (x, y), 'orientation': orientation}

def get_x(runner) -> int:
    """
    Get the x position of the runner
    param runner: The runner including position and orientation
    return: The x position of the runner
    """
    return runner['position'][0]

def get_y(runner) -> int:
    """
    Get the y position of the runner
    param runner: The runner including position and orientation
    return: The y position of the runner
    """
    return runner['position'][1]

def get_orientation(runner) -> str:
    """
    Get the orientation of the runner
    param runner: The runner including position and orientation
    return: The runner's orientation
    """
    return runner['orientation']

def turn(runner, direction: str) -> str:
    """
    Turn the runner on the given direction
    param runner: The runner including position and orientation
    param direction: Either Left or Right
    return: Runner with new direction
    """
    current_orientation = DIRECTIONS.index(runner["orientation"])

    if direction == "Left":
        new_index = (current_orientation - 1) % len(DIRECTIONS)
    elif direction == "Right":
        new_index = (current_orientation + 1) % len(DIRECTIONS)

    runner["orientation"] = DIRECTIONS[new_index]
    return runner

def forward(runner):
    """
    Move the runner forward one cell in the given direction
    param runner: The runner including position and orientation
    return: The runner having moved forward one cell
    """
    x, y = runner["position"]
    if runner["orientation"] == "N":
        runner["position"] = (x, y + 1)
    elif runner["orientation"] == "E":
        runner["position"] = (x + 1, y)
    elif runner["orientation"] == "S":
        runner["position"] = (x, y - 1)
    elif runner["orientation"] == "W":
        runner["position"] = (x - 1, y)
    return runner

def sense_walls(runner, maze) -> tuple:
    x, y = runner["position"]
    orientation = runner["orientation"]
    walls = get_walls(maze, x, y)

    if orientation == "N":
        return walls[3], walls[0], walls[1]  # Left: West, Front: North, Right: East
    elif orientation == "E":
        return walls[0], walls[1], walls[2]  # Left: North, Front: East, Right: South
    elif orientation == "S":
        return walls[1], walls[2], walls[3]  # Left: East, Front: South, Right: West
    elif orientation == "W":
        return walls[2], walls[3], walls[0]  # Left: South, Front: West, Right: North


def go_straight(runner: dict, maze: list) -> dict:
    left, front, right = sense_walls(runner, maze)
    if front:
        raise ValueError("Cannot move forward. There is a wall in front.")
    return forward(runner)


def move(runner: dict, maze: list) -> tuple:
    left, front, right = sense_walls(runner, maze)

    if not left:
        turn(runner, "Left")
        return forward(runner), "LF"  # Turn Left, Go Forward
    elif not front:
        return forward(runner), "F"  # Go Forward
    elif not right:
        turn(runner, "Right")
        return forward(runner), "RF"  # Turn Right, Go Forward
    else:
        turn(runner, "Left")
        turn(runner, "Left")  # Turn around
        return forward(runner), "LF"  # Turn Left twice, Go Forward


def explore(runner: dict, maze: list, goal: tuple = None) -> str:
    width, height = get_dimensions(maze)
    if goal is None:
        goal = (width - 1, 0)  # Default goal: top-right corner

    actions = ""

    while runner["position"] != goal:
        runner, action = move(runner, maze)
        actions += action

    return actions


def print_maze(maze: list, runner: dict) -> None:
    width, height = len(maze), len(maze[0])
    directions = {"N": "^", "E": ">", "S": "v", "W": "<"}
    runner_x, runner_y = runner["position"]
    runner_icon = directions[runner["orientation"]]

    print("#" * (2 * width + 3))

    for y in range(height):
        row = "#"
        for x in range(width):
            if (x, y) == (runner_x, runner_y):
                row += runner_icon
            else:
                row += "."
            if x < width - 1 and get_walls(maze, x, y)[1]:  # East wall
                row += "#"
            else:
                row += "."
        row += "#"
        print(row)

        if y < height - 1:
            row = "#"
            for x in range(width):
                if get_walls(maze, x, y)[2]:  # South wall
                    row += "#."
                else:
                    row += ".."
            row = row[:-1] + "#"
            print(row)

    print("#" * (2 * width + 3))

#Some implementations for testing
new_runner = create_runner(3,2,"E")
turn(new_runner, "Left")
forward(new_runner)
print(new_runner)