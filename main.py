import pygame
import os 
import random

# PARAMETERS 
pygame.init()   

WIN_W = 450
WIN_H = WIN_W * 2
SCREEN = pygame.display.set_mode([WIN_W, WIN_H])
pygame.display.set_caption("Tetris")

BLOCKS = ["L", "J", "S", "Z", "SQ", "I", "T"]
BLOCK_SIZE = int(WIN_W/10)

GRID = []
for i in range(int(WIN_H/BLOCK_SIZE)):
    row = []
    for j in range(int(WIN_W/BLOCK_SIZE)):
        row.append(0)
    GRID.append(row)
print(GRID)

# OBJECTS 
class Block():
    def __init__(self, block):
        self.block = block
        self.active = False
        self.x = WIN_W/2
        self.y = WIN_H/4
    def rotate(self):
        pass
    def move(self):
        pass
    def draw(self,screen):
        screen.blit(self.block, (self.x, self.y))

# MAIN LOOP
def main():
    active_block = Block(random.choice(BLOCKS))
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
        active_block.draw(SCREEN)
        pygame.display.update()
    pygame.quit()

main()
