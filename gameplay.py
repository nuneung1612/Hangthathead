import pygame
import sys
from pygame.locals import *
from pygame import mixer
import random

#word 8-37
#button 41-46
#display 50-169


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
'Mainboard','Serialata', 'Floppydisk', 'Camcorders', 'Projecter', 'Smartwatch', 'Wirelesscharger', 'Wirelessrater',\
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
    pink = (219, 99, 104)
    for button, letter in BUTTONS:
        btn_text = btn_font.render(letter, True, pink)
        btn_text_rect = btn_text.get_rect(center=(button.x + SIZE//2, button.y + SIZE//2))
        pygame.draw.rect(screen, WHITE, button)
        screen.blit(btn_text, btn_text_rect)


def display_guess():
    display_word = ''

    for letter in WORD:
        if letter in GUESSED:
            display_word += f"{letter} "
        else:
            display_word += "_ "

    text = letter_font.render(display_word, True, BLACK)
    screen.blit(text, (400, 200))

def gameplay():
    pygame.init()
    global WIDTH, HEIGHT, screen, WORD, SIZE, BLACK, WHITE, GUESSED
    WIDTH, HEIGHT = 800, 500
    yellow = (249, 233, 147)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Hang That Head")

    mixer.music.load('music/gameplay.mp3')
    mixer.music.set_volume(0.2)
    mixer.music.play(-1)

    game_over = False

    # colors
    WHITE = (255,255,255)
    BLACK = (0,0,0)

    # Images
    IMAGES = []
    hangman_satus = 0

    for i in range(1, 9):
        image = pygame.image.load(f"images/Hang{i}.PNG")
        IMAGES.append(image)


    # Buttons
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
    A = 65
    BUTTONS = []

    for ind, box in enumerate(BOXES):
        letter = chr(A+ind)
        button = ([box, letter])
        BUTTONS.append(button)

    
    # Fonts
    global btn_font, letter_font, game_font
    btn_font = pygame.font.SysFont('arial', 30)
    letter_font = pygame.font.Font('fonts/Dimbo Regular.ttf', 60)
    game_font = pygame.font.Font('fonts/Dimbo Regular.ttf', 80)


    # Word
    word_list = []
    country_e = ["Brazil", "Laos", "China", "Egypt", "India", "Peru", "Russia", "Serbia", "Turkey", "Fiji", "Nepal",\
    "Libya", "Kenya", "Iran", "Italy", "Japan", "Korea", "France", "Cuba", "Canada"]
    mode = "food"
    level = "e"
    for _ in range(5):
        gen_list = words(mode, level)
        WORD = random.choice(gen_list)
        gen_list.remove(WORD)
        WORD = WORD.upper()
        word_list.append(WORD)
    print(word_list)
    GUESSED = []
    

    # Title
    title = "Hang That Head"
    title_text = game_font.render(title, True, BLACK)
    title_text_rect = title_text.get_rect(center=(WIDTH//2,title_text.get_height()//2+10))

    count = 0
    #score
   


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
            score_text = letter_font.render(str(count)+"/5", True, BLACK)
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
                A = 65
                BUTTONS = []

                for ind, box in enumerate(BOXES):
                    letter = chr(A+ind)
                    button = ([box, letter])
                    BUTTONS.append(button)
                draw_btns(BUTTONS)

            elif won and count == 4:
                game_over = True
                display_text = 'You Won !!!'
            else:
                display_text = 'You Lost !!!  '+str(count)+'/5'

            pygame.display.update()

            if game_over:
                pygame.time.delay(500)
                screen.fill(WHITE)
                game_over_text = game_font.render(display_text, True, BLACK)
                game_over_text_rect = game_over_text.get_rect(center=(WIDTH//2,HEIGHT//2))
                screen.blit(game_over_text, game_over_text_rect)
                pygame.display.update()
                pygame.time.delay(3000)
                pygame.quit()
                sys.exit()

#ยังแก้ไม่เสร็จ
gameplay()
