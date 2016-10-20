import pygame
from pygame.locals import *

import random
import os


pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('2048 game! :D')

# Fill background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

coords = [(50,50,100,100),(155,50,100,100),(260,50,100,100),(365,50,100,100),
          (50,155,100,100),(155,155,100,100),(260,155,100,100),(365,155,100,100),\
          (50,260,100,100),(155,260,100,100),(260,260,100,100),(365,260,100,100),\
          (50,365,100,100),(155,365,100,100),(260,365,100,100),(365,365,100,100) ]
rects = []
c = ['white','light gray','dark gray','maroon','red','green','blue','yellow','gold','purple','brown','orange','pink','violet']
colors = {2**(i):pygame.Color(c[i]) for i in range(len(c))}

board=[]
possgen = [2,4]
ask=1
score=0

def init():
    i=0
    initialBoard = board[:]
    while i<16:
        board.append(0)
        i+=1
    board[random.randint(0,15)]=possgen[random.randint(0,1)]
    i=random.randint(0,15)
    if board[i]==0:
        board[i]=possgen[random.randint(0,1)]
    elif i==15:
        board[i-1]=possgen[random.randint(0,1)]
    else:
        board[i+1]=possgen[random.randint(0,1)]
    show()

def animate_draw(coord,bg):

    x = coord[2]/2
    y = coord[3]/2
    i=0
    j=0

    while i<=x and j<=y:
        pygame.draw.rect(screen,bg,(coord[0]+x-(i/2),coord[1]+y-(j/2),i,j))
        pygame.display.flip()
        i=i+5
        j=j+5
        pygame.time.wait(3)


def show():
    os.system('clear')
    print('\n\n\n\n')
    print('||',board[0],'|',board[1],'|',board[2],'|',board[3],'||                                   SCORE: ',score)
    print('||',board[4],'|',board[5],'|',board[6],'|',board[7],'||')
    print('||',board[8],'|',board[9],'|',board[10],'|',board[11],'||')
    print('||',board[12],'|',board[13],'|',board[14],'|',board[15],'||')



    BG_COLOR = (200,200,200)
    TEXT_COLOR = (0,0,0)

    screen.blit(background, (0, 0))
    pygame.time.wait(10)
    pygame.draw.rect(screen,(0,0,0),(40,40,435,435))

    global rects,colors
    for i in range(16):
        if board[i]==0:
            BG_COLOR = pygame.Color('white')
        else:
            BG_COLOR = colors[board[i]]
        rects.append(pygame.draw.rect(screen,BG_COLOR,coords[i]))


    FONT_SIZE = 50
    font  = pygame.font.Font(None,FONT_SIZE)

    screen.blit(font.render('Score: '+str(score), 1,TEXT_COLOR),(500,50))

    for i in range(16):
        if board[i]!=0:
            xCut = len(str(board[i]))*FONT_SIZE/4
            yCut = FONT_SIZE/2
            screen.blit(font.render(str(board[i]), 1,TEXT_COLOR),(rects[i].centerx-xCut,rects[i].centery-yCut))

    pygame.display.flip()


def leftA():
    l=15
    while l>0:
        if l not in (0,4,8,12):
            if board[l-1]==0 and not board[l]==0:
                board[l-1]=board[l]
                board[l]=0
        l-=1
def leftB():
    global score
    m=1
    while m<16:
        if m not in (0,4,8,12):
            if board[m-1]==board[m] and not board[m]==0:
                board[m-1]=(board[m])*2
                board[m]=0
                score+=board[m-1]
                if m<4 and m-2>=0:
                    if board[m-2]==board[m-1]:
                        m=4
                elif m<8 and m-2>=4:
                    if board[m-2]==board[m-1]:
                        m=8
                elif m<12 and m-2>=8:
                    if board[m-2]==board[m-1]:
                        m=12
        m+=1
    leftA()
    leftA()

def rightA():
    l=0
    while l<15:
        if l not in (3,7,11,15):
            if board[l+1]==0 and not board[l]==0:
                board[l+1]=board[l]
                board[l]=0
        l+=1
def rightB():
    global score
    m=14
    while m>0:
        if m not in (3,7,11,15):
            if board[m+1]==board[m] and not board[m]==0:
                board[m+1]=(board[m])*2
                board[m]=0
                score+=board[m+1]
                if m>11 and m+2<=15:
                    if board[m+2]==board[m+1]:
                        m=8
                elif m>7 and m+2<=11:
                    if board[m+2]==board[m+1]:
                        m=4
                elif m>3 and m+2<=7:
                    if board[m+2]==board[m+1]:
                        m=0
        m-=1
    rightA()
    rightA()

def upA():
    k=15
    while k>0:
        l=k
        while l>3:
            if board[l-4]==0 and not board[l]==0:
                board[l-4]=board[l]
                board[l]=0
            l-=4
        k-=1

def upB():
    global score
    n=0
    while n<4:
        m=n
        while m<12:
            if board[m+4]==board[m] and not board[m]==0:
                board[m]=(board[m+4])*2
                board[m+4]=0
                score+=board[m]
                if m in (12,8) and board[m-8]==board[m-4]:
                    m=1
                elif m in (9,13) and board[m-8]==board[m-4]:
                    m=2
                elif m in (10,14)and board[m-8]==board[m-4]:
                    m=3
            m+=4
        n+=1
    upA()
    upA()

def downA():
    k=0
    while k<4:
        l=k
        while l<12:
            if board[l+4]==0 and not board[l]==0:
                board[l+4]=board[l]
                board[l]=0
            l+=4
        k+=1

def downB():
    global score
    n=15
    while n>11:
        m=n
        while m>3:
            if board[m-4]==board[m] and not board[m]==0:
                board[m]=(board[m-4])*2
                board[m-4]=0
                score+=board[m]
                if m in (7,3) and board[m+8]==board[m+4]:
                    m=14
                elif m in (2,6) and board[m+8]==board[m+4]:
                    m=13
                elif m in (1,5)and board[m+8]==board[m+4]:
                    m=12
            m-=4
        n-=1
    downA()
    downA()


def gen():
    while 1:
        i = random.randint(0,15)
        if board[i]==0:
            pygame.time.wait(10)
            board[i]=possgen[random.randint(0,1)]
            animate_draw(coords[i],colors[board[i]])
            break


def check():
    for val in board:
        if val==2048 and ask==1:
            ask=0
            print('                   ******************************************\n\
                   ******************************************\n\
                   ******************************************\n\
                                     YOU WON!\n\
                   ******************************************\n\
                   ******************************************\n\
                   ******************************************')
            return 0
    return 1

def gameOver():
    game_over=0
    for index, val in enumerate(board):
        if val==0:
            game_over+=1
        if index<12:
            if board[index]==board[index+1] and index not in (3,7,11,15):
                game_over+=1
            elif board[index]==board[index+4]:
                game_over+=1
        elif index in (12,13,14) and board[index]==board[index+1]:
            game_over+=1
    return game_over



def L():
    initialBoard=board[:]
    leftA()
    show()
    leftA()
    show()
    leftA()
    show()
    leftB()
    if not board==initialBoard:
        show()
        gen()
    show()

def R():
    initialBoard=board[:]
    rightA()
    show()
    rightA()
    show()
    rightA()
    show()
    rightB()
    if not board==initialBoard:
        show()
        gen()
    show()

def U():
    initialBoard=board[:]
    upA()
    show()
    upA()
    show()
    upA()
    show()
    upB()
    if not board==initialBoard:
        show()
        gen()
    show()

def D():
    initialBoard=board[:]
    downA()
    show()
    downA()
    show()
    downA()
    show()
    downB()
    if not board==initialBoard:
        show()
        gen()
    show()



def main():
    init()

    # board[0]=2
    # board[1]=4
    # board[2]=8
    # board[3]=16
    # board[4]=16
    # board[5]=8
    # board[6]=4
    # board[7]=2
    # board[8]=128
    # board[9]=4
    # board[10]=1024
    # board[11]=16
    # board[12]=16
    # board[13]=8
    # board[14]=4
    # board[15]=0

    # Display some text
    font = pygame.font.Font(None,60)
    text = font.render("2048", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    show()
    pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    print("UP")
                    screen.blit(background, (0, 0))
                    U()
                if event.key == K_LEFT:
                    print("LEFT")
                    screen.blit(background, (0, 0))
                    L()
                if event.key == K_RIGHT:
                    print("RIGHT")
                    screen.blit(background, (0, 0))
                    R()
                if event.key == K_DOWN:
                    print("DOWN")
                    screen.blit(background, (0, 0))
                    D()

        check()
        if gameOver()==0:
            background.blit(font.render("GAMEOVER!", 1, (10, 10, 10)),(100,500))



        pygame.display.flip()

if __name__=='__main__' : main()
