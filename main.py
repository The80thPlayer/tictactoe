import pygame
import os
import colors
pygame.init()

FPS = 60

WIDTH = 600
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

X_O_FONT = pygame.font.SysFont('comicsans', 150)
WINNER_FONT = pygame.font.SysFont('comicsans', 60)

BOARD_IMAGE = pygame.image.load(
    os.path.join('Assets', 'ultimate-tic-tac-toe12-01.webp')
)
BOARD = pygame.transform.scale(BOARD_IMAGE, [WIDTH, HEIGHT])

X_WIN = pygame.USEREVENT + 1
O_WIN = pygame.USEREVENT + 2
DRAW = pygame.USEREVENT + 3

def draw_board(board):
    board_objects = ["","","","","","","","",""]
    for square in range(0,len(board)):
        board_objects[square] = X_O_FONT.render(board[square], 1, colors.BLACK)
    return board_objects

def draw_window(board):
    WIN.fill(colors.WHITE)
    WIN.blit(BOARD, [0,0])
    
    board_objects = draw_board(board)
    WIN.blit(board_objects[0], (30, 15))
    WIN.blit(board_objects[1], ((WIDTH//3) + 30,15))
    WIN.blit(board_objects[2], (2*(WIDTH//3) + 30,15))
    
    WIN.blit(board_objects[3], (30, (HEIGHT//3) + 5))
    WIN.blit(board_objects[4], ((WIDTH//3) + 30,(HEIGHT//3) + 5))
    WIN.blit(board_objects[5], (2*(WIDTH//3) + 30,(HEIGHT//3) + 5))
    
    WIN.blit(board_objects[6], (30, 2*(HEIGHT//3) + 5))
    WIN.blit(board_objects[7], ((WIDTH//3) + 30, 2*(HEIGHT//3) + 5))
    WIN.blit(board_objects[8], (2*(WIDTH//3) + 30, 2*(HEIGHT//3) + 5))
    
    pygame.display.update()
    
def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1 , colors.GREEN)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def horizontalCheck(board):
    if((board[0] == "X" and board[1] == "X" and board[2] == "X") or (board[3] == "X" and board[4] == "X" and board[5] == "X") or (board[6] == "X" and board[7] == "X" and board[8] == "X")):
        return "X win"
    elif((board[0] == "O" and board[1] == "O" and board[2] == "O") or (board[3] == "O" and board[4] == "O" and board[5] == "O") or (board[6] == "O" and board[7] == "O" and board[8] == "O")):
        return "O win"
    else:
        return "0"
    
def verticalCheck(board):
    if((board[0] == "X" and board[3] == "X" and board[6] == "X") or (board[1] == "X" and board[4] == "X" and board[7] == "X") or (board[2] == "X" and board[5] == "X" and board[8] =="X")):
        return "X win"
    elif((board[0] == "O" and board[3] == "O" and board[6] == "O") or (board[1] == "O" and board[4] == "O" and board[7] == "O") or (board[2] == "O" and board[5] == "O" and board[8] =="O")):
        return "O win"
    else:
        return "0"
    
def diagonalCheck(board):
    if((board[0] == "X" and board[4] == "X" and board[8] == "X") or (board[2] == "X" and board[4] == "X" and board[6] == "X")):
        return "X win"
    elif((board[0] == "O" and board[4] == "O" and board[8] == "O") or (board[2] == "O" and board[4] == "O" and board[6] == "O")):
        return "O win"
    else:
        return "0"

def checkDraw(turn):
    if(turn >= 9):
        return "draw"
    
def checkWin(board, turn):
    if(horizontalCheck(board) == "X win" or verticalCheck(board) == "X win" or diagonalCheck(board) == "X win"):
        return "X win"
    elif(horizontalCheck(board) == "O win" or verticalCheck(board) == "O win" or diagonalCheck(board) == "O win"):
        return "O win"
    elif(horizontalCheck(board) == "0" and verticalCheck(board) == "0" and diagonalCheck(board) == "0"):
        if(checkDraw(turn) == "draw"):
            return "draw"
    else:
        return 0

def resetBoard(board):
    for i in range(0, len(board)):
        board[i] = ""


def getInput(mouse_pressed):
    if mouse_pressed[0]:
        pos = pygame.mouse.get_pos()
        if pos[1] < HEIGHT//3 and pos[0] < WIDTH//3:
            return 0
        elif pos[1] < HEIGHT//3 and pos[0] < 2*(WIDTH//3):
            return 1
        elif pos[1] < HEIGHT//3 and pos[0] < WIDTH:
            return 2
        elif pos[1] < 2*(HEIGHT//3) and pos[0] < WIDTH//3:
            return 3
        elif pos[1] < 2*(HEIGHT//3) and pos[0] < 2*(WIDTH//3):
            return 4
        elif pos[1] < 2*(HEIGHT//3) and pos[0] < WIDTH:
            return 5
        elif pos[1] < HEIGHT and pos[0] < WIDTH//3:
            return 6
        elif pos[1] < HEIGHT and pos[0] < 2*(WIDTH//3):
            return 7
        elif pos[1] < HEIGHT and pos[0] < WIDTH:
            return 8
        else:
            return -1
    else:
        return -1

def game(mouse_pressed, turn, board):
    square = getInput(mouse_pressed)
    if(board[square] != ""):
        return 0
    elif square != -1:
        if (turn)%2 == 1:
            board[square] = "X"
        elif (turn)%2 == 0:
            board[square] = "O"
        else:
            print("turn is neither even or odd???")
        pygame.time.delay(100)
        
        win = checkWin(board, turn)
        
        if win == "X win":
            pygame.event.post(pygame.event.Event(X_WIN))
        elif win == "O win":
            pygame.event.post(pygame.event.Event(O_WIN))
        elif win == "draw":
            pygame.event.post(pygame.event.Event(DRAW))
        return 1
    else:
        return 0
            
            
                

def main():
    clock = pygame.time.Clock()
    
    board = []
    for i in range(0, 9):
        board.append("")
    turn = 1
    win_text = ""
        
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == X_WIN:
                win_text = "X has won the game!"
            if event.type == O_WIN:
                win_text = "O has won the game!"
            if event.type == DRAW:
                win_text = "The game is a draw."
        
        mouse_pressed = pygame.mouse.get_pressed()
        draw_window(board)
        turn = turn + game(mouse_pressed,turn,board)
        
        if win_text != "":
            draw_winner(win_text)
            run = False
        
    
    pygame.quit()
    
    
if __name__ == "__main__":
    main()