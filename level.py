"""level select"""
import pygame
import sys
from pygame.locals import *
from pygame import mixer
def level():
    #color
    white = (255, 255, 255)
    black = (0, 0, 0)
    yellow = (249, 233, 147) #bg
    pink = (219, 99, 104) #hang_man
    gray = (113, 113, 122) #fonts

    pygame.init()

    #music
    mixer.music.load('music/intro.mp3')
    mixer.music.play(-1)

    clock = pygame.time.Clock()
    WIDTH, HEIGHT = 800, 500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("Hang That Head")
    pygame.display.update()

    #Fonts
    game_font = pygame.font.Font('fonts/Dimbo Regular.ttf', 80)
    letter_font = pygame.font.Font('fonts/Dimbo Regular.ttf', 40)
    butt_font = pygame.font.SysFont('Corbel_bold', 40)

    #text in menu
    #title
    title = "Hang That Head"
    title_text = game_font.render(title, True, black)
    title_text_rect = title_text.get_rect(center=(WIDTH//2,title_text.get_height()//2+20))

    #Select level
    select = "Select Level:"
    select_text = letter_font.render(select, True, gray)
    select_text_rect = select_text.get_rect(center=(WIDTH//2,title_text.get_height()//2+100))

    #level text
    butt_easy = butt_font.render("Easy", True, black)
    butt_normal = butt_font.render("Normal", True, black)
    butt_hard = butt_font.render("Hard", True, black)


    while True:
        screen.fill(yellow)
        screen.blit(title_text, title_text_rect)
        screen.blit(select_text, select_text_rect)
        #pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if 330 <= mouse[0] <= 330+140 and 210 <= mouse[1] <= 210+45: #easy
                    print("easy select!")
                if 330 <= mouse[0] <= 330+140 and 270 <= mouse[1] <= 270+45: #normal
                    print("normal select!")
                if 330 <= mouse[0] <= 330+140 and 330 <= mouse[1] <= 330+45: #hard
                    print("hard select!")

        clock.tick(50)
        
        mouse = pygame.mouse.get_pos()


	    #easy button
        if 330 <= mouse[0] <= 330+140 and 210 <= mouse[1] <= 210+45:
            pygame.draw.rect(screen, gray, [330, 210, 140, 45])
		
        else:
            pygame.draw.rect(screen, pink, [330, 210, 140,45])
        
        #normal button

        if 330 <= mouse[0] <= 330+140 and 270 <= mouse[1] <= 270+45:
            pygame.draw.rect(screen, gray, [330, 270, 140, 45])
		
        else:
            pygame.draw.rect(screen, pink, [330, 270, 140,45])
        
        #hard button

        if 330 <= mouse[0] <= 330+140 and 330 <= mouse[1] <= 330+45:
            pygame.draw.rect(screen, gray, [330, 330, 140, 45])
		
        else:
            pygame.draw.rect(screen, pink, [330, 330, 140,45])
        
	

        screen.blit(butt_easy, (365, 220))
        screen.blit(butt_normal, (350, 280))
        screen.blit(butt_hard, (365, 340))
       
        pygame.display.update()
level()