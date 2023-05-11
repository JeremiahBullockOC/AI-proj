import pygame

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

state = 'State 1'
control = ''
maze_size = ''
algorithm = ''
theme = ''
# automateButton = None
# manualButton = None
# astarButton = None
# dfsButton = None
# ucsButton = None
# returnButton = None
# assistedButton = None
# unassistedButton = None
# basicButton = None
# retroButton = None
# oceanButton = None
# smallMazeButton = None
# bigMazeButton = None
buttons = []

class Choices:
    def __init__(self):
            # Set up the screen
            self.screen = pygame.display.set_mode((CHOICES_WIDTH, CHOICES_HEIGHT))
            pygame.display.set_caption("My Game: Choices")

            # Define the agent starting position

            # Define the game loop
            self.running = True

            self.automateButton = Button('Automate', 30, 30, 300, 80, 'Automate', lambda: self.controlClick(self.automateButton))
            self.manualButton = Button('Manual', 30, 130, 300, 80, 'Manual', lambda: self.controlClick(self.manualButton))
            self.astarButton = Button('astar', 30, 30, 300, 80, 'A* Algorithm', lambda: self.algoClick(self.astarButton))
            self.dfsButton = Button('dfs', 30, 130, 300, 80, 'DFS Algorithm', lambda: self.algoClick(self.dfsButton))
            self.ucsButton = Button('ucs', 30, 230, 300, 80, 'UCS Algorithm', lambda: self.algoClick(self.ucsButton))
            self.returnButton = Button('', 30, 330, 300, 80, 'Return', self.returnFunc)
            self.assistedButton = Button('assisted', 30, 30, 300, 80, 'Path Assisted', lambda: self.assistClick(self.assistedButton))
            self.unassistedButton = Button('unassisted', 30, 130, 300, 80, 'No Assistance', lambda: self.assistClick(self.unassistedButton))
            self.basicButton = Button('basic', 30, 30, 300, 80, 'Basic Theme', lambda: self.themeClick(self.basicButton))
            self.retroButton = Button('retro', 30, 130, 300, 80, 'Retro Theme', lambda: self.themeClick(self.retroButton))
            self.oceanButton = Button('ocean', 30, 230, 300, 80, 'Ocean Theme', lambda: self.themeClick(self.oceanButton))
            self.smallMazeButton = Button('small maze', 30, 30, 300, 80, 'Small Maze', lambda: self.mazeClick(self.smallMazeButton))
            self.bigMazeButton = Button('big maze', 30, 130, 300, 80, 'Big Maze', lambda: self.mazeClick(self.bigMazeButton))
            buttons.extend([self.automateButton, self.manualButton, self.astarButton, self.dfsButton, self.ucsButton,self.returnButton,self.assistedButton, self.unassistedButton, self.basicButton,self.retroButton, self.oceanButton, self.smallMazeButton, self.bigMazeButton])
    def returnFunc(self):
        global state
        if state.casefold() == 'state 2' or state.casefold() == 'state 2a' or state.casefold() == 'state 2b':
            state = 'State 1'
        elif state.casefold() == 'state 2b_1':
            state = 'state 2b'
        elif state.casefold() == 'state 3':
            if control.casefold() == 'Automated':
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
        control = button.buttonVal
        if button.buttonVal.casefold() == 'Automated':
            global state
            state = 'State 2a'
        else:
            state = 'State 2b'

    # Assisted or Unassisted
        # If assisted navigate to algorithm of choice
    def assistClick(self, button):
        global algorithm
        if button.buttonVal.casefold() == 'assisted':
            global state
            state = 'State 2b_1'
        else:
            algorithm = 'Unassisted'
            state = 'State 3'

    # Alogrithm of choice
        # A*
        # DFS
        # UCS
        # Not sure how much difference the user will see
    def algoClick(self, button):
        global algorithm
        if button.buttonVal.casefold() == 'astar':
            algorithm = 'astar'
        elif button.buttonVal.casefold() == 'dfs':
            algorithm = 'dfs'
        else:
            algorithm = 'ucs'
        global state
        state = 'State 3'
  
    # Small or Big Maze
    # 10x10 or 20x20
    def mazeClick(self, button):
        global maze_size
        if button.buttonVal.casefold() == 'big maze':
            maze_size = 'big'
        else:
            maze_size = 'small'
        global state
        state = 'State 4'


    # Color Theme
        # Basic - Black and White
        # Retro - Green lines, black background, and red walls
        # Oceano - Deep blue background, light blue lines, Gray walls
    def themeClick(self, button):
        global theme
        if button.buttonVal.casefold() == 'basic':
            theme = 'Basic'
        elif button.buttonVal.casefold() == 'retro':
            theme = 'Retro'
        else:
            theme = 'Ocean'
        global state
        state = 'State 5'



    def draw(self):
        # buttons.clear()

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
            self.automateButton.process(self.screen)
            self.manualButton.process(self.screen)

        # State 2a - Automated choose Algo
        # State 2b - Manual choose Assisted or Unassisted
        # State 2b1 - Assisted - Algo of choice
        elif state.casefold() in ['state 2a', 'state 2b_1']:
            self.astarButton.process(self.screen)
            self.dfsButton.process(self.screen)
            self.ucsButton.process(self.screen)
            self.returnButton.process(self.screen)

        # State 2b - Manual choose Assisted or Unassisted
        elif state.casefold() in ['state 2b']:
            self.assistedButton.process(self.screen)
            self.unassistedButton.process(self.screen)
            self.returnButton.process(self.screen)

        # State 3 - Maze size
        elif state.casefold() in ['state 3']:
            self.smallMazeButton.process(self.screen)
            self.bigMazeButton.process(self.screen)
            self.returnButton.process(self.screen)

        # State 4 - Color theme
        elif state.casefold() in ['state 4']:
            self.basicButton.process(self.screen)
            self.retroButton.process(self.screen)
            self.oceanButton.process(self.screen)
            self.returnButton.process(self.screen)
        
        pygame.display.flip()

    # TODO
    def finish(self):
        return

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def run(self):
            while self.running:
                
                self.handle_events()

                for object in buttons:
                    object.process(self.screen)

                if(state.casefold() == 'state 5'):
                    self.finish()

                # Draw the game
                self.draw()

            # Quit pygame
            pygame.quit()







  




