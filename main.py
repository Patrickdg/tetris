from pygame.time import Clock

from blocks import *

# TO-DO
"""
o Boundaries (1. Side, 2. Placed blocks X, 3. Ground X)
o Score system (complete lines)
o 'Next Piece' display
"""

# PARAMETERS 
pygame.init()   

# MAIN LOOP
def main():
    clock = pygame.time.Clock()
    
    active_block = Block(random.choice(list(BLOCKS.keys())))
    x_coords = range(0, WIN_H, SZ)

    running = True
    while running:
        SCREEN.fill((0,0,0))

        if active_block.placed:
            active_block = Block(random.choice(list(BLOCKS.keys())))

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
            
        # Check for complete lines
        placed_y_coords = set()
        for coord in PLACED['coords']: 
            placed_y_coords.add(coord[1])
        for y in placed_y_coords: 
            coords = []
            for x in x_coords:
                coords.append([x, y])
            if all(coord in list(placed_y_coords) for coord in coords):
                complete_line(SCREEN, coords)
                move_placed_down(SCREEN, PLACED['coords'])

        draw_placed(SCREEN, PLACED)
        active_block.draw(SCREEN)
        pygame.display.update()
        clock.tick(3)
    pygame.quit()

main()
