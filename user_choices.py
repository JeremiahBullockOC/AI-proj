import pygame

from config import *
from button import *

pygame.init()

# Choices state
state = 'State 1'

# This file is to hold and store all the choices that a user might make for a game. This will be passed to Game.py
# User choices
control = ''
algorithm = ''
maze_size = ''
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
    def controlClick(buttonVal):
        control = buttonVal
        if(buttonVal.casefold() == 'Automated'):
            state = 'State 2a'
        else:
            state = 'State 2b'

    # Assisted or Unassisted
        # If assisted navigate to algorithm of choice
    def assistClick(buttonVal):
        if(buttonVal.casefold() == 'assisted'):
            state == 'State 2b_1'
        else:
            algorithm = 'Unassisted'
            state = 'State 3'

    # Alogrithm of choice
        # A*
        # DFS
        # UCS
        # Not sure how much difference the user will see
    def algoClick(buttonVal):
        if(buttonVal.casefold() == 'astar'):
            algorithm = 'astar'
        elif(buttonVal.casefold() == 'dfs'):
            algorithm = 'dfs'
        else:
            algorithm = 'ucs'
        
        state = 'State 3'
  
    # Small or Big Maze
    # 10x10 or 20x20
    def mazeClick(buttonVal):
        if(buttonVal.casefold() == 'big maze'):
            maze = 'big'
        else:
            maze = 'small'

    # Color Theme
        # Basic - Black and White
        # Retro - Green lines, black background, and red walls
        # Oceano - Deep blue background, light blue lines, Gray walls
    def themeClick(buttonVal):
        if(buttonVal.casefold() == 'basic'):
            theme = 'Basic'
        elif(buttonVal.casefold() == 'retro'):
            theme = 'Retro'
        else:
            theme = 'Ocean'
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
        if(state.casefold() == 'state 1'):
            automateButton = Button(30, 30, 300, 80, 'Automate', controlClick('Automate'))
            manualButton = Button(30, 130, 300, 80, 'Manual', controlClick('Manual'))

        elif(state.casefold() == 'state 2a' or state.casefold() == 'state 2b_1'):
            astarButton = Button(30, 30, 300, 80, 'A* Algorithm', algoClick('astar'))
            dfsButton = Button(30, 130, 300, 80, 'DFS Algorithm', algoClick('dfs'))
            ucsButton = Button(30, 230, 300, 80, 'UCS Algorithm', algoClick('ucs'))
            returnButton = Button(30, 330, 300, 80, 'Return', returnFunc())

        elif(state.casefold() == 'state 2b'):
            assistedButton = Button(30, 30, 300, 80, 'Path Assisted', assistClick('assisted'))
            unassistedButton = Button(30, 130, 300, 80, 'No Assistance', assistClick('unassisted'))
            returnButton = Button(30, 230, 300, 80, 'Return', returnFunc())

        elif(state.casefold() == 'state 3'):
            smallMazeButton = Button(30, 30, 300, 80, 'Small Maze', mazeClick('small maze'))
            bigMazeButton = Button(30, 130, 300, 80, 'Big Maze', mazeClick('big maze'))
            returnButton = Button(30, 230, 300, 80, 'Return', returnFunc())

        elif(state.casefold() == 'state 4'):
            basicButton = Button(30, 30, 300, 80, 'Basic Theme', themeClick('basic'))
            retroButton = Button(30, 130, 300, 80, 'Retro Theme', themeClick('retro'))
            oceanButton = Button(30, 230, 300, 80, 'Ocean Theme', themeClick('ocean'))
            returnButton = Button(30, 330, 300, 80, 'Return', returnFunc())
        
        pygame.display.flip()

    # TODO
    def finish():
        return

    def run(self):
            while self.running:
                
                for object in objects:
                    object.process()

                if(state.casefold() == 'state 5'):
                    finish()

                # Draw the game
                self.draw()

            # Quit pygame
            pygame.quit()







  




