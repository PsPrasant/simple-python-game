import pygame
fps=30
score=0
import random
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((300,300))
surf=[None]*64
bucket=pygame.Surface((40,10))
for i in range(64):
    surf[i]=pygame.Surface((8,8))
done = False

x = 30
y = 30
circle_x=100
clock = pygame.time.Clock()
a=[0]*64
b=[0]*64
total=0
polygon1=[0,40,35,5]

w=0
while not done:
    if total>64*2:total=0
    else:total=total+1
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True

            if event.type ==pygame.KEYDOWN and event.key == pygame.K_UP:
                    fps=fps+5
            if event.type ==pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    fps=fps-5

         # you have to call this at the start, 
                   # if you want to use this module.
    
    key=pygame.key.get_pressed()
        
    if key[pygame.K_LEFT] and polygon1[0]-4>=0:
        polygon1=[x-4 for x in polygon1]

            
            

    if key[pygame.K_RIGHT] and polygon1[1]+4<=200:
        polygon1=[x+4 for x in polygon1]
        
        
    screen.fill((0, 0, 0))
    if(score%1000>500):
        add=score%1000 
    else: 
        add=1000-score%1000
    color=(120+add/1000*100,200,220-100*add/1000)
    count=total%128
        
    for i in range(64):
        surf[i].fill((255,255,255))
        surf[i].set_colorkey((255,255,255))
        pygame.draw.circle(surf[i], color,(4,4),2)
        
        if(b[i]>a[i]):x=b[i]#-(b[i]-a[i])*i/64
        else: x=b[i]#-(a[i]-b[i])*i/64
        
        surf[i].set_alpha(50+i*(200/64))
        if i<=60 or (i>60 and (x<polygon1[0] or x>polygon1[2])):
            screen.blit(surf[i],(x,i*4))
        if(x>=polygon1[0] and x<=polygon1[1]):
            score=score+0.1
            screen.blit(surf[i],(x,i*4-8*(i%60)+random.randint(1,2)-2))
        else:
            w=w+0.0001

    #screen.fill((0,0,0),rect=(0,i*24-2,212,24))
    #print total,count,i,q
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render(str(score//10)+' '+str(w//10), False, (200, 200, 200))
    
    screen.blit(textsurface,(200,0))
    if(count):
        integer= random.randint(-20,20)
        circle_x=circle_x+integer
        if(circle_x<0): circle_x=0
        if(circle_x>200): circle_x=200
        for i in range(1,64):
            a[i]=b[i]
            b[i]=a[i-1]
            
        a[0]=b[0]
        b[0]=circle_x
    if(w>400):
        screen.fill((0, 0, 0))
            
    pygame.draw.polygon(screen,color,((polygon1[0],240),(polygon1[1],240),(polygon1[2],250),(polygon1[3],250)))
    pygame.display.flip()
    
    clock.tick(fps+score//10000)

