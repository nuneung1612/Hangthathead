import pygame
import sys
from pygame.locals import *
from pygame import mixer
import random
#word 8-37
#button 41-46
#display 50-169


def words():
    """ words in game """
    country_e = ["Brazil", "Laos", "China", "Egypt", "India", "Peru", "Russia", "Serbia", "Turkey", "Fiji", "Nepal",\
"Libya", "Kenya", "Iran", "Italy", "Japan", "Korea", "France", "Cuba", "Canada"]
    country_n = ["Bhutan", "Algeria", "Colombia", "Dominica", "Ecuador", "Georgia", "Hungary", "Lebanon", "Malaysia", \
"Netherlands", "Nicaragua", "Paraguay", "Philippines", "Slovakia", "Switzerland", "Uruguay", "Venezuela", "Suriname", \
"Tunisia","Sri Lanka"]
    country_h = ["Afghanistan", "Azerbaijan", "Bangladesh", "Botswana", "Djibouti", "Kyrgyzstan", "Liechtenstein", \
"Luxembourg", "Madagascar", "Mauritania", "Saudi Arabia", "Tajikistan", "Turkmenistan", "United Arab Emirates", \
"United States of America", "United Kingdom", "Zimbabwe", "Palestine State", "Papua New Guinea", "Kazakhstan"]
    animal_e = ["ant", "bat", "bird", "bear", "bee", "cat", "crab", "coe", "deer", "dog", "duck", "fox", "fish", "goat",\
"lion", "owl", "pig", "rat", "wolf", "frog"]
    animal_n = ["donkey", "goose", "horse", "monkey", "panda", "piglet", "rabbit", "sheep", "snake", "spider", "shark", \
"squid", "tiger", "whale", "zebra", "eagle", "rabbit", "turtle", 'Koala', "Camel"]
    animal_h = ["buffalo", "butterfly", "chicken", "crocodile", "elephant", "giraffe", "goldfish", "hamster", "crocodile", \
"gorilla", "hippopotamus", "kangaroo", "starfish", "ostrich", "Lobster", "rhinoceros", "Chimpanzee", "Penguin", "Shrimp", "Cheetah"]
    it_e = ['CPU', 'ram', 'mouse', 'phone', 'SSD', 'HDD', 'Case', 'IDE', 'SCSI','Cable', 'DVD', 'ROM', 'UPS', 'LCD', 'ipad', \
'ipod', 'macbook', 'Lan', 'VR', 'hub']
    it_n = ['Computer', 'notebook', 'monitor', 'webcam','Router','Display Card','Hard disk', 'DVD-RW', 'Speaker', 'VGA Card', \
'sound card', 'CPU Fan', 'memory',\
'storage', 'Scanner', 'USB hub', 'Laptop', 'tablet']
    it_h = ['smartphone', 'Flash Drive', 'keyboard', 'Head set', 'Thumb Drive','Handy Drive', 'Printer', 'Power Supply', \
'mainboard','Serial ATA', 'Floppy disk', 'Camcorders', 'Projecter', 'smartwatch', 'wireless charger', 'wireless rater',\
'wireless mouse','wireless keyboard', 'powerbank', 'Cooling Pad']
    food_e = ["Tea", "Soup", "Cake", "Egg", "Fish", "Jam", "Milk", "Taco", "Ham", "Tuna", "Stew", "Pie", "Tart", "Kiwi", \
"Corn", "Beef", "Pork", "Wine", "Salt", "Soda"]
    food_n = ["Salmon", "Cheese", "Steak", "Honey", "Salad", "Pizza", "Yogurt", "Gelato", "Coffee", "Cookie", "Bacon", \
"Lemon", "Butter", "Candy", "Jelly", "Juice", "Chips", "Water", "Bread", "Peach"]
    food_h = ["Macaron", "Cupcake", "Sandwich", "Burrito", "Noodles", "Croissant", "Avocado", "Almond", "Popsicle", \
"Meatball", "Ketchup", "Mustard", "Chocolate", "Spaghetti", "Artichoke", "Biscuit", "Popcorn", "Champagne", "Caramel", "Lolipop"]

def draw_btns(BUTTONS):
    for button, letter in BUTTONS:
        btn_text = btn_font.render(letter, True, BLACK)
        btn_text_rect = btn_text.get_rect(center=(button.x + SIZE//2, button.y + SIZE//2))
        pygame.draw.rect(screen, BLACK, button, 2)
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

def main(mode, level):
    """input"""
    pass
def gameplay():
    pygame.init()
    global WIDTH, HEIGHT, screen, WORD, SIZE, BLACK, WHITE, GUESSED
    WIDTH, HEIGHT = 800, 500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Hang That Head")

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
    WORD = random.choice(["Brazil", "Laos", "China", "Egypt", "India", "Peru", "Russia", "Serbia", "Turkey", "Fiji", "Nepal",\
"Libya", "Kenya", "Iran", "Italy", "Japan", "Korea", "France", "Cuba", "Canada"])
    WORD = WORD.upper()
    print(WORD)
    GUESSED = []
    

    # Title
    title = "Hang That Head"
    title_text = game_font.render(title, True, BLACK)
    title_text_rect = title_text.get_rect(center=(WIDTH//2,title_text.get_height()//2+10))

    while True:
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

        screen.fill(WHITE)
        screen.blit(IMAGES[hangman_satus], (130,60))
        screen.blit(title_text, title_text_rect)
        draw_btns(BUTTONS)
        display_guess()

        won = True

        for letter in WORD:
            if letter not in GUESSED:
                won = False
        scoring(won, game_over)



def scoring(won, game_over):
        count = 0
        if won:
            game_over = True
            display_text = 'You Won !!!'
        else:
            display_text = 'You Lost !!!'

        pygame.display.update()
        while game_over:
            if won and count < 5:
                pygame.time.delay(500)
                count += 1
                gameplay()
                pygame.display.update()
            else:
                pygame.time.delay(500)
                screen.fill(WHITE)
                game_over_text = game_font.render(display_text, True, BLACK)
                game_over_text_rect = game_over_text.get_rect(center=(WIDTH//2,HEIGHT//2))
                screen.blit(game_over_text, game_over_text_rect)
                pygame.display.update()
                pygame.time.delay(3000)
                pygame.quit()
                sys.exit()

gameplay()
