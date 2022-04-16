import pygame

pygame.init()

WIDTH, HEIGHT = 500,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = (0,0,0)
WHITE=(255, 255, 255)
RED =(255, 0, 0)

T = {}          #display Grid... empty-0, obstacle-2, path->1

pygame.display.set_caption("Shortest path")


n, m = 10, 10
dist = {}
G = {}          #main grid
queue = []      
par = {}        #BFS Tree
dx = [1,-1,0,0]
dy = [0,0,-1,1]

#49 pixels

def show():
    global T
    for i in range(n):
        for j in range(m):
            if(T[i][j]==0):
                pygame.draw.rect(WIN, WHITE, (50*i, 50*j, 49, 49))
            if(T[i][j]==1):
                pygame.draw.rect(WIN, RED, (50*i, 50*j, 49, 49))
            if(T[i][j]==2):
                pygame.draw.rect(WIN, BLACK, (50*i, 50*j, 49, 49))


def err():
    WIN.fill(RED)


def coord(x,y):
    a=int(x/50)
    b=int(y/50)
    global T, G
    if(T[a][b]!=2):
        T[a][b]=2
        G[a][b]=1
    else:
        T[a][b]=0
        G[a][b]=0


for i in range(n): 
    T[i]=[]
    dist[i]=[]
    G[i]=[]
    par[i]=[]

for i in range(n):
    
    for j in range(n):
        dist[i].append(-1)
        G[i].append(0)
        par[i].append((-1,-1))
        T[i].append(0)


run = True

while run:

    execute = False
    #time delay
    pygame.time.delay(10)

    for event in pygame.event.get():
        
        if(execute == False and event.type == pygame.MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
            coord(*pos)

             

        if (event.type==pygame.QUIT): run = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:

        queue.append((n-1,m-1))
        dist[n-1][m-1]=0

        while queue:
            (x,y) = queue[0]
            queue.pop(0)
            for i in range(4):
                X = dx[i]+x
                Y = dy[i]+y
                if X<0 or Y<0 or X>=n or Y>=m:
                    continue
                if dist[X][Y]>-1 or G[X][Y]==1: continue
                dist[X][Y] = dist[x][y]+1
                par[X][Y] = (x,y)
                queue.append((X,Y))
        execute = True
    


    if(execute == False):
        WIN.fill((0,0,0))
        show()
        pygame.display.update()
    else:
        (x,y) = (0,0)
        if(dist[0][0]==-1):
            err()
            pygame.display.update()
            continue
        while (x,y)!=(-1,-1):       
        #print (x,y)                 #highlight boxes
            T[x][y]=1
            (x,y)=par[x][y]
            WIN.fill((0,0,0))
            show()
            pygame.time.delay(60)
            pygame.display.update()
        
    

pygame.quit()





