import pygame
import sys

pygame.init()
sys.init()

SCREEN_WIDTH=800
SCREEN_HEIGHT=600

WHITE=(255,255,255)
BLACK=(0,0,0)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption("main menu")

font=pygame.font.SysFont(None, 60)

def draw_text(text,font,color,surface,x,y):
    text_obj=font.render(text,True,color)
    text_rect= text_obj.get_rect()
    text_rect.center=(x,y)
    surface.blit(text_obj,text_rect)

def main_menu():
    while True:
        screen.fill(WHITE)
        draw_text("Welcom to Main Menu",font,BLACK,screen,SCREEN_WIDTH//2,SCREEN_HEIGHT//4)

        mouse_x,mouse_y=pygame.mouse.get_pos()

        button_start=pygame.rect(300,250,200,50)
        button_quit=pygame.rect(300,350,250,50)

        pygame.draw.rect(screen, BLACK, button_start)
        draw_text("Başla", font, WHITE, screen, button_start.centerx, button_start.centery)
        pygame.draw.rect(screen, BLACK, button_quit)
        draw_text("Çıkış", font, WHITE, screen, button_quit.centerx, button_quit.centery)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_start.collidepoint(mouse_x, mouse_y):
                    #  game is here
                    #  main game loop is here
                    pass
                if button_quit.collidepoint(mouse_x, mouse_y):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main_menu()