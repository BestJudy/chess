#!/usr/bin/env python
# -*- coding: utf8 -*-
# 			app04_input.py
#
#   https://github.com/BestJudy/chess
#
# 
import pygame
import sys
import os
import random

def readPlayer():
    chess_f = './app221/chess06.txt'
    if(os.path.exists(chess_f)):
        with open(chess_f) as f:
            settings = f.readlines()
        for a_line in settings:
            l_line = a_line.split(':')
            if(l_line[0] == 'player1'):
                chess_player = l_line[1]
                return chess_player
    return ''
def savePlayer(account):
    chess_f = './app221/chess06.txt'
    with open(chess_f, 'w') as f:
        f.write('player1:' + account)
    pass
def chess_login():
    # pygame.init() will initialize all
    # imported module
    pygame.init()
    clock = pygame.time.Clock()
    # it will display on screen
    screen = pygame.display.set_mode([800, 800])
    pygame.display.set_caption( "Chess Player" )
    # basic font for user typed
    base_font = pygame.font.Font(None, 32)
    user_text = readPlayer()
    # create rectangle
    input_rect = pygame.Rect(100, 200, 400, 32)
    # color_active stores color(lightskyblue3) which
    # gets active when input box is clicked by user
    color_active = pygame.Color('lightskyblue3')
    # color_passive store color(chartreuse4) which is
    # color of input box.
    color_passive = pygame.Color('chartreuse4')
    color = color_passive
    active = False

    while True:
        for event in pygame.event.get():
            # if user types QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                #sys.exit()
                if(('@' in user_text)):
                    pass
                else:
                    user_text = 'chess' + str(random.randrange(1000, 9999)) + '@gmail.com'
                savePlayer(user_text)
                return user_text 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
                    if( event.button == 1 ):
                        x, y = pygame.mouse.get_pos()
                        if(x > 300 and x < 500 and y > 400 and y < 500 and ('@' in user_text)):
                            savePlayer(user_text)
                            return user_text
                        pass
            if event.type == pygame.KEYDOWN:
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
                # Unicode standard is used for string
                # formation
                else:
                    user_text += event.unicode
        
        # it will set background color of screen
        screen.fill((255, 255, 255))
        # part 1: input window
        if active:
            color = color_active
        else:
            color = color_passive
        # draw rectangle and argument passed which should
        # be on screen
        pygame.draw.rect(screen, color, input_rect)
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        # render at position stated in arguments
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        # set width of textfield so that text cannot get
        # outside of user's text input
        input_rect.w = max(100, text_surface.get_width()+10)
        # part 2: command text
        g_msg2 = base_font.render("Input your email as a player's account:", False, (0, 0, 255))
        screen.blit(g_msg2, (100, 150)) 
        # part 3: button
        g_msg2 = base_font.render("Click to Enter Game", False, (255, 0, 0))
        screen.blit(g_msg2, (300, 400)) 
        
        # display.flip() will update only a portion of the
        # screen to updated, not full area
        pygame.display.flip()
        
        # clock.tick(60) means that for every second at most
        # 60 frames should be passed.
        clock.tick(60)
    return user_text

