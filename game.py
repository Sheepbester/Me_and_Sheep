import pygame
class Game:
    

    
    def __init__(self, FPS):
        self.WIN_WIDTH = 640
        self.WIN_HEIGHT = 360
        self.title = "Cheesburger Game"
        self.RES = (self.WIN_WIDTH, self.WIN_HEIGHT)
        self.BACKGROUND_IMG  = pygame.transform.scale(pygame.image.load("Assets/background.png"), self.RES)
        self.FPS = FPS
        
    def draw_background(self, win):
        win.blit(self.BACKGROUND_IMG, (0, 0))



pygame.init()

game = Game(FPS=60)

screen = pygame.display.set_mode(game.RES)
pygame.display.set_caption(game.title)

def main(game):
    
    running = True
    clock = pygame.time.Clock()
    
    while running:
        
        clock.tick(game.FPS) # limits the fps
        # screen.blit("background.png", (0, 0)) -- background.png not defined yet
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        pygame.display.flip()
        
        game.draw_background(screen)
        
    pygame.quit()
    quit()
    
main(game=game)
