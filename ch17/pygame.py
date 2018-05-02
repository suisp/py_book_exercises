import pygame
import time

def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surface_sz = 480   # Desired physical surface size, in pixels.

    # Create surface of (width, height), and its window.
    main_surface = pygame.display.set_mode((surface_sz, surface_sz))

    # Set up some data to describe a small rectangle and its color
    small_rect = (300, 200, 150, 90)
    some_color = (255, 0, 0)        # A color is a mix of (Red, Green, Blue)

    # Kam added these items
    head = pygame.image.load("trumphead3.png")
    my_font = pygame.font.SysFont("lmao", 16)

    frame_count = 0
    frame_rate  = 0
    t0 = time.clock()


    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        # Update your game objects and data structures here...
        frame_count +=1
        if frame_count % 50 == 0:
            t1= time.clock()
            frame_rate = 50 / (t1-t0)
            t0 = t1

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        main_surface.fill((0, 200, 255))

        # Overpaint a smaller rectangle on the main surface
        main_surface.fill(some_color, small_rect)
        main_surface.blit(head, (100,0))
        the_text = my_font.render("Frame = {0},  rate = {1:.2f} fps"
                                  .format(frame_count, frame_rate), True, (0, 0, 0))
        main_surface.blit(the_text, (10,10))

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()

    pygame.quit()     # Once we leave the loop, close the window.

main()