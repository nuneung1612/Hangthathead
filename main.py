"""MAIN MENU"""
import pygame
import sys
from pygame.locals import *
from pygame import mixer
#menu 6-127
#level 132-230

#menu
#music


def menu(var=True):
    #color
    white = (255, 255, 255)
    black = (0, 0, 0)
    yellow = (249, 233, 147) #bg
    pink = (219, 99, 104) #hang_man
    gray = (113, 113, 122) #fonts

    pygame.init()
    
    mixer.music.load('music/intro.mp3')
    mixer.music.set_volume(0.2)
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

    #Select level
    select_level = letter_font.render("Select Level:", True, gray)
    #select_text_rect = select_text.get_rect(center=(WIDTH//2,title_text.get_height()//2+100))

    #text button
    butt_country_text = butt_font.render("Country", True, black)
    butt_animal_text = butt_font.render("Animal", True, black)
    butt_food_text = butt_font.render("Food", True, black)
    butt_it_text = butt_font.render("IT", True, black)

    #level text
    butt_easy = butt_font.render("Easy", True, black)
    butt_normal = butt_font.render("Normal", True, black)
    butt_hard = butt_font.render("Hard", True, black)
    butt_back = butt_font.render("Back", True, white)

    #status of the menu and level
    menu_isrun = var
    level_isrun = False


    while menu_isrun == True:
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
                    #pygame.quit()
                    menu_isrun = False
                    level_isrun = True

                if 480 <= mouse[0] <= 480+140 and 220 <= mouse[1] <= 220+45: #animal
                    print("Animal mode select!")
                    menu_isrun = False
                    level_isrun = True

                if 180 <= mouse[0] <= 180+140 and 300 <= mouse[1] <= 300+45: #food
                    print("Food mode select!")
                    menu_isrun = False
                    level_isrun = True

                if 480 <= mouse[0] <= 480+140 and 300 <= mouse[1] <= 300+45: #it
                    print("IT mode select!")
                    menu_isrun = False
                    level_isrun = True

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

    


        while level_isrun == True:
            screen.fill(yellow)
            screen.blit(title_text, title_text_rect)
            screen.blit(select_level, select_text_rect)
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
                    if 100 <= mouse[0] <= 100 + 100 and 400<= mouse[1] <= 400+45:#back
                        level_isrun = False
                        menu_isrun = True

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
            
            if 100 <= mouse[0] <= 100 + 100 and 400 <= mouse[1] <= 400+45:
                pygame.draw.rect(screen, gray, [100, 400, 100, 45])
            else:
                pygame.draw.rect(screen, black, [100, 400, 100, 45])



            screen.blit(butt_easy, (365, 220))
            screen.blit(butt_normal, (350, 280))
            screen.blit(butt_hard, (365, 340))
            screen.blit(butt_back, (115, 410))

            pygame.display.update()


menu()
