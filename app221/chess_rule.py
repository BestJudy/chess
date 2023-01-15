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
    def getLegal(self, piece, col_selected, row_selected):
        l_legal = np.zeros((8, 8))
        # white rook 
        if piece == 1 or piece == 7:
            #print('piece', piece, col_selected, row_selected)
            for i in range(8):
                l_legal[row_selected][i] = 1
                l_legal[i][col_selected] = 1
            l_legal[row_selected][col_selected] = 0
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
            for i in range(8):
                a_row, a_col = row_selected+i, col_selected+i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
                a_row, a_col = row_selected+i, col_selected-i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
                a_row, a_col = row_selected-i, col_selected+i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
                a_row, a_col = row_selected-i, col_selected-i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
            l_legal[row_selected][col_selected] = 0
            
        # white queen
        if piece == 4 or piece == 10:
            #pygame.draw.circle(self.win, WHITE , ((col_selected) *100+50, (row_selected) * 100+50), 20)
            for i in range(0, 8):
                l_legal[row_selected][i] = 1
                l_legal[i][col_selected] = 1
                a_row, a_col = row_selected+i, col_selected+i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
                a_row, a_col = row_selected+i, col_selected-i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
                a_row, a_col = row_selected-i, col_selected+i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
                a_row, a_col = row_selected-i, col_selected-i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
            l_legal[row_selected][col_selected] = 0

        # white king
        if piece == 5 or piece == 11:
            for i in range(1, 2):
                a_row, a_col = row_selected+i, col_selected+0
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
                a_row, a_col = row_selected-i, col_selected+0
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
                a_row, a_col = row_selected+0, col_selected+i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
                a_row, a_col = row_selected+0, col_selected-i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
                a_row, a_col = row_selected+i, col_selected+i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
                a_row, a_col = row_selected+i, col_selected-i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
                a_row, a_col = row_selected-i, col_selected+i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
                a_row, a_col = row_selected-i, col_selected-i
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
            l_legal[row_selected][col_selected] = 0
        # white pawn
        if piece == 12:
            if True:
                a_row, a_col = row_selected-1, col_selected
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
                a_row, a_col = row_selected-2, col_selected
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
        # black pawn
        if piece == 6:
            if True:
                a_row, a_col = row_selected+1, col_selected
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
                a_row, a_col = row_selected+2, col_selected
                if(a_row <= 7 and a_row >= 0 and a_col <= 7 and a_col >= 0):
                    l_legal[a_row][a_col] = 1
        return l_legal
'''
END OF THE FILE
'''