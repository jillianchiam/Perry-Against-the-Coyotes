
#1 - Import library
import pygame, sys
import os
import math
import random
from pygame.locals import *

#2 - Initialize game
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

keys = [False, False, False, False, False]
playerpos = [150, 100]

acc=[0,0]
hats=[]

pygame.display.set_caption('THIS IS WAR!')

#2.1 - add the bad guys decrease the
#badtimer every frame until it is zero and then you spawn a new badger

badtimer=100
badtimer1=0
coyotes=[[640,100]]
healthvalue=194


#3 - load images

current_path = os.path.dirname(r'''C:\Users\jilli\AppData\Local\Programs\Python\Python36\shooting.py''') # Where your .py file is located
resource_path = os.path.join(current_path, 'resources') # The resource folder path
image_path = os.path.join(resource_path, 'images') # The image folder path

player = pygame.image.load(os.path.join(image_path, 'perry.png'))

grass = pygame.image.load(os.path.join(image_path, 'grass.png'))

sunflower = pygame.image.load(os.path.join(image_path, 'sunflower.png'))

hat = pygame.image.load(os.path.join(image_path, 'perryhat.png'))

coyoteimg1 = pygame.image.load(os.path.join(image_path, 'coyote.png'))
coyoteimg = coyoteimg1

badguyimg1 = pygame.image.load(os.path.join(image_path,'badguy.png'))
badguyimg=badguyimg1



#4 - Loop through game so it doesn't halt
while True:
    badtimer = badtimer - 1
    #5 - clears the screen before drawing it again
    screen.fill(0)
    #6 - draw screen elements (draw backgorund before player so player is above background
    for x in range(width//grass.get_width()+1): # range() can only work with integers, but dividing
                                                        #with the / operator always results in a float value
        for y in range(height//grass.get_height()+1):
            screen.blit(grass,(x*100,y*100))
    screen.blit(sunflower,(0,30))
    screen.blit(sunflower,(0,135))
    screen.blit(sunflower,(0,240))
    screen.blit(sunflower,(0,345 ))
    
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+32), position[0]-(playerpos[0]+26))
    playerrotates = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrotates.get_rect().width/2, playerpos[1]-playerrotates.get_rect().height/2)
    screen.blit(playerrotates, playerpos1)
    
     # 6.2 - Draw hats
    for perryhat in hats:
        index=0
        velx = math.cos(perryhat[0])*10 #10 is the speed of the arrow
        vely = math.sin(perryhat[0])*10
        perryhat[1] = perryhat[1] + velx
        perryhat[2] = perryhat[2] + vely
        if perryhat[1] < -64 or perryhat[2] > 640 or perryhat[2] < -64 or perryhat[2] > 480:
            hats.pop(index) #If no index is specified, a.pop() removes and
                     # returns the last item in the list.
        index = index + 1
        for projectile in hats:
            hats1 = pygame.transform.rotate(hat, 360-projectile[0]*57.29) # multiply radians by approximately 57.29 or 360/2π
            screen.blit(hats1, (projectile[1], projectile[2]))

    #6.3 - Draw coyotes
    if badtimer==0:
        coyotes.append([640, random.randint(50,430)])
        badtimer=100-(badtimer1*2)
        if badtimer1>=35:
            badtimer1=35
        else:
            badtimer1+=5
    index=0
    for coyote in coyotes:
        if coyote[0]<-64:
            coyotes.pop(index)
        coyote[0]-=7
    #6.3.1 - attack sunflowers
        badrect=pygame.Rect(coyoteimg.get_rect())
        badrect.top=coyote[1]
        badrect.left=coyote[0]
        if badrect.left<64:
            healthvalue -= random.randint(5,20)
            coyotes.pop(index)
        index1 = 0
        for perryhat in hats: #rect here store rectangular coordinates
            hatrect = pygame.Rect(hat.get_rect())
            hatrect.left=perryhat[1]
            hatrect.top=perryhat[2]
            if badrect.colliderect(hatrect):
                acc[0]+=1
                coyotes.pop(index) # pop() removes and returns last object or obj from the list
                hats.pop(index1)
                index1 += 1
    #6.3.3 - next coyote
        index+=1
    for coyote in coyotes:
        screen.blit(coyoteimg, coyote)


    #6.3.3 - placing next bed guy into screen
        for coyote in coyotes:
            screen.blit(coyoteimg, coyote)
                
                
    #7 - update the screen
    pygame.display.flip()            # Update the full display Surface to the screen
    for event in pygame.event.get(): #event is for actions made by user
                                     #like pressing a key
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            pygame.display.update()
            
    #8 - Keys!

        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                keys[0]=True
            elif event.key==K_a:
                keys[1]=True
            elif event.key==K_s:
                keys[2]=True
            elif event.key==K_d:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
                keys[3]=False



        if event.type==pygame.MOUSEBUTTONDOWN:
            position=pygame.mouse.get_pos()
            acc[1]+=1
            hats.append([math.atan2(position[1]-(playerpos1[1]+32),
                                                position[0]-(playerpos1[0]+26)),
                                     playerpos1[0]+32,
                                     playerpos1[1]+32])

        #9 - Move player
        if keys[0]:
            playerpos[1]= playerpos[1] - 5
        elif keys[1]:
            playerpos[1]= playerpos[1] + 5
        elif keys[2]:
            playerpos[0] = playerpos[0] - 5
        elif keys[3]:
            playerpos[0] = playerpos[0] + 5
            
            
            
            
