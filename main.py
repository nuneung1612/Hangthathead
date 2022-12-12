"""MAIN MENU"""
import pygame
import sys
import random
from pygame.locals import *
from pygame import mixer
#menu 6-127
#level 132-230

#menu
#music


def menu(var=True):
    """ menu screen """
    #color
    white = (255, 255, 255)
    black = (0, 0, 0)
    yellow = (249, 233, 147) #bg
    pink = (219, 99, 104) #hang_man
    gray = (113, 113, 122) #fonts
    pygame.init()
    
    mixer.music.load('music/intro.mp3')
    mixer.music.set_volume(0.025)
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

    #text button
    butt_country_text = butt_font.render("Country", True, white)
    butt_animal_text = butt_font.render("Animal", True, white)
    butt_food_text = butt_font.render("Food", True, white)
    butt_it_text = butt_font.render("IT", True, white)

    #level text
    butt_easy = butt_font.render("Easy", True, white)
    butt_normal = butt_font.render("Normal", True, white)
    butt_hard = butt_font.render("Hard", True, white)
    butt_back = butt_font.render("Back", True, white)

    #status of the menu and level
    menu_isrun = var
    level_isrun = False


    while menu_isrun == True:
        screen.fill(yellow)
        screen.blit(title_text, title_text_rect)
        screen.blit(select_text, select_text_rect)
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if 180 <= mouse[0] <= 180+140 and 220 <= mouse[1] <= 220+40: #contry
                    print("Country mode select!")
                    mode = "country"
                    menu_isrun = False
                    level_isrun = True


                if 480 <= mouse[0] <= 480+140 and 220 <= mouse[1] <= 220+45: #animal
                    print("Animal mode select!")
                    mode = "animal"
                    menu_isrun = False
                    level_isrun = True

                if 180 <= mouse[0] <= 180+140 and 300 <= mouse[1] <= 300+45: #food
                    print("Food mode select!")
                    mode = "food"
                    menu_isrun = False
                    level_isrun = True

                if 480 <= mouse[0] <= 480+140 and 300 <= mouse[1] <= 300+45: #it
                    print("IT mode select!")
                    mode = "it"
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
        screen.blit(butt_country_text, (195, 230))
        screen.blit(butt_animal_text, (500, 230))
        screen.blit(butt_food_text, (215, 310))
        screen.blit(butt_it_text, (535, 310))
        pygame.display.update()

        while level_isrun == True:
            screen.fill(yellow)
            screen.blit(title_text, title_text_rect)
            screen.blit(select_level, select_text_rect)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if 330 <= mouse[0] <= 330+140 and 210 <= mouse[1] <= 210+45: #easy
                        print("easy select!")
                        level = "e"
                        gameplay(mode, level)
                    if 330 <= mouse[0] <= 330+140 and 270 <= mouse[1] <= 270+45: #normal
                        print("normal select!")
                        level = "n"
                        gameplay(mode, level)
                    if 330 <= mouse[0] <= 330+140 and 330 <= mouse[1] <= 330+45: #hard
                        print("hard select!")
                        level = "h"
                        gameplay(mode, level)
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


def words(mode, level):
    """ words in game """
    country_e = ["Brazil", "Laos", "China", "Egypt", "India", "Peru", "Russia", "Serbia", "Turkey", "Fiji", "Nepal",\
"Libya", "Kenya", "Iran", "Italy", "Japan", "Korea", "France", "Cuba", "Canada"]
    country_n = ["Bhutan", "Algeria", "Colombia", "Dominica", "Ecuador", "Georgia", "Hungary", "Lebanon", "Malaysia", \
"Bangkok", "Finland", "Paraguay", "Philippines", "Slovakia", "Denmark", "Uruguay", "Belgium", "Suriname", \
"Tunisia","Vanuatu"]
    country_h = ["Afghanistan", "Azerbaijan", "Bangladesh", "Venezuela" "Botswana", "Switzerland", "Djibouti", "Kyrgyzstan", "Liechtenstein", \
"Luxembourg", "Madagascar", "Mauritania", "Nicaragua", "Tajikistan", "Turkmenistan", "Ascension", \
"Netherlands", "Zimbabwe", "Lithuania", "Kazakhstan"]
    animal_e = ["ant", "bat", "bird", "bear", "bee", "cat", "crab", "cow", "deer", "dog", "duck", "fox", "fish", "goat",\
"lion", "owl", "pig", "rat", "wolf", "frog"]
    animal_n = ["donkey", "goose", "horse", "monkey", "panda", "piglet", "rabbit", "sheep", "snake", "spider", "shark", \
"squid", "tiger", "whale", "zebra", "eagle", "rabbit", "turtle", 'Koala', "Camel"]
    animal_h = ["buffalo", "butterfly", "chicken", "crocodile", "elephant", "giraffe", "goldfish", "hamster", "crocodile", \
"gorilla", "hippopotamus", "kangaroo", "starfish", "ostrich", "Lobster", "rhinoceros", "Chimpanzee", "Penguin", "Shrimp", "Cheetah"]
    it_e = ['Cpu', 'Ram', 'Mouse', 'Phone', 'Ssd', 'Hdd', 'Case', 'Ide', 'Scsi','Cable', 'Dvd', 'Rom', 'Ups', 'Lcd', 'Ipad', \
'Ipod', 'Macbook', 'Lan', 'VR', 'Hub']
    it_n = ['Computer', 'Notebook', 'Monitor', 'Webcam','Router','DisplayCard','Harddisk', 'Dvdrw', 'Speaker', 'Vgacard', \
'Soundcard', 'Cpufan', 'Memory',\
'Storage', 'Scanner', 'Usbhub', 'Laptop', 'Tablet']
    it_h = ['Smartphone', 'Flashdrive', 'Keyboard', 'Headset', 'Thumbdrive','Handydrive', 'Printer', 'Powersupply', \
'Mainboard','Serialata', 'Floppydisk', 'Camcorders', 'Projecter', 'Smartwatch', 'Wirelesscharger', 'Wirelessrouter',\
'Wirelessmouse','Wirelesskeyboard', 'Powerbank', 'CoolingPad']
    food_e = ["Tea", "Soup", "Cake", "Egg", "Fish", "Jam", "Milk", "Taco", "Ham", "Tuna", "Stew", "Pie", "Tart", "Kiwi", \
"Corn", "Beef", "Pork", "Wine", "Salt", "Soda"]
    food_n = ["Salmon", "Cheese", "Steak", "Honey", "Salad", "Pizza", "Yogurt", "Gelato", "Coffee", "Cookie", "Bacon", \
"Lemon", "Butter", "Candy", "Jelly", "Juice", "Chips", "Water", "Bread", "Peach"]
    food_h = ["Macaron", "Cupcake", "Sandwich", "Burrito", "Noodles", "Croissant", "Avocado", "Almond", "Popsicle", \
"Meatball", "Ketchup", "Mustard", "Chocolate", "Spaghetti", "Artichoke", "Biscuit", "Popcorn", "Champagne", "Caramel", "Lolipop"]
    if mode == "country" and level == "e":
        lis = country_e
    elif mode == "country" and level == "n":
        lis = country_n
    elif mode == "country" and level == "h":
        lis = country_h
    elif mode == "animal" and level == "e":
        lis = animal_e
    elif mode == "animal" and level == "n":
        lis = animal_n
    elif mode == "animal" and level == "h":
        lis = animal_h
    elif mode == "it" and level == "e":
        lis = it_e
    elif mode == "it" and level == "n":
        lis = it_n
    elif mode == "it" and level == "h":
        lis = it_h
    elif mode == "food" and level == "e":
        lis = food_e
    elif mode == "food" and level == "n":
        lis = food_n
    elif mode == "food" and level == "h":
        lis = food_h
    return lis

def draw_btns(BUTTONS):
    """to draw buttons"""
    pink = (219, 99, 104)
    for button, letter in BUTTONS:
        btn_text = btn_font.render(letter, True, WHITE)
        btn_text_rect = btn_text.get_rect(center=(button.x + SIZE//2, button.y + SIZE//2))
        pygame.draw.rect(screen, pink, button)
        screen.blit(btn_text, btn_text_rect)


def display_guess():
    """guess word"""
    display_word = ''

    for letter in WORD:
        if letter in GUESSED:
            display_word += f"{letter} "
        else:
            display_word += "_ "
    text = letter_font.render(display_word, True, BLACK)
    screen.blit(text, (400, 200))

def gameplay(mode, level):
    """game play"""
    pygame.init()
    global WIDTH, HEIGHT, screen, WORD, SIZE, BLACK, WHITE, GUESSED
    WIDTH, HEIGHT = 800, 500
    yellow = (249, 233, 147)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Hang That Head")
    mixer.music.load('music/gameplay.mp3')
    mixer.music.set_volume(0.025)
    mixer.music.play(-1)

    game_over = False

    # colors
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    gray = (113, 113, 122)

    #Images
    IMAGES = []
    hangman_satus = 0

    for i in range(1, 9):
        image = pygame.image.load(f"images/Hang{i}.PNG")
        IMAGES.append(image)


    #Buttons
    ROWS = 2
    COLS = 13
    GAP = 20
    SIZE = 40
    BOXES = []

    for row in range(ROWS):
        for col in range(COLS):
            x = ((GAP * col) + GAP) + (SIZE * col)
            y = ((GAP * row) + GAP) + (SIZE * row) + 330
            box = pygame.Rect(x, y, SIZE, SIZE)
            BOXES.append(box)
    aaa = 65
    BUTTONS = []

    for ind, box in enumerate(BOXES):
        letter = chr(aaa+ind)
        button = ([box, letter])
        BUTTONS.append(button)


    # Fonts
    global btn_font, letter_font, game_font
    btn_font = pygame.font.SysFont('arial', 30)
    letter_font = pygame.font.Font('fonts/Dimbo Regular.ttf', 60)
    game_font = pygame.font.Font('fonts/Dimbo Regular.ttf', 70)


    # Word
    word_list = []
    gen_list = words(mode, level)
    for _ in range(5):
        WORD = random.choice(gen_list)
        gen_list.remove(WORD)
        WORD = WORD.upper()
        word_list.append(WORD)
    print(word_list)
    GUESSED = []

    # Title
    title = "Hang That Head"
    title_text = game_font.render(title, True, BLACK)
    title_text_rect = title_text.get_rect(center=(WIDTH//2, title_text.get_height()//2+10))

    count = 0

    #command
    game_isrun = True

    while count < 4:
        while game_isrun:
            game_over = False
            WORD = word_list[count]
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    clicked_pos = event.pos

                    for button, letter in BUTTONS:
                        if button.collidepoint(clicked_pos):
                            GUESSED.append(letter)

                            if letter not in WORD:
                                hangman_satus += 1

                            if hangman_satus == 7:
                                game_over = True

                            BUTTONS.remove([button, letter])
            score_text = letter_font.render(str(count)+"/5", True, gray)
            screen.fill(yellow)
            screen.blit(IMAGES[hangman_satus], (130,60))
            screen.blit(title_text, title_text_rect)
            screen.blit(score_text,(700,90))
            draw_btns(BUTTONS)
            display_guess()

            won = True

            for letter in WORD:
                if letter not in GUESSED:
                    won = False
            if won and count<4:
                count += 1
                game_over = False
                hangman_satus = 0
                del GUESSED[0:]
                ROWS = 2
                COLS = 13
                GAP = 20
                SIZE = 40
                BOXES = []

                for row in range(ROWS):
                    for col in range(COLS):
                        x = ((GAP * col) + GAP) + (SIZE * col)
                        y = ((GAP * row) + GAP) + (SIZE * row) + 330
                        box = pygame.Rect(x, y, SIZE, SIZE)
                        BOXES.append(box)
                aaa = 65
                BUTTONS = []

                for ind, box in enumerate(BOXES):
                    letter = chr(aaa+ind)
                    button = ([box, letter])
                    BUTTONS.append(button)
                #draw_btns(BUTTONS)

            elif won and count == 4:
                game_over = True
                display_text = 'You Won !!!'
            else:
                display_text = 'You Lost !!!'

            pygame.display.update()

            #summary screen

            if game_over:
                pygame.time.delay(500)
                gameover(display_text, True)


def gameover(display_text, gameover_run=False):
    """game over screen"""
    pygame.init()

    mixer.music.load('music/game over.mp3')
    mixer.music.set_volume(0.025)
    mixer.music.play(-1)

    pink = (219, 99, 104)
    gray = (113, 113, 122)
    yellow = (249, 233, 147)
    black = (0,0,0)
    white = (255,255,255)
    screen = pygame.display.set_mode((800, 500))
    game_font = pygame.font.Font('fonts/Dimbo Regular.ttf', 100)
    butt_font = pygame.font.SysFont('Corbel_bold', 40)
    while gameover_run == True:
        screen.fill(yellow)
        game_over_text = game_font.render(display_text, True, black)
        game_over_text_rect = 240, 80
        screen.blit(game_over_text, game_over_text_rect)

        menu_butt_txt = butt_font.render("Menu", True, white)
        exit_butt_txt = butt_font.render("Quit", True, white)

        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if 330 <= mouse[0] <= 330+140 and 250 <= mouse[1] <= 250+45:
                    print("menu")
                    gameover_run = False
                    menu(True)

                if 330 <= mouse[0] <= 330+140 and 310 <= mouse[1] <= 310+45: #animal
                    print("exit")
                    gameover_run = False
                    pygame.quit()
                    sys.exit()

        if 330 <= mouse[0] <= 330+140 and 250 <= mouse[1] <= 250+45:
            pygame.draw.rect(screen, gray, [330, 250, 140, 45])

        else:
            pygame.draw.rect(screen, pink, [330, 250, 140, 45])

        if 330 <= mouse[0] <= 330+140 and 310 <= mouse[1] <= 310+45:
            pygame.draw.rect(screen, gray, [330, 310, 140, 45])

        else:
            pygame.draw.rect(screen, pink, [330, 310, 140, 45])
        screen.blit(menu_butt_txt, (365, 260))
        screen.blit(exit_butt_txt, (367, 320))
        pygame.display.update()


menu()
