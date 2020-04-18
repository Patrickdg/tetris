import pygame
import 

# PARAMETERS 
pygame.init()   

WIN_W = 250
WIN_H = 250
SCREEN = pygame.display.set_mode([WIN_W, WIN_H])
pygame.display.set_caption("Tetris")

# OBJECTS 
class Block():
    def __init__(self, type):
        self.type = type
        self.placed = False

    def rotate(self):

    def move(self):

    def draw(self):


# MAIN LOOP
def main():


    running = True
    while running:
        SCREEN.fill((0,0,0))
        pygame.time.delay(200)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Key input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    active_block.move('left')
                elif event.key == pygame.K_RIGHT:
                    active_block.move('right')
                elif event.key == pygame.K_DOWN:
                    active_block.move('down')

        pygame.display.update()
    pygame.quit()
