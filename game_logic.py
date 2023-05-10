import pygame
from config import *
from path_planning import *

# Initialize pygame
pygame.init()

# Define the font
font = pygame.font.SysFont(FONT, FONT_SIZE)

class Game:
    def __init__(self):
        # Set up the screen
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("My Game: Running")

        # Define the agent starting position
        self.agent_pos = AGENT_POS

        # Define the game loop
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_UP:
                    new_pos = (self.agent_pos[0], self.agent_pos[1] - 1)
                    if new_pos[1] >= 0 and not maze[new_pos[1]][new_pos[0]]:
                        self.agent_pos = new_pos
                elif event.key == pygame.K_DOWN:
                    new_pos = (self.agent_pos[0], self.agent_pos[1] + 1)
                    if new_pos[1] < GRID_HEIGHT and not maze[new_pos[1]][new_pos[0]]:
                        self.agent_pos = new_pos
                elif event.key == pygame.K_LEFT:
                    new_pos = (self.agent_pos[0] - 1, self.agent_pos[1])
                    if new_pos[0] >= 0 and not maze[new_pos[1]][new_pos[0]]:
                        self.agent_pos = new_pos
                elif event.key == pygame.K_RIGHT:
                    new_pos = (self.agent_pos[0] + 1, self.agent_pos[1])
                    if new_pos[0] < GRID_WIDTH and not maze[new_pos[1]][new_pos[0]]:
                        self.agent_pos = new_pos

    # Add this method to the Game class
    def draw_path(self, path):
        if path is not None:
            for i in range(len(path) - 1):
                x1, y1 = path[i]
                x2, y2 = path[i + 1]
                rect1 = pygame.Rect(x1 * GRID_SIZE, y1 * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                rect2 = pygame.Rect(x2 * GRID_SIZE, y2 * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                pygame.draw.line(self.screen, PURPLE, rect1.center, rect2.center, 10)

    def draw(self):
        # Draw the grid
        self.screen.fill(BLACK)
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                pygame.draw.rect(self.screen, NEON_GREEN, rect, 1)
                if maze[y][x] == 1:
                    pygame.draw.rect(self.screen, RED, rect)
                if GOAL_POS[0] == x and GOAL_POS[1] == y:
                    if GOAL_POS[0] < 0 or GOAL_POS[0] >= GRID_WIDTH or GOAL_POS[1] < 0 or GOAL_POS[1] >= GRID_HEIGHT:
                        continue
                    pygame.draw.circle(self.screen, BLUE, rect.center, GRID_SIZE // 2)
                if (x, y) == GOAL_POS and (x, y) == self.agent_pos:
                    text = font.render('Bazingga!', True, PURPLE)
                    text_rect = text.get_rect(center=self.screen.get_rect().center)
                    self.screen.blit(text, text_rect)


        # Find the path from the agent to the goal grid
        path = astar(maze, self.agent_pos, GOAL_POS)

        # Draw the path
        self.draw_path(path)

        # Draw the agent
        agent_rect = pygame.Rect(self.agent_pos[0] * GRID_SIZE, self.agent_pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        if self.agent_pos[0] < 0 or self.agent_pos[0] >= GRID_WIDTH or self.agent_pos[1] < 0 or self.agent_pos[1] >= GRID_HEIGHT:
            pass
        else:
            pygame.draw.circle(self.screen, YELLOW, agent_rect.center, GRID_SIZE // 2)

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
