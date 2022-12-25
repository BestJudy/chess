import pygame

pygame.init()

win = pygame.display.set_mode((800, 800))

pygame.display.set_caption("Chess")

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)
RED =       (255,   0,   0)
BLUE = (0, 0, 255)
backround = pygame.image.load('./app221/chessboard.png')
win.blit(backround, (0, 0))

lst_image_names = ['', './app221/bR.png', './app221/bN.png', './app221/bB.png', './app221/bQ.png',
            './app221/bK.png', './app221/bP.png',
            './app221/wR.png', './app221/wN.png', './app221/wB.png', './app221/wQ.png',
            './app221/wK.png', './app221/wP.png']

            
lst_image_index = [ [1, 2, 3, 4, 5, 3, 2, 1],
                    [6, 6, 6, 6, 6, 6, 6, 6],
                    [-0, -0, -0, -0, -0, -0, 0, 0],
                    [-0, -0, -0, -0, -0, -0, 0, 0],
                    [-0, -0, -0, -0, -0, -0, 0, 0],
                    [-0, -0, -0, -0, -0, -0, 0, 0],
                    [12, 12, 12, 12, 12, 12, 12, 12],
                    [7, 8, 9, 10, 11, 9, 8, 7]
    ]
'''
for i in range(len(x)):
        for col in range(len(x[i])):
                print(x[i][col])

'''
#print(lst_image_index.shape)
def display_chess():
    win.blit(backround, (0, 0))
    for row in range(8):
        for col in range(len(lst_image_index[row])):
            if(lst_image_index[row][col] > 0): 
                #print(lst_image_index[row][col])
                bQ= pygame.image.load(lst_image_names[lst_image_index[row][col]])
                win.blit(bQ, ((col)*100+10, 10 + 100*(row)))
                #print((ii%8)*100+10, 10 + 100*(ii//8))

#given a mouse position to get col and row
def get_chess_position(x, y):
    col, row= 0, 0
    col = x//100
    row = y//100
    return col, row

state = 0
col_selected, row_selected= 0, 0
chess_selected = 0
x, y = 0, 0

run = True
while run: 
    
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(x, y)
                col, row = get_chess_position(x, y)
                print(col, row)
                if state == 0:
                    state = 1
                    col_selected, row_selected= col, row
                elif state == 3:
                    state = 4
                    col_selected, row_selected= col, row
                #lst_image_index[row][col] = -lst_image_index[row][col] 
        elif event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                col, row = get_chess_position(x, y)
                if state == 1:
                    state = 2
                    chess_selected = lst_image_index[row_selected][col_selected]
                    lst_image_index[row_selected][col_selected] = 0
                elif state == 4:
                    state = 5
                    lst_image_index[row][col] = chess_selected
                #lst_image_index[row][col] = lst_image_index[row][col] 
        elif event.type == pygame.MOUSEMOTION:
                x, y = pygame.mouse.get_pos()
                if state == 2:
                    state = 3
                elif state == 5:
                    state= 0

    #Mouse_x, Mouse_y = pygame.mouse.get_pos()
    #col , row = get_chess_position(Mouse_x, Mouse_y)
    #print(get_chess_position(Mouse_x, Mouse_y))
    display_chess()
    if state == 1:
        pygame.draw.circle(win, RED , (col_selected *100+50, row_selected * 100+50), 20)
    if state == 2 or state == 3:
        if chess_selected > 0:
            bQ= pygame.image.load(lst_image_names[chess_selected])
            win.blit(bQ, (x-50, y-50))
    if state == 4:
        pygame.draw.circle(win, BLUE , (col_selected *100+50, row_selected * 100+50), 20)
    key = pygame.key.get_pressed()
    #print(Mouse_x, Mouse_y)
    pygame.display.update()
    

pygame.quit()