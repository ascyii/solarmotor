"""
Wir haben ein rechtshaendiges Koordinatensystem,
wobei der Ursprung in der oberen linken Ecke des Tisches ist und die x-Achse in Richtung des Targets zeigt.
"""

import numpy as np
import pygame

SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280

MIRROR_LENGTH = 0.1
GRID_SIZE = 0.15
TABLE_SIZE = (6, 8) # Definiert die Anzahl der Spiegel

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

# Eigenschaften des Tisches
print(f"The table (mirror grid) has size {GRID_SIZE * TABLE_SIZE[0] * 100}cm x {GRID_SIZE * TABLE_SIZE[1] * 100}cm")

# Sonne und Turm Position (muss noch validiert werden)
source_pos = np.array([0.8, 0.45, 0.3])
target_pos = np.array([1, 0, 0])

game_table_orig = pygame.Vector2(50, SCREEN_HEIGHT - 50)
pixel_per_m = SCREEN_HEIGHT / (GRID_SIZE * TABLE_SIZE[1])

def rotate_point(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + np.cos(angle) * (px - ox) - np.sin(angle) * (py - oy)
    qy = oy + np.sin(angle) * (px - ox) + np.cos(angle) * (py - oy)

    return pygame.Vector2(qx, qy)

def global_to_game_pos(global_pos):
    return game_table_orig + pygame.Vector2(global_pos[0] * pixel_per_m, -global_pos[1] * pixel_per_m)

def game_to_global_pos(game_pos):
    res = (game_pos - game_table_orig) / pixel_per_m
    return np.array([res.x, -res.y, 0])

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            source_pos = game_to_global_pos(pygame.mouse.get_pos())

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # Iterate over each mirror
    for x_i in range(TABLE_SIZE[0]):
        for y_i in range(TABLE_SIZE[1]):
            mirror_pos = np.array([x_i * GRID_SIZE, y_i * GRID_SIZE, 0])

            target_dir = target_pos - mirror_pos
            source_dir = source_pos - mirror_pos

            c = global_to_game_pos(mirror_pos)

            if source_pos[0] < GRID_SIZE * (TABLE_SIZE[0] - 1) + 0.01:
                pygame.draw.line(screen, "PINK", c + pygame.Vector2(0, MIRROR_LENGTH / 2 * pixel_per_m), c + pygame.Vector2(0, -MIRROR_LENGTH / 2 * pixel_per_m), 3)
            else:
                # Calculate theta
                target_alpha = np.atan(target_dir[2]  / np.sqrt(target_dir[0] ** 2 + target_dir[1] ** 2))
                source_alpha = np.atan(source_dir[2]  / np.sqrt(source_dir[0] ** 2 + source_dir[1] ** 2))
                theta = target_alpha + np.abs(source_alpha - target_alpha) / 2

                # Calculate phi
                target_gamma = np.atan(target_dir[1] / target_dir[0])
                source_gamma = np.atan(source_dir[1] / source_dir[0])
                phi = (target_gamma - source_gamma) / 2 - target_gamma

                pygame.draw.line(screen, "LIGHTBLUE", rotate_point(c, c + pygame.Vector2(0, MIRROR_LENGTH / 2 * pixel_per_m), phi), rotate_point(c, c + pygame.Vector2(0, -MIRROR_LENGTH / 2 * pixel_per_m), phi), 3)

            pygame.draw.circle(screen, "DARKBLUE", c, 3)

    pygame.draw.circle(screen, "YELLOW", global_to_game_pos(source_pos), 10)
    pygame.draw.circle(screen, "GRAY", global_to_game_pos(target_pos), 10)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 30

pygame.quit()
