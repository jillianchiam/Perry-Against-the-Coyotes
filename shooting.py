
#1 - Import library
import pygame, sys
import os
import math
import random
from pygame.locals import *


pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

keys = [False, False, False, False, False]
playerpos = [250, 200]

acc=[0,0]
list_of_hats=[]

pygame.display.set_caption('Perry Against the Coyotes')

countdown=100
countdown1=0
coyotes=[[640,100]]
healthvalue=194


current_path = os.path.dirname(r'''C:\Users\jilli\AppData\Local\Programs\Python\Python36\shooting.py''') 
resource_path = os.path.join(current_path, 'resources') 
image_path = os.path.join(resource_path, 'images')



player = pygame.image.load(os.path.join(image_path, 'perry.png'))

background = pygame.image.load(os.path.join(image_path, 'background.png'))

sunflower = pygame.image.load(os.path.join(image_path, 'sunflower.png'))

hat = pygame.image.load(os.path.join(image_path, 'perryhat.png'))

coyoteimg1 = pygame.image.load(os.path.join(image_path, 'coyote.png'))
coyoteimg = coyoteimg1

healthbar = pygame.image.load(os.path.join(image_path, 'healthbar.png'))
health = pygame.image.load(os.path.join(image_path, 'health.png'))

gameover=pygame.image.load(os.path.join(image_path, 'gameover.png'))
youwin=pygame.image.load(os.path.join(image_path, 'youwin.png'))

"""
renders the game and characters
"""
running = 1
exitcode = 0
while running:
    countdown-=1

    screen.fill(0)
    
    for x in range(width//background.get_width()+1): # range() can only work with integers, but dividing
                                                        #with the / operator always results in a float value
        for y in range(height//background.get_height()+1):
            screen.blit(background,(x*100,y*100))
    screen.blit(sunflower,(0,30))
    screen.blit(sunflower,(0,135))
    screen.blit(sunflower,(0,240))
    screen.blit(sunflower,(0,345 ))
    
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+32), position[0]-(playerpos[0]+26))
    playerrotates = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrotates.get_rect().width/2, playerpos[1]-playerrotates.get_rect().height/2)
    screen.blit(playerrotates, playerpos1)
    
    for perryhat in list_of_hats:
        index=0
        velx = math.cos(perryhat[0])*10 #10 is the speed of the arrow
        vely = math.sin(perryhat[0])*10
        perryhat[1] = perryhat[1] + velx
        perryhat[2] = perryhat[2] + vely
        if perryhat[1] < -64 or perryhat[2] > 640 or perryhat[2] < -64 or perryhat[2] > 480:
            list_of_hats.pop(index) #If no index is specified, a.pop() removes and
                     # returns the last item in the list.
        index = index + 1
        for projectile in list_of_hats:
            list_of_hats1 = pygame.transform.rotate(hat, 360-projectile[0]*57.29) # multiply radians by approximately 57.29 or 360/2π
            screen.blit(list_of_hats1, (projectile[1], projectile[2]))


    if countdown==0:
        coyotes.append([640, random.randint(50,430)])
        countdown=100-(countdown1*2)
        if countdown1>=35:
            countdown1=35
        else:
            countdown1+=5
    index=0
    for coyote in coyotes:
        if coyote[0]<-64:
            coyotes.pop(index)
        coyote[0]-=7
    
        coyoterect=pygame.Rect(coyoteimg.get_rect())
        coyoterect.top=coyote[1]
        coyoterect.left=coyote[0]
        if coyoterect.left<64:
            healthvalue -= random.randint(5,20)
            coyotes.pop(index)
        index1 = 0
        for perryhat in list_of_hats: #rect here store rectangular coordinates
            hatrect = pygame.Rect(hat.get_rect())
            hatrect.left=perryhat[1]
            hatrect.top=perryhat[2]
            if coyoterect.colliderect(hatrect):
                acc[0]+=1
                coyotes.pop(index) # pop() removes and returns last object or obj from the list
                list_of_hats.pop(index1)
                index1 += 1
    
        index+=1
    for coyote in coyotes:
        screen.blit(coyoteimg, coyote)
        for coyote in coyotes:
            screen.blit(coyoteimg, coyote)
            
    
        font = pygame.font.Font(None, 22)
        survivedtext = font.render(str((90000-pygame.time.get_ticks())/60000)+":"+str((90000-pygame.time.get_ticks())/1000%60).zfill(2), True, (0,0,0))
        textRect = survivedtext.get_rect()
        textRect.topright=[640,5]
        screen.blit(survivedtext, textRect)
        
   
    screen.blit(healthbar, (5,5))
    for perryhealth in range(healthvalue):
        screen.blit(health, (perryhealth+8, 8))

                
    pygame.display.flip()            # Update the full display Surface to the screen
    for event in pygame.event.get(): #event is for actions made by user
                                     #like pressing a key
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            pygame.display.update()

        if event.type == pygame.KEYDOWN:
            left = -10
            right = 10
            up = 10
            down = -10
            if event.key==K_w or event.key == pygame.K_UP:
                keys[0]=True
            elif event.key==K_s or event.key == pygame.K_LEFT:
                keys[1]=True
            elif event.key==K_a or event.key == pygame.K_DOWN:
                keys[2]=True
            elif event.key==K_d or event.key == pygame.K_RIGHT:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w or event.key == pygame.K_UP:
                keys[0]=False
            elif event.key==K_a or event.key == pygame.K_LEFT:
                keys[1]=False
            elif event.key==K_s or event.key == pygame.K_DOWN:
                keys[2]=False
            elif event.key==pygame.K_d or event.key == pygame.K_RIGHT:
                keys[3]=False
            


        if event.type==pygame.MOUSEBUTTONDOWN:
            position=pygame.mouse.get_pos()
            acc[1]+=1
            list_of_hats.append([math.atan2(position[1]-(playerpos1[1]+32),
                                                position[0]-(playerpos1[0]+26)),
                                     playerpos1[0]+32,
                                     playerpos1[1]+32])


        if keys[0]:
            playerpos[1]= playerpos[1] - 10
        elif keys[1]:
            playerpos[1]= playerpos[1] + 10
        elif keys[2]:
            playerpos[0] = playerpos[0] - 10
        elif keys[3]:
            playerpos[0] = playerpos[0] + 10

        if pygame.time.get_ticks()>=90000:
            running=0
            exitcode=1
        if healthvalue <= 0:
            running=0
            exitcode=0
        if acc[1]!=0:
            accuracy=acc[0]*1.0/acc[1]*100
        else:
            accuracy=0

        


def initialize_gameover_font():
    pygame.font.init()
    font = pygame.font.Font(None, 24)

def produce_text_on_screen():
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    result = gameover if exitcode == 0 else youwin
    screen.blit(result, (0,0))
    screen.blit(text, textRect)

if exitcode==0:
    initialize_gameover_font()
    text = font.render("Accuracy: "+str(accuracy)+"%", True, (255, 0, 0))
    produce_text_on_screen()
else:
    initialize_gameover_font()
    text = font.render("Accuracy: "+str(accuracy)+"%", True,  (0, 255, 0))
    produce_text_on_screen()
   

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()




            
            
            
            
