import os 
import random
import pygame
from pygame.time import Clock

# PARAMETERS 
pygame.init()   

WIN_W = 300
WIN_H = 600
SCREEN = pygame.display.set_mode([WIN_W, WIN_H])
pygame.display.set_caption("Tetris")

SZ = int(WIN_W/10)
BLOCKS = {"L": {'coords': [[0,SZ], [SZ,SZ], [2*SZ,SZ], [2*SZ,0]], 
                'color':(255,128,0)},
          "J": {'coords': [[0,0], [0,SZ], [SZ,SZ], [2*SZ,SZ]], 
                'color':(0,0,255)},
          "S": {'coords': [[0,SZ], [SZ,SZ], [SZ,0], [2*SZ,0]], 
                'color':(0,255,0)},
          "Z": {'coords': [[0,0], [SZ,0], [SZ,SZ], [2*SZ,SZ]], 
                'color':(255,0,0)},
          "SQ":{'coords': [[0,0], [0,SZ], [SZ,0], [SZ,SZ]], 
                'color':(255,255,0)},
          "I": {'coords': [[0,0], [SZ,0], [2*SZ,0], [3*SZ,0]], 
                'color':(0,255,255)},
          "T": {'coords': [[0,SZ], [SZ,0], [SZ,SZ], [2*SZ,SZ]], 
                'color':(153,51,255)}
        }

SZ = int(WIN_W/10)

# Initialize vector to track unavailable coordinates and insert 'ground' in PLACED
PLACED = []
for r in range(0,WIN_W, SZ):
    PLACED.insert(0,[r, WIN_H])

# OBJECTS 
class Block():
    MID_SCREEN = WIN_W/2
    DY = SZ

    def __init__(self, block):
        self.block = block
        self.x = WIN_W/2
        self.y = WIN_H/4
        self.coords = BLOCKS[self.block]['coords']
        self.placed = False
        self.side_flag = False
        self.color = BLOCKS[self.block]['color']
    
        # Displace block coordinates to spawn zone
        for n in range(len(self.coords)):
            self.coords[n] = [self.coords[n][0] + self.MID_SCREEN - SZ, 
                              self.coords[n][1] + SZ]

    def rotate(self):
        pass
    def move(self, dir):
        x_change = 0
        y_change = 0 
        if dir == 'left' and not self.side_flag:
            x_change = -SZ
        elif dir == 'right' and not self.side_flag:
            x_change = SZ
        elif dir == 'up':
            y_change = -SZ
        elif dir == 'down':
            y_change = SZ
        
        self.coords = [[x + x_change, y + y_change] for [x,y] in self.coords]

        side_flag = any(0 in coord for coord in self.coords) or any((WIN_W - SZ) in coord for coord in self.coords)
        self.side_flag = True if side_flag else False

    # TO-DO: trigger transfer self.coords into placed vector for crash detection (other pieces AND bare floor)
    def place(self):
        self.placed = True
        for coord in self.coords: 
            PLACED.insert(coord)

    def draw(self,screen):
        for piece in self.coords:
            pygame.draw.rect(screen, self.color, 
                (piece[0], piece[1], 
                SZ, SZ)
            )
        print(self.coords)
        print(PLACED)
    

# MAIN LOOP
def main():
    clock = pygame.time.Clock()
    active_block = Block(random.choice(list(BLOCKS.keys())))
    running = True
    while running:
        SCREEN.fill((0,0,0))
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
                elif event.key == pygame.K_UP:
                    active_block.rotate()

        if not active_block.placed:
            active_block.move('down')
        active_block.draw(SCREEN)
        pygame.display.update()
        clock.tick(2)
    pygame.quit()

main()
