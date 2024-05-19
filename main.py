import pygame
import random
import sys
import button
import time

#function for getting a random number between 1-6
def dice_roll():
    dice_number = random.randint(1,6)
    print(dice_number)
    if dice_number == 1:
        dice_image = pygame.image.load(r"C:\Users\yoges\Desktop\Aarya Program\Python\snakes_and_ladders_game\ONE_dice.png")
        return dice_image
    elif dice_number == 2:
        dice_image = pygame.image.load(r"C:\Users\yoges\Desktop\Aarya Program\Python\snakes_and_ladders_game\two_dice.png")
        return dice_image
    elif dice_number == 3:
        dice_image = pygame.image.load(r"C:\Users\yoges\Desktop\Aarya Program\Python\snakes_and_ladders_game\three_dice.png")
        return dice_image
    elif dice_number == 4:
        dice_image = pygame.image.load(r"C:\Users\yoges\Desktop\Aarya Program\Python\snakes_and_ladders_game\four_dice.png")
        return dice_image
    elif dice_number == 5:
        dice_image = pygame.image.load(r"C:\Users\yoges\Desktop\Aarya Program\Python\snakes_and_ladders_game\five_dice.png")
        return dice_image
    elif dice_number == 6:
        dice_image = pygame.image.load(r"C:\Users\yoges\Desktop\Aarya Program\Python\snakes_and_ladders_game\six_dice.png")
        return dice_image

#intiating the game
pygame.init()

#dimension of thr screen
screen = pygame.display.set_mode((1050, 600))

#setting the background
background = pygame.image.load(r"C:\Users\yoges\Desktop\Aarya Program\Python\snakes_and_ladders_game\bkg.png")

#title, logo for the window
pygame.display.set_caption("Snakes and Ladders")
icon = pygame.image.load(r"C:\Users\yoges\Desktop\Aarya Program\Python\snakes_and_ladders_game\snake-and-ladder.png")
pygame.display.set_icon(icon)

#write the text on the screen
def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img,(x,y))

#function for image placement
def imageplacement(image, imageX, imageY):
    screen.blit(image, (imageX, imageY))

def player_mode():
    cvp_image = pygame.image.load(r"C:\Users\yoges\Desktop\Aarya Program\Python\snakes_and_ladders_game\computer_vs_player.png").convert_alpha()
    cvp_button = button.button(290, 300, cvp_image, 1)
    pvp_image = pygame.image.load(r"C:\Users\yoges\Desktop\Aarya Program\Python\snakes_and_ladders_game\player_vs_player.png").convert_alpha()
    pvp_button = button.button(540, 300, pvp_image, 1)
    running = True

    while running:

        screen.fill("black")
        screen.blit(background,(0,0))
        draw_text(" CHOOSE THE MODE ", pygame.font.SysFont("times new roman", 40), (0,0,0), 300, 150)

        cvp_button.draw(screen)
        pvp_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cvp_button.draw(screen):
                    cvp_game()
                if pvp_button.draw(screen):
                    pvp_game()
        pygame.display.update()
  
def cvp_game():
    #pasting snake and ladder image in the screen
    image = pygame.image.load(r"C:\Users\yoges\Desktop\Aarya Program\Python\snakes_and_ladders_game\desktop-wallpaper-4-snakes-and-ladders-game-and-snake-and-ladder.png")

    arrow_image = pygame.image.load(r"C:\Users\yoges\Desktop\Aarya Program\Python\snakes_and_ladders_game\arrow.png").convert_alpha()
    arrow_button = button.button(110, 350, arrow_image, 1)

    running = True

    while running:

        screen.fill("black")
        screen.blit(background,(0,0))
        imageplacement(image, 307, 0)
        draw_text(" Player Blue ", pygame.font.SysFont("times new roman", 30), (0,0,255), 50, 140)
        imageplacement(pygame.image.load(r"snakes_and_ladders_game\player (4).png"), 240, 130)
        draw_text(" Player Red ", pygame.font.SysFont("times new roman", 30), (255,0,0), 50, 50)
        imageplacement(pygame.image.load(r"snakes_and_ladders_game\player (2).png"), 240, 40)
        arrow_button.draw(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if arrow_button.draw(screen):
                    img = dice_roll()
                    imageplacement(img, 100, 250)
                
        
        pygame.display.update()
        time.sleep(1.3)

def pvp_game():
    #pasting snake and ladder image in the screen
    image = pygame.image.load(r"C:\Users\yoges\Desktop\Aarya Program\Python\snakes_and_ladders_game\desktop-wallpaper-4-snakes-and-ladders-game-and-snake-and-ladder.png")
    imageX = 307
    imageY = 0
    arrow_image = pygame.image.load(r"C:\Users\yoges\Desktop\Aarya Program\Python\snakes_and_ladders_game\arrow.png").convert_alpha()
    arrow_button = button.button(110, 350, arrow_image, 1)

    running = True

    while running:

        screen.fill("black")
        screen.blit(background,(0,0))
        imageplacement(image, imageX, imageY)
        draw_text(" Player Blue ", pygame.font.SysFont("times new roman", 30), (0,0,255), 50, 140)
        imageplacement(pygame.image.load(r"snakes_and_ladders_game\player (4).png"), 240, 130)
        draw_text(" Player Red ", pygame.font.SysFont("times new roman", 30), (255,0,0), 50, 50)
        imageplacement(pygame.image.load(r"snakes_and_ladders_game\player (2).png"), 240, 40)

        arrow_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if arrow_button.draw(screen):
                    img = dice_roll()
                    imageplacement(img, 100, 250)
        
        pygame.display.update()
        time.sleep(1.3)

start_image = pygame.image.load(r"C:\Users\yoges\Desktop\Aarya Program\Python\snakes_and_ladders_game\—Pngtree—play button candy blue_5306396.png").convert_alpha()
start_button = button.button(390, 300, start_image, 1)

#variables font and text color for main menu
font = pygame.font.SysFont("Times New Roman", 40)
text_color = (0,0,0)

running = True

while running:

    screen.fill((0,0,0))
    screen.blit(background,(0,0))#background set for the window

    draw_text("MAIN MENU", font, text_color, 400, 100)
    start_button.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.draw(screen):
                player_mode()
    
    pygame.display.update()