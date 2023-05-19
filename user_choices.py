import pygame
import time

from config import *
from button import *

pygame.init()

# Choices state
global state

# This file is to hold and store all the choices that a user might make for a game. This will be passed to Game.py
# User choices
global control 
global algorithm 
global maze_size 
global theme 
global clicked

state = 'State 1'
control = ''
maze_size = ''
algorithm = ''
theme = ''
clicked = False


controlButtons = []
assistanceButtons = []
algorithmButtons = []
mazeButtons = []
themeButtons = []
returnButtons = []

class Choices:
    def __init__(self):
            # Set up the screen
            self.screen = pygame.display.set_mode((CHOICES_WIDTH, CHOICES_HEIGHT))
            pygame.display.set_caption("My Game: Choices")

            # Define the agent starting position

            # Define the game loop
            self.running = True

            self.automateButton = Button('Automated', 30, 30, 375, 80, 'Automated', lambda: self.controlClick(self.automateButton))
            self.manualButton = Button('Manual', 30, 130, 375, 80, 'Manual', lambda: self.controlClick(self.manualButton))
            self.astarButton = Button('astar', 30, 30, 375, 80, 'A* Algorithm', lambda: self.algoClick(self.astarButton))
            self.dfsButton = Button('dfs', 30, 130, 375, 80, 'DFS Algorithm', lambda: self.algoClick(self.dfsButton))
            self.bfsButton = Button('bfs', 30, 230, 375, 80, 'BFS Algorithm', lambda: self.algoClick(self.bfsButton))
            self.ucsButton = Button('ucs', 30, 330, 375, 80, 'UCS Algorithm', lambda: self.algoClick(self.ucsButton))
            self.returnButton = Button('', 30, 430, 375, 80, 'Return', lambda: self.returnFunc)
            self.assistedButton = Button('assisted', 30, 30, 375, 80, 'Path Assisted', lambda: self.assistClick(self.assistedButton))
            self.unassistedButton = Button('unassisted', 30, 130, 375, 80, 'No Assistance', lambda: self.assistClick(self.unassistedButton))
            self.basicButton = Button('basic', 30, 30, 375, 80, 'Basic Theme', lambda: self.themeClick(self.basicButton))
            self.retroButton = Button('retro', 30, 130, 375, 80, 'Retro Theme', lambda: self.themeClick(self.retroButton))
            self.oceanButton = Button('ocean', 30, 230, 375, 80, 'Ocean Theme', lambda: self.themeClick(self.oceanButton))
            self.smallMazeButton = Button('small maze', 30, 30, 375, 80, 'Small Maze', lambda: self.mazeClick(self.smallMazeButton))
            self.smallRandomMazeButton = Button('small random maze', 30, 130, 375, 80, 'Small Random Maze', lambda: self.mazeClick(self.smallRandomMazeButton))
            self.bigMazeButton = Button('big maze', 30, 230, 375, 80, 'Big Maze', lambda: self.mazeClick(self.bigMazeButton))
            self.bigRandomMazeButton = Button('big random maze', 30, 330, 375, 80, 'Big Random Maze', lambda: self.mazeClick(self.bigRandomMazeButton))

            controlButtons.extend([self.automateButton, self.manualButton])
            assistanceButtons.extend([self.assistedButton, self.unassistedButton])
            algorithmButtons.extend([self.astarButton, self.dfsButton, self.bfsButton, self.ucsButton])
            mazeButtons.extend([self.smallMazeButton, self.smallRandomMazeButton, self.bigMazeButton, self.bigRandomMazeButton])
            themeButtons.extend([self.basicButton, self.retroButton, self.oceanButton])
            
            # TODO Fix the return function
            #returnButtons.append(self.returnButton)
    def returnFunc(self):
        global state
        global clicked
        clicked = True
        if state.casefold() == 'state 2' or state.casefold() == 'state 2a' or state.casefold() == 'state 2b':
            state = 'State 1'
        elif state.casefold() == 'state 2b_1':
            state = 'state 2b'
        elif state.casefold() == 'state 3':
            if control.casefold() == 'automated':
                state = 'state 2a'
            elif algorithm.casefold() == 'unassisted':
                state = 'state 2b'
            else:
                state = 'state 2b_1'
        elif state.casefold() == 'state 4':
            state = 'State 3'

            
    # Automated or manual
        # If automated pause for a slight moment after each movement so user can see initial state.
    def controlClick(self, button):
        global control
        global state
        global clicked
        clicked = True

        control = button.buttonVal
        if control.casefold() == 'automated':
            if state.casefold() == 'state 1':
                state = 'State 2a'
        else:
            if state.casefold() == 'state 1':
                state = 'State 2b'


    # Assisted or Unassisted
        # If assisted navigate to algorithm of choice
    def assistClick(self, button):
        global algorithm
        global state


        if button.buttonVal.casefold() == 'assisted':
            if state.casefold() == 'state 2b':
                state = 'State 2b_1'
        elif button.buttonVal.casefold() == 'unassisted':
            algorithm = 'Unassisted'
            if state.casefold() == 'state 2b':
                state = 'State 3'

    # Alogrithm of choice
        # A*
        # DFS
        # UCS
        # Not sure how much difference the user will see
    def algoClick(self, button):
        global algorithm
        global clicked
        clicked = True
        if button.buttonVal.casefold() == 'astar':
            algorithm = 'astar'
        elif button.buttonVal.casefold() == 'dfs':
            algorithm = 'dfs'
        elif button.buttonVal.casefold() == 'bfs':
            algorithm = 'bfs'
        elif button.buttonVal.casefold() == 'ucs':
            algorithm = 'ucs'

        global state
        if(algorithm != ''):
            state = 'State 3'
  
    # Small or Big Maze
    # 10x10 or 20x20
    def mazeClick(self, button):
        global maze_size
        global clicked
        clicked = True
        if button.buttonVal.casefold() == 'big maze':
            maze_size = 'big'
        elif button.buttonVal.casefold() == 'big random maze':
            maze_size = 'big random'        
        elif button.buttonVal.casefold() == 'small maze':
            maze_size = 'small'
        elif button.buttonVal.casefold() == 'small random maze':
            maze_size = 'small random'
            
        global state
        if(maze_size != ''):
            state = 'State 4'


    # Color Theme
        # Basic - Black and White
        # Retro - Green lines, black background, and red walls
        # Oceano - Deep blue background, light blue lines, Gray walls
    def themeClick(self, button):
        global theme
        global clicked
        clicked = True        
        if button.buttonVal.casefold() == 'basic':
            theme = 'Basic'
        elif button.buttonVal.casefold() == 'retro':
            theme = 'Retro'
        elif button.buttonVal.casefold() == 'ocean':
            theme = 'Ocean'

        global state
        if(theme != ''):
            state = 'State 5'



    def draw(self):

        # State 1 - Automated or Manual
        # State 2a - Automated choose Algo
        # State 2b - Manual choose Assisted or Unassisted
        # State 2b1 - Assisted - Algo of choice
        # State 3 - Maze size
        # State 4 - Color theme
        # State 5 - Run 
        self.screen.fill((20, 20, 20))
        
        # State 1 - Automated or Manual
        if state.casefold() in ['state 1']:
            for Object in controlButtons:
                Object.process(self.screen)


        # State 2a - Automated choose Algo
        # State 2b1 - Assisted - Algo of choice
        elif state.casefold() in ['state 2a', 'state 2b_1']:
            for Object in algorithmButtons:
                Object.process(self.screen)
            for Object in returnButtons:
                Object.process(self.screen)

        # State 2b - Manual choose Assisted or Unassisted
        elif state.casefold() in ['state 2b']:
            for Object in assistanceButtons:
                Object.process(self.screen)
            for Object in returnButtons:
                Object.process(self.screen)

        # State 3 - Maze size
        elif state.casefold() in ['state 3']:
            for Object in mazeButtons:
                Object.process(self.screen)
            for Object in returnButtons:
                Object.process(self.screen)

        # State 4 - Color theme
        elif state.casefold() in ['state 4']:
            for Object in themeButtons:
                Object.process(self.screen)
            for Object in returnButtons:
                Object.process(self.screen)
        
        pygame.display.flip()

    def finish(self):
        self.running = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def run(self):
            global clicked

            while self.running:
                
                self.handle_events()
                self.draw()
                
                if(clicked == True):
                    clicked = False
                    time.sleep(0.25)


                if(state.casefold() == 'state 5'):
                    self.finish()

                time.sleep(0.1)
                # Draw the game

            # Quit pygame
            pygame.quit()

    def getTheme(self):
        return theme
    def getControl(self):
        return control
    def getAlgorithm(self):
        return algorithm
    def getMaze(self):
        return maze_size






  




