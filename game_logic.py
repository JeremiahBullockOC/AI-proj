import pygame
from config import *
from path_planning import *
from user_choices import Choices

# Initialize pygame
pygame.init()
pygame.font.init()

global agentColor
global backgroundColor
global wallColor
global gridColor
global pathColor
global destinationColor
global usedMaze
global usedWidth
global usedHeight
global windowWidth
global windowHeight
global assisted
global destinationPos

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
        self.screen = pygame.display.set_mode((windowWidth, windowHeight))
        pygame.display.set_caption("My Game: Running")

        # Define the agent starting position
        self.agent_pos = AGENT_POS

        # Define the game loop
        self.running = True



    def handle_choices(self):
        global agentColor
        global backgroundColor
        global wallColor
        global gridColor
        global pathColor
        global destinationColor
        global usedMaze
        global usedWidth
        global usedHeight
        global windowWidth
        global windowHeight
        global assisted
        global destinationPos

        if(self.theme.casefold() == 'ocean'):
            agentColor = OCEAN_AGENT
            backgroundColor = OCEAN_BACKGROUND
            wallColor = OCEAN_WALL
            gridColor = OCEAN_GRID
            pathColor = OCEAN_PATH
            destinationColor = OCEAN_DESTINATION
        elif(self.theme.casefold() == 'basic'):
            agentColor = BASIC_AGENT
            backgroundColor = BASIC_BACKGROUND
            wallColor = BASIC_WALL
            gridColor = BASIC_GRID
            pathColor = BASIC_PATH
            destinationColor = BASIC_DESTINATION
        elif(self.theme.casefold() == 'retro'):
            agentColor = RETRO_AGENT
            backgroundColor = RETRO_BACKGROUND
            wallColor = RETRO_WALL
            gridColor = RETRO_GRID
            pathColor = RETRO_PATH
            destinationColor = RETRO_DESTINATION

        if(self.maze_size.casefold() == 'small'):
            usedMaze = maze
            usedWidth = len(maze[0])
            usedHeight = len(maze)        
        elif(self.maze_size.casefold() == 'big'):
            usedMaze = big_maze
            usedWidth = len(big_maze[0])
            usedHeight = len(big_maze)   

        windowWidth = GRID_SIZE * usedWidth
        windowHeight = GRID_SIZE * usedHeight
        destinationPos = (usedWidth-1, usedHeight-1)

        if(self.algorithm.casefold == ''):
            assisted = False
        else:
            assisted = True


    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_UP:
                    new_pos = (self.agent_pos[0], self.agent_pos[1] - 1)
                    if new_pos[1] >= 0 and not usedMaze[new_pos[1]][new_pos[0]]:
                        self.agent_pos = new_pos
                elif event.key == pygame.K_DOWN:
                    new_pos = (self.agent_pos[0], self.agent_pos[1] + 1)
                    if new_pos[1] < usedHeight and not usedMaze[new_pos[1]][new_pos[0]]:
                        self.agent_pos = new_pos
                elif event.key == pygame.K_LEFT:
                    new_pos = (self.agent_pos[0] - 1, self.agent_pos[1])
                    if new_pos[0] >= 0 and not usedMaze[new_pos[1]][new_pos[0]]:
                        self.agent_pos = new_pos
                elif event.key == pygame.K_RIGHT:
                    new_pos = (self.agent_pos[0] + 1, self.agent_pos[1])
                    if new_pos[0] < usedWidth and not usedMaze[new_pos[1]][new_pos[0]]:
                        self.agent_pos = new_pos

    # Add this method to the Game class
    def draw_path(self, path):
        if path is not None:
            for i in range(len(path) - 1):
                x1, y1 = path[i]
                x2, y2 = path[i + 1]
                rect1 = pygame.Rect(x1 * GRID_SIZE, y1 * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                rect2 = pygame.Rect(x2 * GRID_SIZE, y2 * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                pygame.draw.line(self.screen, pathColor, rect1.center, rect2.center, 10)

    def draw(self):
        # Draw the grid
        self.screen.fill(backgroundColor)
        for y in range(usedHeight):
            for x in range(usedWidth):
                rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                pygame.draw.rect(self.screen, gridColor, rect, 1)
                if usedMaze[y][x] == 1:
                    pygame.draw.rect(self.screen, wallColor, rect)
                if destinationPos[0] == x and destinationPos[1] == y:
                    if destinationPos[0] < 0 or destinationPos[0] >= usedWidth or destinationPos[1] < 0 or destinationPos[1] >= usedHeight:
                        continue
                    pygame.draw.circle(self.screen, destinationColor, rect.center, GRID_SIZE // 2)
                if (x, y) == destinationPos and (x, y) == self.agent_pos:
                    text = font.render('Bazingga!', True, PURPLE)
                    text_rect = text.get_rect(center=self.screen.get_rect().center)
                    self.screen.blit(text, text_rect)


        if(assisted):
             # Find the path from the agent to the goal grid
            path = astar(usedMaze, self.agent_pos, destinationPos)

            # Draw the path
            self.draw_path(path)

        # Draw the agent
        agent_rect = pygame.Rect(self.agent_pos[0] * GRID_SIZE, self.agent_pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        if self.agent_pos[0] < 0 or self.agent_pos[0] >= usedWidth or self.agent_pos[1] < 0 or self.agent_pos[1] >= usedHeight:
            pass
        else:
            pygame.draw.circle(self.screen, agentColor, agent_rect.center, GRID_SIZE // 2)

        # Update the screen
        pygame.display.flip()

    def run(self):
        while self.running:
            # Handle events
            self.handle_events()

            # Draw the game
            self.draw()

        # Quit pygame
        pygame.quit()
