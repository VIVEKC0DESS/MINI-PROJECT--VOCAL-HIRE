import pygame
import sys

# Initialize the Pygame engine
pygame.init()

# Setup the display (Width: 800, Height: 600)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("VocalHire: Data Science Interview Simulator")

# Define some basic colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main():
    running = True
    
    # The Main Application Loop
    while running:
        # 1. Handle Events (like clicking the X to close the window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # 2. Draw the background
        screen.fill(WHITE)
        
        # 3. Update the display
        pygame.display.flip()
        
    # Shutdown cleanly when the loop breaks
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()