import pygame
import random
import time
from datetime import datetime

def main():
    ...
    #creates a scaled pixel/square artwork that is randomly generated.
    
    running = True
    size = 50

    scale = int(input("Pick a number between 2 and 5, which will be the scale of the art."))
    scale = scale + 1


    colors = []

    for color in range(1, scale**2):
        red_value = random.randrange(0, 256)
        green_value = random.randrange(0, 256)
        blue_value = random.randrange(0, 256)
        rgb = (red_value, green_value, blue_value)
        colors.append(rgb)

    pygame.init() 
    pygame.display.set_caption("Generative_Pixel_Pattern")
    clock = pygame.time.Clock()
    past_time = time.time
    dt = 0
    resolution = (800, 600)
    screen_info = pygame.display.Info()
    screen_res = (screen_info.current_w, screen_info.current_h)
    screen = pygame.display.set_mode(resolution, pygame.RESIZABLE, pygame.FULLSCREEN)

    while running:
        #Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill('blue')

        counter = 0
        for row in range(1 , scale):
            for col in range(1, scale):
                surf = pygame.Surface((size, size))
                pix_color = pygame.Color(colors[counter])
                surf.fill(pix_color)
                screen.blit(surf, (100 + (size * col), 100 + (size * row)))
                counter += 1

        pygame.display.flip()
        clock.tick(60)
        
    pygame.image.save(screen, f"Pixel_Art_Generation_{datetime.now().strftime("%B_%d_%Y_%I--%M_%S_%p")}.png")
    pygame.quit()

if __name__ == "__main__":
    main()
