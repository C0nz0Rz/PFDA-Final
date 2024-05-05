import pygame
import random
import time


def grid_pattern(size):
    for row in range(size):
        pattern = random.randrange(0, 256)
        for col in range(size):
            screen.blit(surf, (100 + (size * cube), 100 + (size * cube)))

grid_pattern(3)
    ...

def coloring():
    red_value = random.randrange(0, 256)
    green_value = random.randrange(0, 256)
    blue_value = random.randrange(0, 256)   