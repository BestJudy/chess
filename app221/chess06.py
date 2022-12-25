############################################
#       chess06.py
#
#   https://github.com/BestJudy/chess
############################################
import pygame
import numpy as np
from app03_cloudh import app221Login, app221GetGameId, app20SaveGame, app221GetGameData

__version__ = '0.0.8'

class app221_chess():
    def __init__(self, _id_game, _n_role):
        self.id_game, self.n_role = _id_game, _n_role
        self.state_oneline = 100    # offline
        pygame.init()

        self.win = pygame.display.set_mode((800, 800))

        pygame.display.set_caption("Chess " + __version__)

        bg_color = pygame.Color('grey12')
        light_grey = (200,200,200)
        self.backround = pygame.image.load('./app221/chessboard.png')
        self.win.blit(self.backround, (0, 0))

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

        self.lst_image_index = np.array(self.default_index)
        self.turn = 1
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
                        col_1, row_1 = self.get_chess_position(x, y)
                        #print(col, row)
                        if state == 0:
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
                        if state == 1:
                            state = 2
                            chess_selected = self.lst_image_index[row_selected][col_selected]
                            self.lst_image_index[row_selected][col_selected] = 0
                        elif state == 4:
                            state = 5
                            #print(chess_selected )
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
                    user_name = 'bestjudyw@gmail.com'
                    self.id_game, self.n_role = app221GetGameId(user_name)
                    self.state_oneline = 200    # online

            self.display_chess()
            if state == 1 or state == 2 or state == 3:
                pygame.draw.circle(self.win, RED , (col_selected *100+50, row_selected * 100+50), 20)
                self.chess_rule(chess_selected, col_selected, row_selected)
            if state == 3:
                if chess_selected > 0:
                    bQ= pygame.image.load(self.lst_image_names[chess_selected])
                    self.win.blit(bQ, (x-50, y-50))
            if state == 4:
                pygame.draw.circle(self.win, BLUE , (col_selected *100+50, row_selected * 100+50), 20)
            
            if state == 0:
                if(self.id_game > 0):
                    self.lst_image_index, self.turn = app221GetGameData(self.id_game)
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
        self.position_okay = [ [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0]
            ]
        #self.lst_image_index
        WHITE = (255,255,255)
        # white rook 
        if piece == 7:
            up_number_range_col = row_selected+1
            right_number_range_row = col_selected+1
            down_number_range_col = 7 - row_selected+1
            left_number_range_row = 7 - col_selected+1

            for i in range(1, up_number_range_col):
                #pygame.draw.circle(self.win, WHITE , ((col_selected) *100+50, (row_selected-i) * 100+50), 20, 3)
                self.piece_draw_hint(col_selected, row_selected-i)
            for i in range(1, right_number_range_row):
                self.piece_draw_hint(col_selected-i, row_selected)
            for i in range (1, left_number_range_row):
                self.piece_draw_hint(col_selected+i, row_selected)
            for i in range (1, down_number_range_col):
                self.piece_draw_hint(col_selected, row_selected+i)
        # white knight
        if piece == 8:
            pygame.draw.circle(self.win, WHITE , ((col_selected-1) *100+50, (row_selected-2) * 100+50), 20, 3)
            pygame.draw.circle(self.win, WHITE , ((col_selected-2) *100+50, (row_selected-1) * 100+50), 20, 3)
            pygame.draw.circle(self.win, WHITE , ((col_selected+1) *100+50, (row_selected-2) * 100+50), 20, 3)
            pygame.draw.circle(self.win, WHITE , ((col_selected+2) *100+50, (row_selected-1) * 100+50), 20, 3)
            pygame.draw.circle(self.win, WHITE , ((col_selected-2) *100+50, (row_selected+1) * 100+50), 20, 3)
            pygame.draw.circle(self.win, WHITE , ((col_selected+2) *100+50, (row_selected+1) * 100+50), 20, 3)
            pygame.draw.circle(self.win, WHITE , ((col_selected-1) *100+50, (row_selected+2) * 100+50), 20, 3)
            pygame.draw.circle(self.win, WHITE , ((col_selected+1) *100+50, (row_selected+2) * 100+50), 20, 3)
        # white bishop
        if piece == 9:
            #pygame.draw.circle(self.win, WHITE , ((col_selected) *100+50, (row_selected) * 100+50), 20)
            for i in range(1, 8):
                pygame.draw.circle(self.win, WHITE , ((col_selected-i) *100+50, (row_selected-i) * 100+50), 20, 3)
                pygame.draw.circle(self.win, WHITE , ((col_selected+i) *100+50, (row_selected-i) * 100+50), 20, 3)
                pygame.draw.circle(self.win, WHITE , ((col_selected+i) *100+50, (row_selected+i) * 100+50), 20, 3)
                pygame.draw.circle(self.win, WHITE , ((col_selected-i) *100+50, (row_selected+i) * 100+50), 20, 3)
        # white queen
        if piece == 10:
            #pygame.draw.circle(self.win, WHITE , ((col_selected) *100+50, (row_selected) * 100+50), 20)
            for i in range(1, 8):
                pygame.draw.circle(self.win, WHITE , ((col_selected) *100+50, (row_selected-i) * 100+50), 20, 3)
                pygame.draw.circle(self.win, WHITE , ((col_selected-i) *100+50, (row_selected) * 100+50), 20, 3)
                pygame.draw.circle(self.win, WHITE , ((col_selected) *100+50, (row_selected+i) * 100+50), 20, 3)
                pygame.draw.circle(self.win, WHITE , ((col_selected+i) *100+50, (row_selected) * 100+50), 20, 3)
                pygame.draw.circle(self.win, WHITE , ((col_selected-i) *100+50, (row_selected-i) * 100+50), 20, 3)
                pygame.draw.circle(self.win, WHITE , ((col_selected+i) *100+50, (row_selected-i) * 100+50), 20, 3)
                pygame.draw.circle(self.win, WHITE , ((col_selected+i) *100+50, (row_selected+i) * 100+50), 20, 3)
                pygame.draw.circle(self.win, WHITE , ((col_selected-i) *100+50, (row_selected+i) * 100+50), 20, 3)
        # white king
        if piece == 11:
            pygame.draw.circle(self.win, WHITE , ((col_selected-1) *100+50, (row_selected-1) * 100+50), 20, 3)
            pygame.draw.circle(self.win, WHITE , ((col_selected) *100+50, (row_selected-1) * 100+50), 20, 3)
            pygame.draw.circle(self.win, WHITE , ((col_selected+1) *100+50, (row_selected-1) * 100+50), 20, 3)
            pygame.draw.circle(self.win, WHITE , ((col_selected+1) *100+50, (row_selected) * 100+50), 20, 3)
            pygame.draw.circle(self.win, WHITE , ((col_selected-1) *100+50, (row_selected) * 100+50), 20, 3)
            pygame.draw.circle(self.win, WHITE , ((col_selected+1) *100+50, (row_selected+1) * 100+50), 20, 3)
            pygame.draw.circle(self.win, WHITE , ((col_selected) *100+50, (row_selected+1) * 100+50), 20, 3)
            pygame.draw.circle(self.win, WHITE , ((col_selected-1) *100+50, (row_selected+1) * 100+50), 20, 3)
        # white pawn
        if piece == 12:
            pygame.draw.circle(self.win, WHITE , ((col_selected) *100+50, (row_selected-1) * 100+50), 20, 3)
            pygame.draw.circle(self.win, WHITE , ((col_selected) *100+50, (row_selected-2) * 100+50), 20, 3)

    def display_chess(self):
        self.win.blit(self.backround, (0, 0))
        for row in range(8):
            for col in range(len(self.lst_image_index[row])):
                if(self.lst_image_index[row][col] > 0): 
                    #print(lst_image_index[row][col])
                    bQ= pygame.image.load(self.lst_image_names[self.lst_image_index[row][col]])
                    self.win.blit(bQ, ((col)*100+10, 10 + 100*(row)))
                    #print((ii%8)*100+10, 10 + 100*(ii//8))

    #given a mouse position to get col and row
    def get_chess_position(self, x, y):
        col, row= 0, 0
        col = x//100
        row = y//100
        return col, row

app221 = app221_chess(0, 1)
    
app221.run()
'''
# now starting game, lunawyh: 2, bestjudyw: 1
user_name = 'lunawyh@gmail.com'
user_password = ''
ret =  app221Login(user_name, user_password)

'''