# LIBRARIES
import pygame
import os 
import math
import random

# PARAMETERS 
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

# Initialize vector to track unavailable coordinates and insert 'ground' in PLACED
PLACED = {'coords': [], 'colors': []}
for r in range(0, WIN_W, SZ):
    PLACED['coords'].append([r, WIN_H])
    PLACED['colors'].append((255,0,0))

# OBJECTS, FUNCTIONS
class Block():
    MID_SCREEN = WIN_W/2

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
        for n in range(len(self.coords)): 
            self.coords[n] = rotate(self.coords[1], self.coords[n], math.radians(90))
                              
    def move(self, dir):
        x_change = 0
        y_change = 0 
        if dir == 'left':
            x_change = -SZ
        elif dir == 'right':
            x_change = SZ
        elif dir == 'down':
            y_change = SZ
        
        new_coords = [[x + x_change, y + y_change] for [x,y] in self.coords]
        if any(coord in new_coords for coord in PLACED['coords']):
            self.place()
        else:
            self.coords = new_coords

    def place(self):
        self.placed = True
        for coord in self.coords: 
            PLACED['coords'].append(coord)
            PLACED['colors'].append(self.color)

    def draw(self,screen):
        for piece in self.coords:
            pygame.draw.rect(screen, self.color, 
                (piece[0], piece[1], 
                SZ, SZ)
            )
        # print(self.coords)

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.
    The angle should be given in radians.
    """
    ox, oy = origin[0], origin[1]
    px, py = point[0], point[1]

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return [round(qx), round(qy)]

def complete_line(screen, coords):
    for pair in coords:
        PLACED['coords'].remove(pair)

def move_placed_down(screen, coords):
    for pair in coords: 
        below = [pair[0], pair[1] + SZ]
        if below not in coords: 
            PLACED['coords'].remove(pair)
            PLACED['coords'].append(below)

def draw_placed(screen, coords_dict):
    for i,coord in enumerate(coords_dict['coords']):
        pygame.draw.rect(screen, coords_dict['colors'][i], 
                        (coord[0], coord[1], 
                        SZ, SZ))
