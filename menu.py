"""MAIN MENU"""
import pygame
import sys
from pygame.locals import *
from pygame import mixer

#menu
def menu():
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

    #Select mode
    select = "Select Mode:"
    select_text = letter_font.render(select, True, gray)
    select_text_rect = select_text.get_rect(center=(WIDTH//2,title_text.get_height()//2+100))

    #text button
    butt_country_text = butt_font.render("Country", True, black)
    butt_animal_text = butt_font.render("Animal", True, black)
    butt_food_text = butt_font.render("Food", True, black)
    butt_it_text = butt_font.render("IT", True, black)


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
                if 180 <= mouse[0] <= 180+140 and 220 <= mouse[1] <= 220+40: #contry
                    print("Country mode select!")

                if 480 <= mouse[0] <= 480+140 and 220 <= mouse[1] <= 220+45: #animal
                    print("Animal mode select!")

                if 180 <= mouse[0] <= 180+140 and 300 <= mouse[1] <= 300+45: #food
                    print("Food mode select!")

                if 480 <= mouse[0] <= 480+140 and 300 <= mouse[1] <= 300+45: #it
                    print("IT mode select!")

        clock.tick(50)
        
        mouse = pygame.mouse.get_pos()


	    #country button
        if 180 <= mouse[0] <= 180+140 and 220 <= mouse[1] <= 220+45:
            pygame.draw.rect(screen, gray, [180, 220, 140, 45])
		
        else:
            pygame.draw.rect(screen, pink, [180, 220, 140,45])
        
        #animal button

        if 480 <= mouse[0] <= 480+140 and 220 <= mouse[1] <= 220+45:
            pygame.draw.rect(screen, gray, [480, 220, 140, 45])
		
        else:
            pygame.draw.rect(screen, pink, [480, 220, 140,45])
        
        #food button

        if 180 <= mouse[0] <= 180+140 and 300 <= mouse[1] <= 300+45:
            pygame.draw.rect(screen, gray, [180, 300, 140, 45])
		
        else:
            pygame.draw.rect(screen, pink, [180, 300, 140,45])
        
        #IT button
        if 480 <= mouse[0] <= 480+140 and 300 <= mouse[1] <= 300+45:
            pygame.draw.rect(screen, gray, [480, 300, 140, 45])
		
        else:
            pygame.draw.rect(screen, pink, [480, 300, 140, 45])
	
	# superimposing the text onto our button
        screen.blit(butt_country_text, (195, 230))
        screen.blit(butt_animal_text, (500, 230))
        screen.blit(butt_food_text, (215, 310))
        screen.blit(butt_it_text, (535, 310))
        pygame.display.update()
menu()
