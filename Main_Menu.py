import pygame
import sys



pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")


font = pygame.font.SysFont("arialblack", 40)
#define color
TEXT_COL=(255,255,255)

def draw_text(text, font,text_col,x,y):
    img = font.render(text, True, text_col)
    screen.blit(img,(x,y))


current=True
while current:

    screen.fill((52,78,91))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            current = False


    pygame.display.update()

pygame.quit()

