import random

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
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
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
     return expand_maze(generate_maze(width//2, height//2), width, height)

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
    
    return genmaze

def expand_maze(maze, width, height):
        newmaze = [[1] * width for _ in range(height)]

        for row_index, row in enumerate(maze):
                for col_index, cell in enumerate(row):
                    newmaze[col_index * 2][row_index * 2] = cell
                    newmaze[col_index * 2 + 1][row_index * 2] = cell
                    newmaze[col_index * 2][row_index * 2 + 1] = cell
                    newmaze[col_index * 2 + 1][row_index * 2 + 1] = cell

        return newmaze



# def generate_maze(width, height, start):
#     # Initialize the maze grid
#     genmaze = [[1] * width for _ in range(height)]
    
#     # Set starting and ending points
#     start_x, start_y = start
#     end = 0,0
#     genmaze[start_y][start_x] = 0
    
#     # Recursive function to carve the maze
#     def carve_maze(x, y):
#         directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
#         random.shuffle(directions)
        
#         for dx, dy in directions:
#             nx, ny = x + dx, y + dy
#             mx, my = x + 2 * dx, y + 2 * dy
#             if mx >= 0 and mx < width and my >= 0 and my < height:
#                 if genmaze[my][mx] == 1:
#                     genmaze[my][mx] = 0
#                     genmaze[ny][nx] = 0
#                     nonlocal end
#                     end = nx, ny
#                     carve_maze(nx, ny)
    
#     # Start carving the maze
#     carve_maze(start_x, start_y)
    
#     return genmaze

