import random
import os

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
    

def show():
    os.system('clear')
    print '\n\n\n\n'
    print '||',board[0],'|',board[1],'|',board[2],'|',board[3],'||                                     SCORE: ',score
    print '||',board[4],'|',board[5],'|',board[6],'|',board[7],'||'
    print '||',board[8],'|',board[9],'|',board[10],'|',board[11],'||'
    print '||',board[12],'|',board[13],'|',board[14],'|',board[15],'||'

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
            board[i]=possgen[random.randint(0,1)]
            break


def check():
    for val in board:
        if val==2048 and ask==1:
                print '                   ******************************************\n\
                       ******************************************\n\
                       ******************************************\n\
                                         YOU WON!\n\
                       ******************************************\n\
                       ******************************************\n\
                       ******************************************'
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
    leftA()
    leftA()
    leftB()
    if not board==initialBoard:
        gen()
        show()

def R():
    initialBoard=board[:]
    rightA()
    rightA()
    rightA()
    rightB()
    if not board==initialBoard:
        gen()
        show()

def U():
    initialBoard=board[:]
    upA()
    upA()
    upA()
    upB()
    if not board==initialBoard:
        gen()
        show()

def D():
    initialBoard=board[:]
    downA()
    downA()
    downA()
    downB()
    if not board==initialBoard:
        gen()
        show()


init()

##board[0]=2
##board[1]=4
##board[2]=8
##board[3]=91
##board[4]=16
##board[5]=1024
##board[6]=1024
##board[7]=16
##board[8]=32
##board[9]=8
##board[10]=2
##board[11]=912
##board[12]=1
##board[13]=2
##board[14]=3
##board[15]=4
##show()

while 1:
    input = raw_input().lower()
    if input=='w':
        U()
    if input=='a':
        L()
    if input=='s':
        D()
    if input=='d':
        R()    

    if check()==0 and ask==1:
        ask=0
        won = raw_input('Would you like to continue?(Y/N)')
        if won.upper()=='N':
            break	
    if gameOver()==0:
        print '                   ******************************************\n\
                   ******************************************\n\
                   ******************************************\n\
                                     GAME OVER!\n\
                   ******************************************\n\
                   ******************************************\n\
                   ******************************************'
        break


        
