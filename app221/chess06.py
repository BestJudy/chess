import pygame
import numpy as np
from app03_cloudh import app221Login, app221GetGameId, app20SaveGame, app221GetGameData

__version__ = '0.0.6'

class app221_chess():
    def __init__(self, _id_game, _n_role):
        self.id_game, self.n_role = _id_game, _n_role
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
                            state = 4
                            col_selected, row_selected= col, row
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
                            self.lst_image_index[row][col] = chess_selected
                        #lst_image_index[row][col] = lst_image_index[row][col] 
                elif event.type == pygame.MOUSEMOTION:
                        x, y = pygame.mouse.get_pos()
                        if state == 2:
                            state = 3
                        elif state == 5:
                            a_str = ' '.join(map(str,(self.lst_image_index)))
                            # print(b_str)
                            app20SaveGame(self.id_game, a_str )
                            state= 0
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # right
                    state = 0
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                    
                    self.lst_image_index = np.array(self.default_index)
                    a_str = ' '.join(map(str,(self.lst_image_index)))
                    app20SaveGame(self.id_game, a_str )

            self.display_chess()
            if state == 1 or state == 2 or state == 3:
                pygame.draw.circle(self.win, RED , (col_selected *100+50, row_selected * 100+50), 20)
            if state == 3:
                if chess_selected > 0:
                    bQ= pygame.image.load(self.lst_image_names[chess_selected])
                    self.win.blit(bQ, (x-50, y-50))
            if state == 4:
                pygame.draw.circle(self.win, BLUE , (col_selected *100+50, row_selected * 100+50), 20)
            
            if state == 0:
                self.lst_image_index = app221GetGameData(self.id_game)
            pygame.display.update()
            

        pygame.quit()
        pass


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

# now starting game        
user_name = 'bestjudyw@gmail.com'
user_password = 'hi'
ret =  app221Login(user_name, user_password)
if(ret == 200):
    id_game, n_role = app221GetGameId(user_name)
    app221 = app221_chess(id_game, n_role)
    app221.run()