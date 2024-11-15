import pygame
import random
def draw_grid(screen):
    LINE_COLOR=(0,0,0)
    for i in range (1,17):
        pygame.draw.line(screen, LINE_COLOR, (0, i*32), (640, i*32),2)
    for i in range(1,21):
        pygame.draw.line(screen,LINE_COLOR, (i*32, 0), (i*32, 512),2)
def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        color=pygame.Color("green")
        clock = pygame.time.Clock()
        running = True
        mole_position=(0,0)
        while running:
            screen.fill("light green")
            draw_grid(screen)
            pygame.draw.line(screen,color,(20,16),(32,32))
            clock.tick(60)
            screen.blit(mole_image,mole_image.get_rect(topleft=(mole_position[0]*32, mole_position[1]*32)))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y=event.pos
                    if (mole_position[0]*32)<=x<((mole_position[0]+1)*32) and (mole_position[1]*32)<=y<((mole_position[1]+1)*32):
                        mole_position=(random.randrange(0,20),random.randrange(0,16))
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
