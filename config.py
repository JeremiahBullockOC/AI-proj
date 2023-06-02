import random
from path_planning import astar

# Define the maze layout
maze = [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]

big_maze = [[0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0]]

# Define the grid size and the window size
GRID_SIZE = 35
GRID_WIDTH = len(maze[0])
GRID_HEIGHT = len(maze)
WIDTH, HEIGHT = GRID_WIDTH * GRID_SIZE, GRID_HEIGHT * GRID_SIZE

CHOICES_WIDTH, CHOICES_HEIGHT = 500, 600

PURPLE = (150, 0, 128)


# Define the colors

#BASIC - Black background, white grid, grey obstacle, yellow player, purple path, blue destination
BASIC_BACKGROUND = (0, 0, 0)
BASIC_GRID = (255, 255, 255)
BASIC_WALL = (128, 128, 128)
BASIC_PATH = (128, 0, 128)
BASIC_AGENT = (255, 255, 0)
BASIC_DESTINATION = (0, 0, 255)


#RETRO - Black background, Green grid, Red Walls, Orange Player, Light Blue Path, White Destination
RETRO_BACKGROUND = (0, 0, 0)
RETRO_GRID = (57, 255, 20)
RETRO_AGENT = (224,231,34)
RETRO_PATH = (4, 217, 255)
RETRO_WALL = (255, 0, 0)
RETRO_DESTINATION = (255, 255, 255)

#OCEAN - Deep blue background, Light blue grid, Deep grey blue Walls, Soft Pink Player, Light Blue Path, White Path, Seafoam Green Destination
OCEAN_BACKGROUND = (0, 65, 81)
OCEAN_GRID = (185,241,254)
OCEAN_AGENT = (255,184,191)
OCEAN_PATH = (242,252,254)
OCEAN_WALL = (3,38,45)
OCEAN_DESTINATION = (159, 226, 191)

# Define the agent starting position
AGENT_POS = (0, 0)

# Define the goal position
GOAL_POS = (GRID_WIDTH-1, GRID_HEIGHT-1)

# Define the font
FONT = 'Comic Sans MS'
FONT_SIZE = 50


def gen_double_maze(width, height):
     results = generate_maze(width//2, height//2)
     temp_maze, end_point = results
     actual_endpoint = end_point[0] * 2, end_point[1] * 2
     return expand_maze(temp_maze, width, height), actual_endpoint

def generate_maze(width, height):
    # Initialize the maze grid
    genmaze = [[1] * width for _ in range(height)]
    # Recursive function to carve the maze
    def carve_maze(x, y):
        genmaze[y][x] = 0
        
        directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx < width and ny >= 0 and ny < height:
                if genmaze[ny][nx] == 1:
                    mx, my = x + dx // 2, y + dy // 2
                    genmaze[my][mx] = 0
                    carve_maze(nx, ny)
    
    # Start carving the maze from a random starting point
    start_x = 0
    start_y = 0
    carve_maze(start_x, start_y)
    
    path = dfs_longest_path(genmaze, (0,0))
    end = path[-1]

    return genmaze, end

def expand_maze(maze, width, height):
        newmaze = [[1] * width for _ in range(height)]

        for row_index, row in enumerate(maze):
                for col_index, cell in enumerate(row):
                    newmaze[col_index * 2][row_index * 2] = cell
                    newmaze[col_index * 2 + 1][row_index * 2] = cell
                    newmaze[col_index * 2][row_index * 2 + 1] = cell
                    newmaze[col_index * 2 + 1][row_index * 2 + 1] = cell

        return newmaze

def dfs_longest_path(maze, start):
    stack = [(start, [start])]
    longest_path = []
    
    while stack:
        (x, y), path = stack.pop()
        if len(path) > len(longest_path):
            longest_path = path
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_x, next_y = x + dx, y + dy
            if 0 <= next_x < len(maze) and 0 <= next_y < len(maze[0]) and maze[next_x][next_y] == 0 and (next_x, next_y) not in path:
                stack.append(((next_x, next_y), path + [(next_x, next_y)]))
    
    return longest_path
