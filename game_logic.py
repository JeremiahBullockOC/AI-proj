import pygame
import time
from config import *
from path_planning import *
from user_choices import Choices


# Initialize pygame
pygame.init()
pygame.font.init()

# Define the font
font = pygame.font.SysFont(FONT, FONT_SIZE)

class Game:
    def __init__(self):
        choice = Choices()
        choice.run() 

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

        global automated


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
        else:
            self.usedMaze = maze
            self.usedWidth = len(maze[0])
            self.usedHeight = len(maze)

        # Editing window height
        self.windowWidth = GRID_SIZE * self.usedWidth
        self.windowHeight = GRID_SIZE * self.usedHeight
        self.destinationPos = (self.usedWidth-1, self.usedHeight-1)

        # Checking if path assisted and what algorithm


        if(self.control.casefold() == 'automated'):
            self.automated = True
        else:
            self.automated = False

        if(self.algorithm.casefold() == ''):
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

    def moveUp(self):
        new_pos = (self.agent_pos[0], self.agent_pos[1] - 1)
        if new_pos[1] >= 0 and not self.usedMaze[new_pos[1]][new_pos[0]]:
            self.agent_pos = new_pos

    def moveDown(self):
        new_pos = (self.agent_pos[0], self.agent_pos[1] + 1)
        if new_pos[1] < self.usedHeight and not self.usedMaze[new_pos[1]][new_pos[0]]:
            self.agent_pos = new_pos
    def moveRight(self):
        new_pos = (self.agent_pos[0] + 1, self.agent_pos[1])
        if new_pos[0] < self.usedWidth and not self.usedMaze[new_pos[1]][new_pos[0]]:
            self.agent_pos = new_pos
    def moveLeft(self):
        new_pos = (self.agent_pos[0] - 1, self.agent_pos[1])
        if new_pos[0] >= 0 and not self.usedMaze[new_pos[1]][new_pos[0]]:
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
                if self.destinationPos[0] == x and self.destinationPos[1] == y:
                    if self.destinationPos[0] < 0 or self.destinationPos[0] >= self.usedWidth or self.destinationPos[1] < 0 or self.destinationPos[1] >= self.usedHeight:
                        continue
                    pygame.draw.circle(self.screen, self.destinationColor, rect.center, GRID_SIZE // 2)
                if (x, y) == self.destinationPos and (x, y) == self.agent_pos:
                    text = font.render('Bazingga!', True, PURPLE)
                    text_rect = text.get_rect(center=self.screen.get_rect().center)
                    self.screen.blit(text, text_rect)


        if(self.automated or self.assisted):
             # Find the path from the agent to the goal grid
            path = astar(self.usedMaze, self.agent_pos, self.destinationPos)

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

        if(self.automated):
            self.agent_pos = path[1]
            time.sleep(0.2)

    def run(self):
        while self.running:
            # Handle events
            self.handle_events()

            # Draw the game
            self.draw()

        # Quit pygame
        pygame.quit()
