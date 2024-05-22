import pygame
import random
import sys
import button
import time

position = {
            1 : (340, 510), 2 : (395, 510), 3 : (445, 510), 4 : (498, 510), 5 : (550, 510), 6 : (603,510), 7 : (655, 510), 8 : (707, 510), 9 : (760, 510), 10 : (814, 510),
            11 : (814, 455), 12 : (760, 455), 13 : (707, 455), 14 : (655,455), 15 : (603,455), 16 : (550, 455), 17 : (498, 455), 18 : (445, 455), 19 : (395, 455), 20 : (340, 455), 
            21 : (340, 400), 22 : (395, 400), 23 : (445, 400), 24 : (498, 400), 25 : (550, 400), 26 : (603, 400), 27 : (655, 400), 28 : (707, 400), 29 : (760, 400), 30 : (814, 400),
            31 : (814, 348), 32 : (760, 348), 33 : (707, 348), 34 : (655, 348), 35 : (603, 348), 36 : (550, 348), 37 : (498, 348), 38 : (445, 348), 39 : (395, 348), 40 : (340, 348), 
            41 : (340, 298), 42 : (395, 298), 43 : (445, 298), 44 : (498, 298), 45 : (550, 298), 46 : (603, 298), 47 : (655, 298), 48 : (707, 298), 49 : (760, 298), 50 : (814, 298),
            51 : (814, 244), 52 : (760, 244), 53 : (707, 244), 54 : (655, 244), 55 : (603, 244), 56 : (550, 244), 57 : (498, 244), 58 : (445, 244), 59 : (395, 244), 60 : (340, 244), 
            61 : (340, 194), 62 : (395, 194), 63 : (445, 194), 64 : (498, 194), 65 : (550, 194), 66 : (603, 194), 67 : (655, 194), 68 : (707, 194), 69 : (760, 194), 70 : (814, 194),
            71 : (814, 140), 72 : (760, 140), 73 : (707, 140), 74 : (655, 140), 75 : (603, 140), 76 : (550, 140), 77 : (498, 140), 78 : (445, 140), 79 : (395, 140), 80 : (340, 140), 
            81 : (340, 86), 82 : (395, 86), 83 : (445, 86), 84 : (498, 86), 85 : (550, 86), 86 : (603, 86), 87 : (655, 86), 88 : (707, 86), 89 : (760, 86), 90 : (814, 86),
            91 : (814, 33), 92 : (760, 33), 93 : (707, 33), 94 : (655, 33), 95 : (603, 33), 96 : (550, 33), 97 : (498, 33), 98 : (445, 33), 99 : (395, 33), 100 : (340, 33), 
            }

def snakes_check(position):
    new_position_dict = {44 : 22, 46 : 5, 48 : 9, 52 : 11, 55 : 7, 59 : 17, 64 : 36, 69 : 39, 73 : 1, 83 : 19, 92 : 51, 95 : 24, 98 : 28}
    if position in new_position_dict:
        return new_position_dict[position]
    else:
        return position

def ladders_check(position):
    new_position_dict = {8 : 26, 21 : 82, 43 : 77, 50 : 91, 54 : 93, 62 : 96, 66 : 87, 80 : 100}
    if position in new_position_dict:
        return new_position_dict[position]
    else:
        return position

#function for getting a random number between 1-6
def dice_roll():
    dice_number = random.randint(1,6)
    if dice_number == 1:
        dice_image = pygame.image.load(r"./ONE_dice.png")
        return dice_image,dice_number
    elif dice_number == 2:
        dice_image = pygame.image.load(r"./two_dice.png")
        return dice_image,dice_number
    elif dice_number == 3:
        dice_image = pygame.image.load(r"./three_dice.png")
        return dice_image,dice_number
    elif dice_number == 4:
        dice_image = pygame.image.load(r"./four_dice.png")
        return dice_image,dice_number
    elif dice_number == 5:
        dice_image = pygame.image.load(r"./five_dice.png")
        return dice_image,dice_number
    elif dice_number == 6:
        dice_image = pygame.image.load(r"./six_dice.png")
        return dice_image,dice_number

#intiating the game
pygame.init()

#dimension of thr screen
screen = pygame.display.set_mode((1050, 600))

#setting the background
background = pygame.image.load(r"./bkg.png")

#title, logo for the window
pygame.display.set_caption("Snakes and Ladders")
icon = pygame.image.load(r"./snake-and-ladder.png")
pygame.display.set_icon(icon)

#write the text on the screen
def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img,(x,y))

#function for image placement
def imageplacement(image, imageX, imageY):
    screen.blit(image, (imageX, imageY))

def player_mode():
    cvp_image = pygame.image.load(r"./computer_vs_player.png").convert_alpha()
    cvp_button = button.button(290, 300, cvp_image, 1)
    pvp_image = pygame.image.load(r"./player_vs_player.png").convert_alpha()
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
  
def turn_r():
    draw_text(" Your turn ", pygame.font.SysFont("comicsansms", 26), (255,255,255), 60, 80)

def turn_b():
    draw_text(" Your turn ", pygame.font.SysFont("comicsansms", 26), (0,0,0), 60, 170)

def cvp_game():
    #pasting snake and ladder image in the screen
    image = pygame.image.load(r"./desktop-wallpaper-4-snakes-and-ladders-game-and-snake-and-ladder.png")
    arrow_image = pygame.image.load(r"./arrow.png").convert_alpha()
    arrow_button = button.button(110, 350, arrow_image, 1)

    running = True
    turn = "blue"
    c_position_r,c_position_b = 0,0
    rx,ry = 240,40
    bx,by = 240,130

    while running:

        screen.fill("black")
        screen.blit(background,(0,0))
        imageplacement(image, 307, 0)
        draw_text(" Player Blue ", pygame.font.SysFont("times new roman", 30), (0,0,255), 50, 140)
        imageplacement(pygame.image.load(r"./player (4).png"), bx,by)
        draw_text(" Computer ", pygame.font.SysFont("times new roman", 30), (255,0,0), 50, 50)
        imageplacement(pygame.image.load(r"./player (2).png"), rx,ry)
        

        if turn == "blue":
            turn_b()
            arrow_button.draw(screen)
        else:
            turn = "blue"
            img,d_num = dice_roll()
            imageplacement(img, 100, 250)
            pygame.display.update()
            time.sleep(1.0)
            c_position_r += d_num
            if c_position_r in position:
                rx,ry = position[c_position_r][0], position[c_position_r][1]
                imageplacement(pygame.image.load(r"./player (2).png"), rx, ry)
                pygame.display.update()

                if snakes_check(c_position_r) != c_position_r:
                    c_position_r = snakes_check(c_position_r)
                    rx,ry = position[c_position_r][0], position[c_position_r][1]
                    imageplacement(pygame.image.load(r"./player (2).png"), rx, ry)
                    pygame.display.update()
                if ladders_check(c_position_r) != c_position_r:
                    c_position_r = ladders_check(c_position_r)
                    rx,ry = position[c_position_r][0], position[c_position_r][1]
                    imageplacement(pygame.image.load(r"./player (2).png"), rx, ry)
                    pygame.display.update()
            if c_position_r >= 100:
                draw_text(" COMPUTER IS THE WINNER ", pygame.font.SysFont("times new roman", 40), (255,255,255), 150, 230)
                pygame.display.update()
                print("COMPUTER is the winner....")
                time.sleep(2.3)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if arrow_button.draw(screen) and turn == "blue":
                    img,d_num = dice_roll()
                    imageplacement(img, 100, 250)
                    pygame.display.update()
                    time.sleep(1.0)

                if img != "" and turn == "blue":
                    turn = "red"
                    c_position_b += d_num
                    if c_position_b in position:
                        bx,by = position[c_position_b][0], position[c_position_b][1]
                        imageplacement(pygame.image.load(r"./player (4).png"), bx, by)
                        pygame.display.update()

                        if snakes_check(c_position_b) != c_position_b:
                            c_position_b = snakes_check(c_position_b)
                            bx,by = position[c_position_b][0], position[c_position_b][1]
                            imageplacement(pygame.image.load(r"./player (2).png"), bx, by)
                            pygame.display.update()
                        if ladders_check(c_position_b) != c_position_b:
                            c_position_b = ladders_check(c_position_b)
                            bx,by = position[c_position_b][0], position[c_position_b][1]
                            imageplacement(pygame.image.load(r"./player (2).png"), bx, by)
                            pygame.display.update()
                if c_position_b >= 100 :
                    draw_text(" PLAYER BLUE IS THE WINNER  ", pygame.font.SysFont("times new roman", 40), (255,255,255), 150, 230)
                    pygame.display.update()
                    print("PLAYER BLUE is the winner....")
                    time.sleep(2.3)
                    running = False
        pygame.display.update()

def pvp_game():
    #pasting snake and ladder image in the screen
    image = pygame.image.load(r"./desktop-wallpaper-4-snakes-and-ladders-game-and-snake-and-ladder.png")
    imageX = 307
    imageY = 0
    arrow_image = pygame.image.load(r"./arrow.png").convert_alpha()
    arrow_button = button.button(110, 350, arrow_image, 1)

    running = True
    turn = "red"
    c_position_r,c_position_b = 0,0
    rx,ry = 240,40
    bx,by = 240,130


    while running:

        screen.fill("black")
        screen.blit(background,(0,0))
        imageplacement(image, imageX, imageY)
        draw_text(" Player Blue ", pygame.font.SysFont("times new roman", 30), (0,0,255), 50, 140)
        imageplacement(pygame.image.load(r"./player (4).png"), bx,by)
        draw_text(" Player Red ", pygame.font.SysFont("times new roman", 30), (255,0,0), 50, 50)
        imageplacement(pygame.image.load(r"./player (2).png"), rx,ry)

        arrow_button.draw(screen)

        if turn == "red":
            turn_r()
        else:
            turn_b()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if arrow_button.draw(screen):
                    img,d_num = dice_roll()
                    print(d_num)
                    imageplacement(img, 100, 250)
                    pygame.display.update()
                    time.sleep(1.3)

                if img != "" and turn == "red":
                    turn = "blue"
                    c_position_r += d_num
                    if c_position_r in position:
                        rx,ry = position[c_position_r][0], position[c_position_r][1]
                        imageplacement(pygame.image.load(r"./player (2).png"), rx, ry)
                        pygame.display.update()

                        if snakes_check(c_position_r) != c_position_r:
                            c_position_r = snakes_check(c_position_r)
                            rx,ry = position[c_position_r][0], position[c_position_r][1]
                            imageplacement(pygame.image.load(r"./player (2).png"), rx, ry)
                            pygame.display.update()
                        if ladders_check(c_position_r) != c_position_r:
                            c_position_r = ladders_check(c_position_r)
                            rx,ry = position[c_position_r][0], position[c_position_r][1]
                            imageplacement(pygame.image.load(r"./player (2).png"), rx, ry)
                            pygame.display.update()


                elif img != "" and turn == "blue":
                    turn = "red"
                    c_position_b += d_num
                    if c_position_b in position:
                        bx,by = position[c_position_b][0], position[c_position_b][1]
                        imageplacement(pygame.image.load(r"./player (4).png"), bx, by)
                        pygame.display.update()

                        if snakes_check(c_position_b) != c_position_b:
                            c_position_b = snakes_check(c_position_b)
                            bx,by = position[c_position_b][0], position[c_position_b][1]
                            imageplacement(pygame.image.load(r"./player (2).png"), bx, by)
                            pygame.display.update()
                        if ladders_check(c_position_b) != c_position_b:
                            c_position_b = ladders_check(c_position_b)
                            bx,by = position[c_position_b][0], position[c_position_b][1]
                            imageplacement(pygame.image.load(r"./player (2).png"), bx, by)
                            pygame.display.update()
                            
                if c_position_b >= 100 or c_position_r >= 100:
                    if c_position_r >= 100:
                        draw_text(" PLAYER RED IS THE WINNER ", pygame.font.SysFont("times new roman", 40), (255,255,255), 150, 230)
                        pygame.display.update()
                        print("PLAYER RED is the winner....")
                        time.sleep(2.3)
                    else:
                        draw_text(" PLAYER BLUE IS THE WINNER  ", pygame.font.SysFont("times new roman", 40), (255,255,255), 150, 230)
                        pygame.display.update()
                        print("PLAYER BLUE is the winner....")
                        time.sleep(2.3)
                    running = False
        pygame.display.update()

start_image = pygame.image.load(r"./—Pngtree—play button candy blue_5306396.png").convert_alpha()
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
