import pygame
import button



pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

resume_img = pygame.image.load("button_resume.png").convert_alpha()
options_img = pygame.image.load("button_options.png").convert_alpha()
quit_img = pygame.image.load("button_quit.png").convert_alpha()
video_img = pygame.image.load("button_video.png").convert_alpha()
keys_img = pygame.image.load("button_keys.png").convert_alpha()
back_img = pygame.image.load("button_back.png").convert_alpha()
audio_img = pygame.image.load("button_audio.png").convert_alpha()



resume_button=button.Button(304,125,resume_img,(1))
options_button=button.Button(304,245,options_img,(1))
quit_button=button.Button(304,365,quit_img,(1))

audio_button=button.Button(304,125,audio_img,(1))
keys_button=button.Button(304,245,keys_img,(1))
back_button=button.Button(304,365,back_img,(1))
video_button=button.Button(304,5,video_img,(1))

#game variables
game_paused = False
menu_state= "main"

font = pygame.font.SysFont("arialblack", 40)
#define color
TEXT_COL=(255,255,255)

def draw_text(text, font,text_col,x,y):
    img = font.render(text, True, text_col)
    screen.blit(img,  (x,y))


current=True
while current:

    background=pygame.image.load("summer.png").convert_alpha()
    screen.blit(background,(0,0))

    #check if game is paused
    if game_paused ==True:
       #check menu state
     if menu_state == "main":
       if  resume_button.draw(screen):
           game_paused = False
       if options_button.draw(screen):
            menu_state = "options"
       if quit_button.draw(screen):
           current = False
     if menu_state == "options":
         if video_button.draw(screen):
             print("video settings")
         if audio_button.draw(screen):
             print("audio settings")
         if keys_button.draw(screen):
             print("change keys settings")
         if back_button.draw(screen):
             menu_state = "main"

    else:
        draw_text("Press SPACE", font, TEXT_COL,160,250)


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused =True
        if event.type == pygame.QUIT:
            current = False


    pygame.display.update()

pygame.quit()

