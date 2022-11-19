"""MAIN MENU"""
import pygame
import sys
import button
from pygame.locals import *
#menu
def menu():
    #color
    white = (255, 255, 255)
    black = (0, 0, 0)
    yellow = (249, 233, 147) #bg
    pink = (219, 99, 104) #hang_man
    gray = (113, 113, 122) #fonts

    pygame.init()

    clock = pygame.time.Clock()
    WIDTH, HEIGHT = 800, 500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("Hang That Head")
    pygame.display.update()

    #Fonts
    game_font = pygame.font.Font('fonts/Dimbo Regular.ttf', 80)
    letter_font = pygame.font.Font('fonts/Dimbo Regular.ttf', 40)

    #text in menu
    #title
    title = "Hang That Head"
    title_text = game_font.render(title, True, black)
    title_text_rect = title_text.get_rect(center=(WIDTH//2,title_text.get_height()//2+20))

    #Select mode
    select = "Select Mode:"
    select_text = letter_font.render(select, True, gray)
    select_text_rect = select_text.get_rect(center=(WIDTH//2,title_text.get_height()//2+100))

    #button
    #load image
    exit_img = pygame.image.load('exit_btn.png').convert_alpha()

    #create button instances
    exit_button = button.Button(450, 200, exit_img, 0.8)



    while True:
        screen.fill(yellow)
        screen.blit(title_text, title_text_rect)
        screen.blit(select_text, select_text_rect)
        if exit_button.draw(screen):
            print("Press")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(50)
        pygame.display.update()

