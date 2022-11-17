"""MAIN MENU"""
import pygame
import sys
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
    #Dimbo
    game_font = pygame.font.SysFont('Dimbo', 80)
    letter_font = pygame.font.SysFont('Dimbo', 40)

    title = "Hang That Head"
    title_text = game_font.render(title, True, black)
    title_text_rect = title_text.get_rect(center=(WIDTH//2,title_text.get_height()//2+30))
    #Select mode
    select = "Select Mode:"
    select_text = letter_font.render(select, True, gray)
    select_text_rect = select_text.get_rect(center=(WIDTH//2,title_text.get_height()//2+100))
    #button


    while True:
        screen.fill(yellow)
        screen.blit(title_text, title_text_rect)
        screen.blit(select_text, select_text_rect)
        pygame.display.update()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(50)





class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False
menu()
