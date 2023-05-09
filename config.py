# Define the maze layout
maze = [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]

# Define the grid size and the window size
GRID_SIZE = 50
GRID_WIDTH = len(maze[0])
GRID_HEIGHT = len(maze)
WIDTH, HEIGHT = GRID_WIDTH * GRID_SIZE, GRID_HEIGHT * GRID_SIZE

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Define the agent starting position
AGENT_POS = (0, 0)

# Define the goal position
GOAL_POS = (GRID_WIDTH-1, GRID_HEIGHT-1)

# Define the font
FONT = 'Comic Sans MS'
FONT_SIZE = 50
