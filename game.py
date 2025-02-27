import pygame

WIN_WIDTH, WIN_HEIGHT = 1000, 600
RES = (WIN_WIDTH, WIN_HEIGHT)

pygame.init()

screen = pygame.display.set_mode(RES)
pygame.display.set_caption("Chessburger Game")

def main(fps=60):
    
    running = True
    clock = pygame.time.Clock()
    
    while running:
        
        screen.fill((0, 0, 0))
        # screen.blit("background.png", (0, 0)) -- background.png not defined yet
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        pygame.display.flip()
        
    pygame.quit()
    quit()
