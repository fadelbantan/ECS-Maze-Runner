DIRECTIONS = ['N', 'E', 'S', 'W'] # North, East, South, West


def create_runner(x: int = 0, y: int = 0, orientation: str = 'N'):
    """
    Create a runner
    :param x: The x position in the grid
    :param y: The y position in the grid
    :param orientation: Which direction the runner is facing
    :return: The runner's position as coordinates and orientation
    """
    return {'position': (x, y), 'orientation': orientation}

def get_x(runner) -> int:
    """
    Get the x position of the runner
    :param runner: The runner including position and orientation
    :return: The x position of the runner
    """
    return runner['position'][0]

def get_y(runner) -> int:
    """
    Get the y position of the runner
    :param runner: The runner including position and orientation
    :return: The y position of the runner
    """
    return runner['position'][1]

def get_orientation(runner) -> str:
    """
    Get the orientation of the runner
    :param runner: The runner including position and orientation
    :return: The runner's orientation
    """
    return runner['orientation']

def turn(runner, direction: str) -> str:
    """
    Turn the runner on the given direction
    :param runner: The runner including position and orientation
    :param direction: Either Left or Right
    :return: Runner with new direction
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
    :param runner: The runner including position and orientation
    :return: The runner having moved forward one cell
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

#Some implementations for testing
new_runner = create_runner(3,2,"E")
turn(new_runner, "Left")
forward(new_runner)
print(new_runner)