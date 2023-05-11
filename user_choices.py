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


class Choices:
    def __init__(self):
            # Set up the screen
            self.screen = pygame.display.set_mode((CHOICES_WIDTH, CHOICES_HEIGHT))
            pygame.display.set_caption("My Game: Choices")

            # Define the agent starting position

            # Define the game loop
            self.running = True

    def returnFunc():
            if(state.casefold() == 'state 2' or 'state 2a' or 'state 2b'):
                state = 'State 1'
            elif(state.casefold() == 'state 2b_1'):
                state = 'state 2b'
            elif(state.casefold() == 'state 3'):
                if(control.casefold() == 'Automated'):
                    state = 'state 2a'
                elif(algorithm.casefold == 'unassisted'):
                    state = 'state 2b'
                else:
                    state ='state 2b_1'
            elif(state.casefold() == 'state 4'):
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
        objects.clear()

        self.screen.fill((20, 20, 20))
        # State 1 - Automated or Manual
        # State 2a - Automated choose Algo
        # State 2b - Manual choose Assisted or Unassisted
        # State 2b1 - Assisted - Algo of choice
        # State 3 - Maze size
        # State 4 - Color theme
        # State 5 - Run 
        if(state.casefold() in ['state 1']):
            automateButton = Button('Automate', 30, 30, 300, 80, 'Automate', lambda: self.controlClick(automateButton))
            manualButton = Button('Manual', 30, 130, 300, 80, 'Manual', lambda: self.controlClick(manualButton))

        elif(state.casefold() in ['state 2a', 'state 2b_1']):
            astarButton = Button('astar', 30, 30, 300, 80, 'A* Algorithm', lambda: self.algoClick(astarButton))
            dfsButton = Button('dfs', 30, 130, 300, 80, 'DFS Algorithm', lambda: self.algoClick(dfsButton))
            ucsButton = Button('ucs', 30, 230, 300, 80, 'UCS Algorithm', lambda: self.algoClick(ucsButton))
            returnButton = Button(30, 330, 300, 80, 'Return', self.returnFunc())

        elif(state.casefold() in ['state 2b']):
            assistedButton = Button('assisted', 30, 30, 300, 80, 'Path Assisted', lambda: self.assistClick(assistedButton))
            unassistedButton = Button('unassisted', 30, 130, 300, 80, 'No Assistance', lambda: self.assistClick(unassistedButton))
            returnButton = Button(30, 230, 300, 80, 'Return', self.returnFunc())

        elif(state.casefold() in ['state 3']):
            smallMazeButton = Button('small maze', 30, 30, 300, 80, 'Small Maze', lambda: self.mazeClick(smallMazeButton))
            bigMazeButton = Button('big maze', 30, 130, 300, 80, 'Big Maze', lambda: self.mazeClick(bigMazeButton))
            returnButton = Button(30, 230, 300, 80, 'Return', self.returnFunc())

        elif(state.casefold() in ['state 4']):
            basicButton = Button('basic', 30, 30, 300, 80, 'Basic Theme', lambda: self.themeClick(basicButton))
            retroButton = Button('retro', 30, 130, 300, 80, 'Retro Theme', lambda: self.themeClick(retroButton))
            oceanButton = Button('ocean', 30, 230, 300, 80, 'Ocean Theme', lambda: self.themeClick(oc))
            returnButton = Button(30, 330, 300, 80, 'Return', self.returnFunc())
        
        pygame.display.flip()

    # TODO
    def finish():
        return

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def run(self):
            while self.running:
                
                self.handle_events()

                for object in objects:
                    object.process(self.screen)

                if(state.casefold() == 'state 5'):
                    self.finish()

                # Draw the game
                self.draw()

            # Quit pygame
            pygame.quit()







  




