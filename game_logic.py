import pygame
import time
from config import *
from path_planning import *
from user_choices import Choices
from asp import *


# Initialize pygame
pygame.init()

# Define the font

class Game:
    def __init__(self):
        choice = Choices()
        choice.run() 

        pygame.font.init()
        self.font = pygame.font.SysFont(FONT, FONT_SIZE)

        self.visited = set()
        
        # Get user choices
        self.theme = choice.getTheme()
        self.control = choice.getControl()
        self.algorithm = choice.getAlgorithm()
        self.maze_size = choice.getMaze()
        

        self.handle_choices()


        # Set up the screen
        self.screen = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        pygame.display.set_caption("My Game: Running")

        # Define the agent starting position
        self.agent_pos = AGENT_POS

        # Define the game loop
        self.running = True



    def handle_choices(self):


        if(self.theme.casefold() == 'ocean'):
            self.agentColor = OCEAN_AGENT
            self.backgroundColor = OCEAN_BACKGROUND
            self.wallColor = OCEAN_WALL
            self.gridColor = OCEAN_GRID
            self.pathColor = OCEAN_PATH
            self.destinationColor = OCEAN_DESTINATION
        elif(self.theme.casefold() == 'retro'):
            self.agentColor = RETRO_AGENT
            self.backgroundColor = RETRO_BACKGROUND
            self.wallColor = RETRO_WALL
            self.gridColor = RETRO_GRID
            self.pathColor = RETRO_PATH
            self.destinationColor = RETRO_DESTINATION
        else:
            self.agentColor = BASIC_AGENT
            self.backgroundColor = BASIC_BACKGROUND
            self.wallColor = BASIC_WALL
            self.gridColor = BASIC_GRID
            self.pathColor = BASIC_PATH
            self.destinationColor = BASIC_DESTINATION

        # Setting mazes        
        if(self.maze_size.casefold() == 'big'):
            self.usedMaze = big_maze
            self.usedWidth = len(big_maze[0])
            self.usedHeight = len(big_maze)
        elif(self.maze_size.__contains__('random')):
            if(self.maze_size.__contains__('big')):
                self.usedMaze, self.destinationPos = gen_double_maze(20, 20)
            else:
                self.usedMaze, self.destinationPos = gen_double_maze(10, 10)
            self.usedWidth = len(self.usedMaze[0])
            self.usedHeight = len(self.usedMaze)
        else:
            self.usedMaze = maze
            self.usedWidth = len(maze[0])
            self.usedHeight = len(maze)
        if(not self.maze_size.__contains__('random')):
            self.destinationPos = (self.usedWidth-1, self.usedHeight-1)
        self.usedMaze = solve_nqueens(self.usedMaze, self.destinationPos)
        for row in self.usedMaze:
            for cell in row:
                    print('#' if cell else ' ', end='')
            print()
        # Editing window height
        self.windowWidth = GRID_SIZE * self.usedWidth
        self.windowHeight = GRID_SIZE * self.usedHeight


        # Checking if path assisted and what algorithm


        if(self.control.casefold() == 'automated'):
            self.automated = True
        else:
            self.automated = False

        if(self.algorithm.casefold() == 'unassisted'):
            self.assisted = False
        else:
            self.assisted = True

    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

                if(self.automated == False):
                    if event.key == pygame.K_UP:
                        self.moveUp()
                    elif event.key == pygame.K_DOWN:
                        self.moveDown()
                    elif event.key == pygame.K_LEFT:
                        self.moveLeft()
                    elif event.key == pygame.K_RIGHT:
                        self.moveRight()

    # Add this method to the Game class
    def draw_path(self, path):
        if path is not None:
            for i in range(len(path) - 1):
                x1, y1 = path[i]
                x2, y2 = path[i + 1]
                rect1 = pygame.Rect(x1 * GRID_SIZE, y1 * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                rect2 = pygame.Rect(x2 * GRID_SIZE, y2 * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                pygame.draw.line(self.screen, self.pathColor, rect1.center, rect2.center, 10)

    def validMove(self, new_pos):
        is_valid = self.usedMaze[new_pos[1]][new_pos[0]] == 0 or self.usedMaze[new_pos[1]][new_pos[0]] == 2
        return is_valid

    def moveUp(self):
        new_pos = (self.agent_pos[0], self.agent_pos[1] - 1)
        if new_pos[1] >= 0 and self.validMove(new_pos):
            self.agent_pos = new_pos

    def moveDown(self):
        new_pos = (self.agent_pos[0], self.agent_pos[1] + 1)
        if new_pos[1] < self.usedHeight and self.validMove(new_pos):
            self.agent_pos = new_pos
    def moveRight(self):
        new_pos = (self.agent_pos[0] + 1, self.agent_pos[1])
        if new_pos[0] < self.usedWidth and self.validMove(new_pos):
            self.agent_pos = new_pos
    def moveLeft(self):
        new_pos = (self.agent_pos[0] - 1, self.agent_pos[1])
        if new_pos[0] >= 0 and self.validMove(new_pos):
            self.agent_pos = new_pos
    
    def draw(self):
        # Draw the grid
        self.screen.fill(self.backgroundColor)
        for y in range(self.usedHeight):
            for x in range(self.usedWidth):
                rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                pygame.draw.rect(self.screen, self.gridColor, rect, 1)
                if self.usedMaze[y][x] == 1:
                    pygame.draw.rect(self.screen, self.wallColor, rect)
                elif self.usedMaze[y][x] == 2:
                    # self.screen.blit(PIT_IMAGE, rect)
                    pygame.draw.rect(self.screen, self.wallColor, rect)
                    pygame.draw.circle(self.screen, self.backgroundColor, rect.center, GRID_SIZE // 2)

                if self.destinationPos[0] == x and self.destinationPos[1] == y:
                    if self.destinationPos[0] < 0 or self.destinationPos[0] >= self.usedWidth or self.destinationPos[1] < 0 or self.destinationPos[1] >= self.usedHeight:
                        continue
                    pygame.draw.circle(self.screen, self.destinationColor, rect.center, GRID_SIZE // 2)
                if (x, y) == self.destinationPos and (x, y) == self.agent_pos:
                    text = self.font.render('Bazingga!', True, PURPLE)
                    text_rect = text.get_rect(center=self.screen.get_rect().center)
                    self.screen.blit(text, text_rect)


        if(self.automated or self.assisted):

             # Find the path from the agent to the goal grid
            if(self.algorithm == 'astar'):
                path = astar(self.usedMaze, self.agent_pos, self.destinationPos)
            elif(self.algorithm == 'dfs'):
                path = dfs(self.usedMaze, self.agent_pos, self.destinationPos, self.visited)
            elif(self.algorithm == 'bfs'):
                path = bfs(self.usedMaze, self.agent_pos, self.destinationPos)
            elif(self.algorithm == 'ucs'):
                path = ucs(self.usedMaze, self.agent_pos, self.destinationPos)
            # Draw the path
            self.draw_path(path)


        # Draw the agent
        agent_rect = pygame.Rect(self.agent_pos[0] * GRID_SIZE, self.agent_pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        if self.agent_pos[0] < 0 or self.agent_pos[0] >= self.usedWidth or self.agent_pos[1] < 0 or self.agent_pos[1] >= self.usedHeight:
            pass
        else:
            pygame.draw.circle(self.screen, self.agentColor, agent_rect.center, GRID_SIZE // 2)

        # Update the screen
        pygame.display.flip()

        if(self.automated and self.agent_pos != self.destinationPos):
            self.visited.add(self.agent_pos)
            self.agent_pos = path[1] 
            time.sleep(0.2)

    def handle_map_events(self):
        if self.usedMaze[self.agent_pos[1]][self.agent_pos[0]] > 1:
            if self.usedMaze[self.agent_pos[1]][self.agent_pos[0]] == 2:
                self.agent_pos = AGENT_POS
                self.draw()

    def run(self):
        while self.running:
            # Handle events
            self.handle_events()

            # Draw the game
            self.draw()

            # Handle pits, chests and traps etc.
            self.handle_map_events()
        # Quit pygame
        pygame.quit()
