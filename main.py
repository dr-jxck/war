import pygame
import time
from sys import exit
import os

#Setup
os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.init()
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()
screen.fill("Black")
global winner
blue_freeze = False
game_active = False
blue_fire = False
red_fire = False
blue_points = 0
red_points = 0
blue_wins = 0
red_wins = 0
bullet_speed = 50

background = pygame.image.load("assets/background.png")
biggerfont = pygame.font.Font("assets/Pixeltype.ttf",75)
font = pygame.font.Font("assets/Pixeltype.ttf",70)
smallfont = pygame.font.Font("assets/Pixeltype.ttf",40)
smallerfont = pygame.font.Font("assets/Pixeltype.ttf",30)
tinyfont = pygame.font.Font("assets/Pixeltype.ttf",23)

#Blue Tank
bluetank = pygame.image.load("assets/bluetank.png",).convert_alpha()
bluetank_rec = bluetank.get_rect(midleft = (0,200))
bluebullet = pygame.image.load("assets/bulletleft.webp")
bluebullet_rec = bluebullet.get_rect(midleft = bluetank_rec.midright)

#Red Tank
redtank = pygame.image.load("assets/redtank.png").convert_alpha()
redtank_rec = bluetank.get_rect(midright = (800,200))
redbullet = pygame.image.load("assets/bulletright.webp")
redbullet_rec = redbullet.get_rect(midright = redtank_rec.midleft)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        key = pygame.key.get_pressed()

    if game_active:
        score_counter = font.render(" / ", False, "Purple")
        score_counter_rec = score_counter.get_rect(center = (400,35))
        blue_score_counter = font.render(str(blue_points), False, "Blue")
        blue_score_counter_rec = blue_score_counter.get_rect(midright = score_counter_rec.midleft)
        red_score_counter = font.render(str(red_points), False, "Red")
        red_score_counter_rec = red_score_counter.get_rect(midleft = score_counter_rec.midright)
        
        screen.blit(background,(0,0))
        screen.blit(bluetank,bluetank_rec)
        screen.blit(redtank,redtank_rec)
        screen.blit(bluebullet,bluebullet_rec)
        screen.blit(redbullet,redbullet_rec)
        screen.blit(score_counter,score_counter_rec)
        screen.blit(blue_score_counter,blue_score_counter_rec)
        screen.blit(red_score_counter,red_score_counter_rec)


        if blue_fire:
            bluebullet_rec.right += bullet_speed
            if bluebullet_rec.colliderect(redtank_rec):
                blue_points += 1
                blue_fire = False
                if blue_points > 4:
                    game_active = False
                    winner = "Blue"
                    blue_wins += 1
                bluebullet_rec.midleft = bluetank_rec.midright
            if bluebullet_rec.left >= 800:
                blue_fire = False
                bluebullet_rec.midleft = bluetank_rec.midright

        if red_fire:
            redbullet_rec.right -= bullet_speed
            if redbullet_rec.colliderect(bluetank_rec):
                red_points += 1
                red_fire = False
                if red_points > 4:
                    game_active = False
                    winner = "Red"
                    red_wins += 1
                redbullet_rec.midright = redtank_rec.midleft
            if redbullet_rec.right <= 0:
                red_fire = False
                redbullet_rec.midright = redtank_rec.midleft
        

        if bluetank_rec.top < 0:
            bluetank_rec.top = 0
            bluebullet_rec.midleft = bluetank_rec.midright
        if bluetank_rec.bottom > 400:
            bluetank_rec.bottom = 400
            bluebullet_rec.midleft = bluetank_rec.midright

        if redtank_rec.top < 0:
            redtank_rec.top = 0
            redbullet_rec.midright = redtank_rec.midleft
        if redtank_rec.bottom > 400:
            redtank_rec.bottom = 400
            redbullet_rec.midright = redtank_rec.midleft
        #Blue Movements
        if key[pygame.K_a]:
            bluetank_rec.top -= 5
            if not blue_fire:
                bluebullet_rec.bottom -= 5
        if key[pygame.K_d]:
            bluetank_rec.bottom += 5
            if not blue_fire:
                bluebullet_rec.top += 5
        if key[pygame.K_w]:
            blue_fire = True

        #Red Movements
        if key[pygame.K_LEFT]:
            redtank_rec.top -= 5
            if not red_fire:
                redbullet_rec.top -= 5
        if key[pygame.K_RIGHT]:
            redtank_rec.bottom +=5
            if not red_fire:
                redbullet_rec.bottom += 5
        if key[pygame.K_UP]:
            red_fire = True
    else:
        screen.fill("Black")
        if red_points or blue_points:
            if blue_wins > red_wins:
                winning_text = smallfont.render("Blue is winning! "+str(blue_wins)+" to "+str(red_wins), False, "Blue")
            elif red_wins > blue_wins:
                winning_text = smallfont.render("Red is winning! "+str(red_wins)+" to "+str(blue_wins), False, "Red")
            else:
                winning_text = smallfont.render("It's  a tie! "+str(blue_wins)+" to "+str(red_wins), False, "Purple")
            winner_text = font.render(winner+" wins!", False, winner)
            winner_text_rec = winner_text.get_rect(center = (400,100))
            restart = smallerfont.render("Press space to restart", False, "White")
            restart_rec = restart.get_rect(center = (400,300))
            winning_text_rec = winning_text.get_rect(center = (400,225))
            screen.blit(winner_text,winner_text_rec)
            screen.blit(restart,restart_rec)
            screen.blit(winning_text,winning_text_rec)
        else:
            screen.fill("Black")
            logo = tinyfont.render("Jxck Developemnt", True, "Cyan")
            logo_rec = logo.get_rect(bottomright = (800,400))
            title = biggerfont.render("War", False, "Purple")
            title_rec = title.get_rect(center = (400,100))
            start = smallerfont.render("Press space to start", False, "White")
            start_rec = start.get_rect(center = (400,300))
            screen.blit(logo,logo_rec)
            screen.blit(title,title_rec)
            screen.blit(start,start_rec)
        if key[pygame.K_SPACE]:
            bluetank_rec.midleft = 0,200
            bluebullet_rec.midleft = bluetank_rec.midright
            blue_points = 0
            redtank_rec.midright = 800,200
            redbullet_rec.midright = redtank_rec.midleft
            red_points = 0
            game_active = True

    pygame.display.update()
    clock.tick(30)