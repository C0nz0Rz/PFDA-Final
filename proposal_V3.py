import pygame
import random
import time
from datetime import datetime

    #that 3 by 3 artwork will be used as a pattern to create the 6 by 6 artwork.
    #I will reflect and translate the each of the 3/3 to create a "mirrored" piece of generative art that looks intentional,
    #       rather than by a human
    

def randomize():
    ...
#this function will randomize the colors to be place on a virtual 3 by 3 square canvas (This will be our original values)

def translate():
    ...
#this function will take the original values associated 
#this will take the coordinate position of each of the 9 squares and reflect them over the x axis, 
#       then translate them down 3 (on the y axis)

#then this will take the coordinate position of each of the original 9 squares and reflect them over the y axis,   
#       then translate them to the right (on the x-axis) 3

#then this will take the coordinate position of each of the original 9 squares and reflect them over the x axis,   
#       then translate them down 3 (on the y-axis), as well as translate them to the right (on the x-axis) 3
#       then finally, reflect the values across the y- axis

#def grid_pattern():
    #for row in range(size):
        #pattern = random.randrange(0, 256)


#grid_pattern(3)
    ...

#def coloring():
    #red_value = random.randrange(0, 256)
    #green_value = random.randrange(0, 256)
    #blue_value = random.randrange(0, 256)    


def main():
    ...
    #create a 6 by 6 pixel/square artwork that is randomly generated.
    #I would like a 3 by 3 pixel/square artwork to be randomly generated using two different colors.


    
    
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
    pygame.display.set_caption("Pixel_Art_Generation")
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
        # TODO: game logic
        #render game here
        screen.fill('blue')
        #create a loop to be repeated 3 times. Each time, the surface moves another surface length to the right.
        #for cube in range(1, 4):

        # TODO: 
        #Input Scale number
        #To set the scale of the art, give me a number between 3 and 7.
        #Check the value inputed and make sure it's between 3 and 7.
        #Allow the program to pause
        #Maybe add a keystroke to be assigned to a pause button
        #Save an image of the display
        
        counter = 0
        for row in range(1 , scale):
            for col in range(1, scale):
                surf = pygame.Surface((size, size))
                pix_color = pygame.Color(colors[counter])
            # #change "pix_color" function to randomize the color values.
                surf.fill(pix_color)
                screen.blit(surf, (100 + (size * col), 100 + (size * row)))
                counter += 1
        

        #surf1_2 = pygame.Surface((50, 50))
        #pix_color = pygame.Color(red_value, green_value, blue_value)
        #change "pix_color" function to randomize the color values.
        #surf1_2.fill(pix_color)
        #screen.blit(surf1_2, (150, 100))


        pygame.display.flip()
        clock.tick(60)
    pygame.image.save(screen, f"Pixel_Art_Generation_{datetime.now().strftime("%B_%d_%Y_%I--%M_%S_%p")}.png")
    pygame.quit()

if __name__ == "__main__":
    main()
