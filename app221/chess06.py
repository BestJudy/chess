############################################
#       chess06.py
#
#   https://github.com/BestJudy/chess
############################################
import pygame
import numpy as np
import random
from app03_cloudh import app221Login, app221GetGameId, app20SaveGame, app221GetGameData, app20CreateGame

__version__ = '0.0.8'

class app221_chess():
    def __init__(self, _id_game, _n_role, _name):
        self.id_game, self.n_role = _id_game, _n_role
        self.state_oneline = 100    # offline
        pygame.init()

        self.win = pygame.display.set_mode((1000, 800))

        pygame.display.set_caption("Chess " + __version__)

        bg_color = pygame.Color('grey12')
        light_grey = (200,200,200)
        self.backround = pygame.image.load('./app221/chessboard.png')
        test_list = ['./app221/another_side_image001.png', './app221/NEW_PANEL_SIDE1.png', './app221/chess_side.png']
        self.bk_side = pygame.image.load(test_list[random.randint(0, 2)])
        
        self.lst_image_names = ['', './app221/bR.png', './app221/bN.png', './app221/bB.png', './app221/bQ.png',
                    './app221/bK.png', './app221/bP.png',
                    './app221/wR.png', './app221/wN.png', './app221/wB.png', './app221/wQ.png',
                    './app221/wK.png', './app221/wP.png']

                    
        self.default_index = [ [1, 2, 3, 4, 5, 3, 2, 1],
                            [6, 6, 6, 6, 6, 6, 6, 6],
                            [-0, -0, -0, -0, -0, -0, 0, 0],
                            [-0, -0, -0, -0, -0, -0, 0, 0],
                            [-0, -0, -0, -0, -0, -0, 0, 0],
                            [-0, -0, -0, -0, -0, -0, 0, 0],
                            [12, 12, 12, 12, 12, 12, 12, 12],
                            [7, 8, 9, 10, 11, 9, 8, 7]
            ]
        self.position_okay = np.zeros((8, 8))

        self.lst_image_index = np.array(self.default_index)
        self.turn = 1
        self.player1 = pygame.image.load(self.lst_image_names[4])
        self.player2 = pygame.image.load(self.lst_image_names[10])
        self.player1_name = _name
        self.player2_name = _name
        pygame.font.init()
        self.game_font = pygame.font.SysFont('Comic Sans MS', 30)
        
        pass
    def run(self):
        state = 0
        col_selected, row_selected= 0, 0
        chess_selected = 0
        x, y = 0, 0

        RED =       (255,   0,   0)
        BLUE = (0, 0, 255)
        run = True
        while run: 
            
            pygame.time.delay(200)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # LEFT
                        x, y = pygame.mouse.get_pos()
                        #print(x, y)
                        col, row = self.get_chess_position(x, y)
                        #print(col, row)
                        if(col >= 8 or row >= 8):
                            if(self.state_oneline == 200):  # will select black or white seat
                                #print('online select', col, row)
                                if(row == 1 and (col == 8 or col == 9)):
                                    self.id_game, self.n_role, self.player2_name = app221GetGameId(self.player1_name, 1)
                                    #print('  app221GetGameId 1', self.player1_name, self.id_game)
                                    if(self.id_game > 0):
                                        self.state_oneline = 300
                                    else:
                                        app20CreateGame(self.player1_name, 1)
                                elif(row == 6 and (col == 8 or col == 9)):
                                    self.id_game, self.n_role, self.player1_name = app221GetGameId(self.player2_name, 2)
                                    #print('  app221GetGameId 2', self.player2_name, self.id_game)
                                    if(self.id_game > 0):
                                        self.state_oneline = 300
                                    else:
                                        app20CreateGame(self.player2_name, 2)
                        elif state == 0:
                            b_legal = False
                            a_chess = self.lst_image_index[row][col]
                            if(self.n_role == 1 ):
                                if(a_chess >= 1 and a_chess <= 6):
                                    b_legal = True
                            if(self.n_role == 2 ):
                                if(a_chess >= 7 and a_chess <= 12):
                                    b_legal = True
                            if(b_legal):
                                state = 1
                                col_selected, row_selected= col, row
                        elif state == 3:
                            if(self.n_role == self.turn):
                                state = 4
                                col_selected, row_selected= col, row
                            else:
                                state = 0
                        #lst_image_index[row][col] = -lst_image_index[row][col] 
                elif event.type == pygame.MOUSEBUTTONUP:
                        x, y = pygame.mouse.get_pos()
                        col, row = self.get_chess_position(x, y)
                        if(col >= 8 or row >= 8):
                            pass
                        elif state == 1:
                            state = 2
                            chess_selected = self.lst_image_index[row_selected][col_selected]
                            self.lst_image_index[row_selected][col_selected] = 0
                            self.chess_rule(chess_selected, col_selected, row_selected)
                        elif state == 4:
                            state = 5
                            self.lst_image_index[row][col] = chess_selected
                            #if self.position_okay[row][col] == 1:
                                #self.lst_image_index[row][col] = chess_selected
                            #else: 
                                #state=0
                                #self.lst_image_index[row_selected][col_selected] = chess_selected
                        #lst_image_index[row][col] = lst_image_index[row][col] 
                elif event.type == pygame.MOUSEMOTION:
                        x, y = pygame.mouse.get_pos()
                        if state == 2:
                            state = 3
                        elif state == 5:
                            a_str = ' '.join(map(str,(self.lst_image_index)))
                            # print(b_str)
                            app20SaveGame(self.id_game, a_str, self.n_role )
                            state= 0
                            if(self.state_oneline == 100):
                                self.turn = self.n_role = 3 - self.n_role
                                pass
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # right
                    state = 0
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    
                    self.lst_image_index = np.array(self.default_index)
                    a_str = ' '.join(map(str,(self.lst_image_index)))
                    app20SaveGame(self.id_game, a_str )
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_l:
                    
                    self.state_oneline = 200    # online
                    self.n_role, self.turn = 0, 0

            self.display_side()
            self.display_chess()
            
            if state == 2 or state == 3:
                self.display_rule()
            if state == 1 or state == 2 or state == 3:
                pygame.draw.circle(self.win, RED , (col_selected *100+50, row_selected * 100+50), 20)
                
            if state == 3:
                if chess_selected > 0:
                    bQ= pygame.image.load(self.lst_image_names[chess_selected])
                    self.win.blit(bQ, (x-50, y-50))
            if state == 4:
                pygame.draw.circle(self.win, BLUE , (col_selected *100+50, row_selected * 100+50), 20)
            
            if state == 0:
                if(self.id_game > 0):
                    ret_arr, self.turn = app221GetGameData(self.id_game)
                    if(ret_arr.shape == (8,8)):
                        self.lst_image_index = ret_arr
                s_title = 'Chess ' +  __version__ + ', I use '
                if(self.n_role == 1):
                    s_title += 'Black piece'
                elif(self.n_role == 2):
                    s_title += 'White piece'
                if(self.turn == self.n_role):
                    s_title += ", my turn"
                elif(self.turn == 1):
                    s_title += ", Black's turn"
                elif(self.turn == 2):
                    s_title += ", White's turn"
                pygame.display.set_caption(s_title)
            pygame.display.update()
            

        pygame.quit()
        pass
    def piece_draw_hint(self, col, row):
        WHITE = (255,255,255)
        pygame.draw.circle(self.win, WHITE , (col *100+50, row * 100+50), 20, 3)
        
        self.position_okay[row][col] = 1
        #print(self.position_okay)
    def chess_rule(self, piece, col_selected, row_selected):
        self.position_okay = np.zeros((8, 8))
        #self.lst_image_index
        WHITE = (255,255,255)
        # white rook 
        if piece == 1 or piece == 7:
            print('piece', piece, col_selected, row_selected)
            for i in range(8):
                self.position_okay[row_selected][i] = 1
                self.position_okay[i][col_selected] = 1
            self.position_okay[row_selected][col_selected] = 0
        # white knight
        if piece == 2 or piece == 8:
            for i in range(1,3):
                a_row, a_col = row_selected+i, col_selected+(3-i)
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    self.position_okay[a_row][a_col] = 1
                a_row, a_col = row_selected-i, col_selected-(3-i)
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    self.position_okay[a_row][a_col] = 1
                a_row, a_col = row_selected+i, col_selected-(3-i)
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    self.position_okay[a_row][a_col] = 1
                a_row, a_col = row_selected-i, col_selected+(3-i)
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    self.position_okay[a_row][a_col] = 1
            self.position_okay[row_selected][col_selected] = 0
        # white bishop
        if piece == 3 or piece == 9:
            for i in range(8):
                a_row, a_col = row_selected+i, col_selected+i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    self.position_okay[a_row][a_col] = 1
                a_row, a_col = row_selected+i, col_selected-i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    self.position_okay[a_row][a_col] = 1
                a_row, a_col = row_selected-i, col_selected+i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    self.position_okay[a_row][a_col] = 1
                a_row, a_col = row_selected-i, col_selected-i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    self.position_okay[a_row][a_col] = 1
            self.position_okay[row_selected][col_selected] = 0
            
        # white queen
        if piece == 4 or piece == 10:
            #pygame.draw.circle(self.win, WHITE , ((col_selected) *100+50, (row_selected) * 100+50), 20)
            for i in range(0, 8):
                self.position_okay[row_selected][i] = 1
                self.position_okay[i][col_selected] = 1
                a_row, a_col = row_selected+i, col_selected+i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    self.position_okay[a_row][a_col] = 1
                a_row, a_col = row_selected+i, col_selected-i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    self.position_okay[a_row][a_col] = 1
                a_row, a_col = row_selected-i, col_selected+i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    self.position_okay[a_row][a_col] = 1
                a_row, a_col = row_selected-i, col_selected-i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    self.position_okay[a_row][a_col] = 1
            self.position_okay[row_selected][col_selected] = 0

        # white king
        if piece == 5 or piece == 11:
            for i in range(1, 2):
                a_row, a_col = row_selected+i, col_selected+0
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    self.position_okay[a_row][a_col] = 1
                a_row, a_col = row_selected-i, col_selected+0
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    self.position_okay[a_row][a_col] = 1
                a_row, a_col = row_selected+0, col_selected+i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    self.position_okay[a_row][a_col] = 1
                a_row, a_col = row_selected+0, col_selected-i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    self.position_okay[a_row][a_col] = 1
                a_row, a_col = row_selected+i, col_selected+i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    self.position_okay[a_row][a_col] = 1
                a_row, a_col = row_selected+i, col_selected-i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    self.position_okay[a_row][a_col] = 1
                a_row, a_col = row_selected-i, col_selected+i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    self.position_okay[a_row][a_col] = 1
                a_row, a_col = row_selected-i, col_selected-i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    self.position_okay[a_row][a_col] = 1
            self.position_okay[row_selected][col_selected] = 0
        # white pawn
        if piece == 12:
            if True:
                a_row, a_col = row_selected-1, col_selected
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    self.position_okay[a_row][a_col] = 1
                a_row, a_col = row_selected-2, col_selected
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    self.position_okay[a_row][a_col] = 1
        # black pawn
        if piece == 6:
            if True:
                a_row, a_col = row_selected+1, col_selected
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    self.position_okay[a_row][a_col] = 1
                a_row, a_col = row_selected+2, col_selected
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    self.position_okay[a_row][a_col] = 1
    def display_side(self):
        self.win.blit(self.backround, (0, 0))
        self.win.blit(self.bk_side, (790, 0))  
        if(self.state_oneline == 100 or self.state_oneline == 300):     
            if(self.turn == 1): 
                self.win.blit(self.player1, (850+10, 50+10))   
                g_msg2 = self.game_font.render('My Turn', False, (255, 255, 255))
                self.win.blit(g_msg2, (850+10, 150+10)) 
            elif(self.turn == 2):     
                self.win.blit(self.player2, (850+10, 650+10))
                g_msg2 = self.game_font.render('My Turn', False, (255, 255, 255))
                self.win.blit(g_msg2, (850+10, 600+10))                 
            
        elif(self.state_oneline == 200):
            self.win.blit(self.player1, (850+10, 50+10))
            g_msg2 = self.game_font.render('I select black', False, (255, 0, 0))
            self.win.blit(g_msg2, (820+10, 150+10)) 
            self.win.blit(self.player2, (850+10, 650+10))
            g_msg2 = self.game_font.render('I select white', False, (255, 0, 0))
            self.win.blit(g_msg2, (820+10, 600+10))
            
        if(self.state_oneline <= 100):
            g_msg3 = self.game_font.render('Offline', False, (255, 255, 0))
        else:
            g_msg3 = self.game_font.render('Online', False, (255, 255, 0))
        if(self.state_oneline != 200):
            g_msg1 = self.game_font.render(self.player1_name.split('@')[0], False, (255, 255, 255))
            self.win.blit(g_msg1, (850+10, 10+10))
            g_msg1 = self.game_font.render(self.player2_name.split('@')[0], False, (255, 255, 255))
            self.win.blit(g_msg1, (850+10, 750+10))
            
        self.win.blit(g_msg3, (850+10, 400+10)) 
    def display_chess(self):
        for row in range(8):
            for col in range(len(self.lst_image_index[row])):
                if(self.lst_image_index[row][col] > 0): 
                    #print(lst_image_index[row][col])
                    bQ= pygame.image.load(self.lst_image_names[self.lst_image_index[row][col]])
                    self.win.blit(bQ, ((col)*100+10, 10 + 100*(row)))
                    #print((ii%8)*100+10, 10 + 100*(ii//8))

    def display_rule(self):
        WHITE = (255,255,255)
        for row in range(8):
            for col in range(len(self.position_okay[row])):
                if(self.position_okay[row][col] > 0): 
                    
                    pygame.draw.circle(self.win, WHITE , (col *100+50, row * 100+50), 20, 3)

    #given a mouse position to get col and row
    def get_chess_position(self, x, y):
        col, row= 0, 0
        col = x//100
        row = y//100
        return col, row

app221 = app221_chess(0, 1, 'lunawyh@gmail.com')
    
app221.run()
'''
# now starting game, lunawyh: 2, bestjudyw: 1
user_name = 'lunawyh@gmail.com'
user_password = ''
ret =  app221Login(user_name, user_password)

'''