############################################
#       chess_rule.py
#
#   https://github.com/BestJudy/chess
#     git reset --hard
#     git pull
############################################
import numpy as np


class chess_rule():
    def __init__(self):
        pass
    # select all pieces in the format of plus
    def getFormatPlus(self, l_legal, col_selected, row_selected, l_chess, n_step=8):
        if(True):
            for i in range(1, n_step):
                a_row, a_col = row_selected+i, col_selected+0
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
                    if(l_chess[a_row][a_col] > 0): break
            for i in range(1, n_step):
                a_row, a_col = row_selected-i, col_selected-0
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
                    if(l_chess[a_row][a_col] > 0): break
            for i in range(1, n_step):
                a_row, a_col = row_selected-0, col_selected+i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
                    if(l_chess[a_row][a_col] > 0): break
            for i in range(1, n_step):
                a_row, a_col = row_selected-0, col_selected-i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
                    if(l_chess[a_row][a_col] > 0): break
            l_legal[row_selected][col_selected] = 0
        return l_legal
    # select all pieces in the format of X
    def getFormatX(self, l_legal, col_selected, row_selected, l_chess, n_step=8):
        if(True):
            for i in range(1, n_step):
                a_row, a_col = row_selected+i, col_selected+i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
                    if(l_chess[a_row][a_col] > 0): break
            for i in range(1, n_step):
                a_row, a_col = row_selected+i, col_selected-i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
                    if(l_chess[a_row][a_col] > 0): break
            for i in range(1, n_step):
                a_row, a_col = row_selected-i, col_selected+i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
                    if(l_chess[a_row][a_col] > 0): break
            for i in range(1, n_step):
                a_row, a_col = row_selected-i, col_selected-i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
                    if(l_chess[a_row][a_col] > 0): break
            l_legal[row_selected][col_selected] = 0
        return l_legal
    def getLegal(self, piece, col_selected, row_selected, l_chess):
        l_legal = np.zeros((8, 8))
        # white rook 
        if piece == 1 or piece == 7:
            l_legal = self.getFormatPlus(l_legal, col_selected, row_selected, l_chess)
        # white knight
        if piece == 2 or piece == 8:
            for i in range(1,3):
                a_row, a_col = row_selected+i, col_selected+(3-i)
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
                a_row, a_col = row_selected-i, col_selected-(3-i)
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
                a_row, a_col = row_selected+i, col_selected-(3-i)
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
                a_row, a_col = row_selected-i, col_selected+(3-i)
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
            l_legal[row_selected][col_selected] = 0
        # white bishop
        if piece == 3 or piece == 9:
            l_legal = self.getFormatX(l_legal, col_selected, row_selected, l_chess)
            
        # white queen
        if piece == 4 or piece == 10:
            l_legal = self.getFormatPlus(l_legal, col_selected, row_selected, l_chess)
            l_legal = self.getFormatX(l_legal, col_selected, row_selected, l_chess)
        # white king
        if piece == 5 or piece == 11:
            l_legal = self.getFormatPlus(l_legal, col_selected, row_selected, l_chess, 2)
            l_legal = self.getFormatX(l_legal, col_selected, row_selected, l_chess, 2)
        # white pawn
        if piece == 12:
            for i in range(1,3):
                a_row, a_col = row_selected-i, col_selected
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
                if(l_chess[a_row][a_col] > 0): break
        # black pawn
        if piece == 6:
            for i in range(1,3):
                a_row, a_col = row_selected+i, col_selected
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
                if(l_chess[a_row][a_col] > 0): break
        return l_legal
'''
END OF THE FILE
'''