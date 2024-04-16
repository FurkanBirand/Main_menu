import pygame
import sys

# Ekran genişliği ve yüksekliği
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Pygame başlat
pygame.init()

# Ekran oluştur
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ana Menü")

# Font yükle
font = pygame.font.SysFont(None, 60)


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)


def main_menu():
    while True:
        screen.fill(WHITE)
        draw_text("Ana Menü", font, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Butonları oluştur
        button_start = pygame.Rect(300, 250, 200, 50)
        button_quit = pygame.Rect(300, 350, 200, 50)

        # Butonları çiz
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
                    # Oyunu başlat
                    # Oyununuzun ana oyun döngüsünü buraya yazın
                    pass
                if button_quit.collidepoint(mouse_x, mouse_y):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main_menu()
