# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 18:00:48 2016

@author: Ela
"""

import pygame
import time
import random

pygame.init()


white = (255,255,255)
black = (0,0,0)
pink=(216,242,136)
red = (172,0,0)
light_red = (255,0,0)

turkus=(0,255,255)
light_turkus=(185,255,255)

yellow = (200,200,0)
light_yellow = (255,255,0)
light_yellow = (255,255,128)

green = (16,157,9)
light_green = (0,255,0)

display_width = 800
display_height  = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snake')

icon = pygame.image.load('C:/Users/Ela/Desktop/snake/apple.png')
pygame.display.set_icon(icon)

snakeimg = pygame.image.load('C:/Users/Ela/Desktop/snake/snakehead.png')
snakeimg2 = pygame.image.load('C:/Users/Ela/Desktop/snake/snake2.png')

jablkoimg = pygame.image.load('C:/Users/Ela/Desktop/snake/apple.png')
badjablkoimg = pygame.image.load('C:/Users/Ela/Desktop/snake/badapple.png')
snakemain = pygame.image.load('C:/Users/Ela/Desktop/snake/snakemain.png')


intro_sound= pygame.mixer.Sound('C:/Users/Ela/Desktop/snake/intro.wav')
#pauze_sound=pygame.mixer.Sound('C:/Users/Ela/Desktop/snake/clock2.wav')
fail_sound = pygame.mixer.Sound('C:/Users/Ela/Desktop/snake/Fail.wav')
mission_sound = pygame.mixer.Sound('C:/Users/Ela/Desktop/snake/mission.wav')
benny_sound = pygame.mixer.Sound('C:/Users/Ela/Desktop/snake/benny.wav')
heart_sound = pygame.mixer.Sound('C:/Users/Ela/Desktop/snake/heart.wav')
#pygame.mixer.music.load("C:/Users/Ela/Desktop/snake/clock.mp3")
#pygame.mixer.music.play(5)

clock = pygame.time.Clock()

jablkoThickness = 30
block_rozmiar = 20
FPS = 15
obstacle=50

kierunek = "right"
kierunek2="left2"

mala = pygame.font.SysFont("gabriola", 25)
srednia = pygame.font.SysFont("gabriola", 100)
duza = pygame.font.SysFont("gabriola", 200)

def napis(text,color,rozmiar):
    if rozmiar == "small":
        textSurface = mala.render(text, True, color)
    elif rozmiar == "medium":
        textSurface = srednia.render(text, True, color)
    elif rozmiar == "large":
        textSurface = duza.render(text, True, color)

    
    return textSurface, textSurface.get_rect()
 
def napis_na_przycisk(msg, color, przyciskx, przycisky, przyciskwidth, przyciskheight, rozmiar = "small"):
    textSurf, textRect = napis(msg,color,rozmiar)
    textRect.center = ((przyciskx+(przyciskwidth/2)), przycisky+(przyciskheight/2))
    gameDisplay.blit(textSurf, textRect)   
    

def zasady():


    gcont = True
    


    while gcont:
        for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

           
        gameDisplay.fill(pink)
        wypisz("Zasady",green,-100,rozmiar="large")
        wypisz("Celem gry jest zjedzenie jak najwiekszej iloci jablek",black,-30)
        wypisz("Gracz 1 : strzalki na klwiaturze",black,0)
        wypisz("Gracz 2 : W-gora, S-dol, A-lewo,D-prawo",black,30)
        #wypisz("Aby waz sie ruszal, uzywaj strzalek na klawiaturze",red,70)
        
        wypisz("pauza: P",black,110)


        przycisk("Graj", 40,500,100,50, green, light_green, action="play")
        przycisk("2 graczy", 240,500,100,50, green, light_green, action="2 graczy")
        przycisk("Menu", 440,500,100,50, yellow, light_yellow, action="main")
        przycisk("Wyjscie", 640,500,100,50, red, light_red, action ="quit")



        pygame.display.update()

        clock.tick(15)


    
def przycisk(text, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.mixer.Sound.stop(intro_sound)
                pygame.quit()
                quit()

            if action == "controls":
                pygame.mixer.Sound.stop(heart_sound)
                pygame.mixer.Sound.stop(intro_sound)
                zasady()

            if action == "play":
                pygame.mixer.Sound.stop(heart_sound)
                pygame.mixer.Sound.stop(intro_sound)
                gra()
                
            if action == "2 graczy":
                pygame.mixer.Sound.stop(heart_sound)
                pygame.mixer.Sound.stop(intro_sound)
                gra2()
                
            if action=="main":
                pygame.mixer.Sound.stop(heart_sound)
                game_intro()
                
            if action=="pauza":
                pygame.mixer.Sound.stop(mission_sound)
                pauza()
                
            if action=="continue":
                pygame.mixer.Sound.stop(heart_sound)
                pauza = False
                
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x,y,width,height))

    napis_na_przycisk(text,black,x,y,width,height)
    
def wypisz(msg,color, y_displace=0, rozmiar = "small"):
    textSurf, textRect = napis(msg,color, rozmiar)
    textRect.center = (display_width / 2), (display_height / 2)+y_displace
    gameDisplay.blit(textSurf, textRect)
        
        
        #clock.tick(5)
def wynik(wynik,):
    text = mala.render("Wynik : "+str(wynik), True, black)
    gameDisplay.blit(text, [0,0])                  

def wynik2(wynik,wynik2):
    text = mala.render("Gracz 1: "+str(wynik), True, green)
    gameDisplay.blit(text, [690,0])
    text2 = mala.render("Gracz 2: "+str(wynik2), True, turkus)
    gameDisplay.blit(text2, [10,0])

def pauza():

    pauzad = True
    wypisz("pauza",
                      black,
                      -100,
                      rozmiar="large")

    wypisz(" K: kontynuowac       ",
                      black,
                      25)
    wypisz(" M:  powrot do menu       ",
                      black,
                      55)
    wypisz("Q: wyjscie",
                      black,
                      80)


    
    pygame.display.update()
    pygame.mixer.Sound.play(heart_sound)
    while pauzad:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k:
                    pygame.mixer.Sound.stop(heart_sound)
                    pygame.mixer.Sound.play(mission_sound)
                    pauzad = False
                    
                if event.key == pygame.K_m:
                    pygame.mixer.Sound.stop(heart_sound)
                    pygame.mixer.Sound.play(intro_sound)
                    game_intro()

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()  
                    
        clock.tick(5)

def jablko():
    randjablkoX = round(random.randrange(0, display_width-jablkoThickness))#/10.0)*10.0
    randjablkoY = round(random.randrange(0, display_height-jablkoThickness))#/10.0)*10.0

    return randjablkoX,randjablkoY
    
def randObstacleGen():
    randObstacleX = round(random.randrange(0, display_width-obstacle))#/10.0)*10.0
    randObstacleY = round(random.randrange(0, display_height-obstacle))#/10.0)*10.0

    return randObstacleY,randObstacleY
'''
def randObstacleGen2():

    pygame.draw.rect(gameDisplay, black, [random.randrange(0, 600),random.randrange(0, 600),random.randrange(0, 50)random.randrange(0, 50)])


   

    
    
    
pygame.display.update()
    return randObstacleY,randObstacleY'''

def game_intro():

    intro = True
    pygame.mixer.Sound.play(intro_sound)
    

    while intro:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_k:
                    pygame.mixer.Sound.stop(intro_sound)
                    intro = False

                    
                if event.key == pygame.K_q:
                    pygame.mixer.Sound.stop(intro_sound)
                    pygame.quit()
                    quit()
       
        gameDisplay.fill(pink)
        gameDisplay.blit(snakemain, (320, 270))
        wypisz("Snake",
                          green,
                          -100,
                          "large")
        

        
        przycisk("Graj", 40,500,100,50, green, light_green, action="play")
        przycisk("2 graczy", 240,500,100,50, turkus, light_turkus, action="2 graczy")
        przycisk("Zasady", 440,500,100,50, yellow, light_yellow, action="controls")
        przycisk("Wyjscie", 640,500,100,50, red, light_red, action ="quit")

        
        pygame.display.update()
        clock.tick(15)
        
       
        


def snake(block_rozmiar, snakelist):

    if kierunek == "right":
        head = pygame.transform.rotate(snakeimg, 270)

    if kierunek == "left":
        head = pygame.transform.rotate(snakeimg, 90)

    if kierunek == "up":
        head = snakeimg

    if kierunek == "down":
        head = pygame.transform.rotate(snakeimg, 180)
        
    
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_rozmiar,block_rozmiar])

def snake2(block_rozmiar, snakelist2):

    if kierunek2 == "right2":
        head2 = pygame.transform.rotate(snakeimg2, 270)

    if kierunek2 == "left2":
        head2 = pygame.transform.rotate(snakeimg2, 90)

    if kierunek2 == "up2":
        head2 = snakeimg2

    if kierunek2 == "down2":
        head2 = pygame.transform.rotate(snakeimg2, 180)
        
    
    gameDisplay.blit(head2, (snakelist2[-1][0], snakelist2[-1][1]))
    
    for XnY2 in snakelist2[:-1]:
        pygame.draw.rect(gameDisplay, turkus, [XnY2[0],XnY2[1],block_rozmiar,block_rozmiar])
        
                         
                         
def gra2():
    global kierunek
    global kierunek2

    kierunek = 'right'
    kierunek2 = 'left2'
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1
    
    lead_x2= display_width/2
    lead_y2= display_height/2

    lead_x_change2 = -10
    lead_y_change2 = 0
    
    snakeList2 = []
    snakeLength2 = 1

    randjablkoX,randjablkoY = jablko()
    randObstacleX,randObstacleY = randObstacleGen()
    
    pygame.mixer.Sound.play(benny_sound)
    
    while not gameExit:

        if gameOver == True:
            pygame.mixer.Sound.stop(benny_sound)
            pygame.mixer.Sound.play(fail_sound)
            wypisz("PRZEGRALES",
                              red,
                              y_displace=-50,
                              rozmiar="medium")
            
            wypisz("K: kontynouwać        M: powrot do menu       Q:  wyjscie",
                              black,
                              50,
                              rozmiar="small")
            pygame.display.update()
            

        while gameOver == True:
            pygame.mixer.Sound.stop(benny_sound)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_k:
                        pygame.mixer.Sound.stop(fail_sound)
                        gra2()
                    if event.key == pygame.K_m:
                        pygame.mixer.Sound.stop(fail_sound)
                        game_intro()
                    

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    kierunek = "left"
                    lead_x_change = -block_rozmiar
                    lead_y_change = 0
                if event.key == pygame.K_RIGHT:
                    kierunek = "right"
                    lead_x_change = block_rozmiar
                    lead_y_change = 0
                if event.key == pygame.K_UP:
                    kierunek = "up"
                    lead_y_change = -block_rozmiar
                    lead_x_change = 0
                if event.key == pygame.K_DOWN:
                    kierunek = "down"
                    lead_y_change = block_rozmiar
                    lead_x_change = 0

                if event.key == pygame.K_p:
                    pauza()
        

                if event.key == pygame.K_a:
                    kierunek2 = "left2"
                    lead_x_change2 = -block_rozmiar
                    lead_y_change2 = 0
                if event.key == pygame.K_d:
                    kierunek2 = "right2"
                    lead_x_change2 = block_rozmiar
                    lead_y_change2 = 0
                if event.key == pygame.K_w:
                    kierunek2 = "up2"
                    lead_y_change2 = -block_rozmiar
                    lead_x_change2 = 0
                if event.key == pygame.K_s:
                    kierunek2 = "down2"
                    lead_y_change2 = block_rozmiar
                    lead_x_change2 = 0


        if lead_x >= display_width:
            lead_x=0
        if lead_x < 0 :
            randObstacleX,randObstacleY = randObstacleGen()
            lead_x=display_width
        if lead_y >= display_height:
            lead_y=0
            randObstacleX,randObstacleY = randObstacleGen()
        if lead_y < 0:
            lead_y=display_height
            
        if lead_x2 >= display_width:
            lead_x2=0
        if lead_x2 < 0 :
            lead_x2=display_width
        if lead_y2 >= display_height:
            lead_y2=0
            randObstacleX,randObstacleY = randObstacleGen()
        if lead_y2 < 0:
            lead_y2=display_height
      

        lead_x += lead_x_change
        lead_y += lead_y_change
        
        lead_x2 += lead_x_change2
        lead_y2 += lead_y_change2
        
        gameDisplay.fill(pink)

        
        #pygame.draw.rect(gameDisplay, red, [randjablkoX, randjablkoY, jablkoThickness, jablkoThickness])

        gameDisplay.blit(jablkoimg, (randjablkoX, randjablkoY))
        gameDisplay.blit(badjablkoimg, (randObstacleX, randObstacleY))
        

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        
        snakeHead2 = []
        snakeHead2.append(lead_x2)
        snakeHead2.append(lead_y2)
        snakeList2.append(snakeHead2)

        if len(snakeList) > snakeLength:
            del snakeList[0]
            
        if len(snakeList2) > snakeLength2:
            del snakeList2[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
                
        for eachSegment2 in snakeList2[:-1]:
            if eachSegment2 == snakeHead2:
                gameOver = True

        
        snake(block_rozmiar, snakeList)
        snake2(block_rozmiar, snakeList2)

        wynik2(snakeLength-1,snakeLength2-1)
        przycisk("Pauza", 350,0,100,50, red, light_red, action="pauza")


        
        pygame.display.update()

        if (lead_x > randjablkoX and lead_x < randjablkoX + jablkoThickness) or (lead_x + block_rozmiar > randjablkoX and lead_x + block_rozmiar < randjablkoX + jablkoThickness) or (lead_x2 > randjablkoX and lead_x2 < randjablkoX + jablkoThickness) or (lead_x2 + block_rozmiar > randjablkoX and lead_x2 + block_rozmiar < randjablkoX + jablkoThickness):

            if lead_y > randjablkoY and lead_y < randjablkoY + jablkoThickness:

                randjablkoX,randjablkoY = jablko()
                snakeLength += 1
                

            if lead_y + block_rozmiar > randjablkoY and lead_y + block_rozmiar < randjablkoY + jablkoThickness:

                randjablkoX,randjablkoY = jablko()
                randObstacleX,randObstacleY = randObstacleGen()
                
                snakeLength += 1
                
            if lead_y2 > randjablkoY and lead_y2 < randjablkoY + jablkoThickness:

                randjablkoX,randjablkoY = jablko()
                snakeLength2 += 1
                

            if lead_y2 + block_rozmiar > randjablkoY and lead_y2 + block_rozmiar < randjablkoY + jablkoThickness:

                randjablkoX,randjablkoY = jablko()
                randObstacleX,randObstacleY = randObstacleGen()
                snakeLength2 += 1
                
                
                
        if (lead_x > randObstacleX and lead_x < randObstacleX + obstacle) or (lead_x + block_rozmiar > randObstacleX and lead_x + block_rozmiar < randObstacleX + obstacle) or (lead_x2 > randObstacleX and lead_x2 < randObstacleX + obstacle) or (lead_x2 + block_rozmiar > randObstacleX and lead_x2 + block_rozmiar < randObstacleX + obstacle):

            if lead_y > randObstacleY and lead_y < randObstacleY + obstacle:

                randObstacleX,randObstacleY = randObstacleGen()
                
                pygame.mixer.Sound.stop(benny_sound) 
                gameOver = True

            if lead_y + block_rozmiar > randObstacleY and lead_y + block_rozmiar < randObstacleY + obstacle:

                randObstacleX,randObstacleY = randObstacleGen()
                pygame.mixer.Sound.stop(benny_sound) 
                gameOver = True
                

            if lead_y2 > randObstacleY and lead_y2 < randObstacleY + obstacle:

                randObstacleX,randObstacleY = randObstacleGen()
                pygame.mixer.Sound.stop(benny_sound) 
                gameOver = True

            if lead_y2 + block_rozmiar > randObstacleY and lead_y2 + block_rozmiar < randObstacleY + obstacle:

                randObstacleX,randObstacleY = randObstacleGen()
                pygame.mixer.Sound.stop(benny_sound) 
                gameOver = True

        
            
        
        

        clock.tick(FPS+snakeLength)
        
    pygame.quit()
    quit()

                         
def gra():
    global kierunek

    kierunek = 'right'
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randjablkoX,randjablkoY = jablko()
    randObstacleX,randObstacleY = randObstacleGen()
    
    pygame.mixer.Sound.play(mission_sound)
    
    while not gameExit:
        

        if gameOver == True:
            pygame.mixer.Sound.stop(mission_sound) 
            wypisz("PRZEGRALES",
                              red,
                              y_displace=-50,
                              rozmiar="medium")
            
            wypisz("K: kontynouwać      M:  powrocic do menu        Q: aby wyjsc",
                              black,
                              50,
                              rozmiar="small")
            pygame.display.update()
            

        while gameOver == True:
            pygame.mixer.Sound.stop(mission_sound) 
            pygame.mixer.Sound.play(fail_sound)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                        pygame.mixer.Sound.stop(fail_sound)
                    if event.key == pygame.K_k:
                        pygame.mixer.Sound.stop(fail_sound)
                        gra()
                        
                    if event.key == pygame.K_m:
                        pygame.mixer.Sound.stop(fail_sound)
                        game_intro()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    kierunek = "left"
                    lead_x_change = -block_rozmiar
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    kierunek = "right"
                    lead_x_change = block_rozmiar
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    kierunek = "up"
                    lead_y_change = -block_rozmiar
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    kierunek = "down"
                    lead_y_change = block_rozmiar
                    lead_x_change = 0

                elif event.key == pygame.K_p:
                    pygame.mixer.Sound.stop(mission_sound) 
                    pauza()

        if lead_x >= display_width:
            lead_x=0
            randObstacleX,randObstacleY = randObstacleGen()
        if lead_x < 0 :
            lead_x=display_width
        if lead_y >= display_height:
            lead_y=0
            randObstacleX,randObstacleY = randObstacleGen()
        if lead_y < 0:
            lead_y=display_height
            
      
      

        lead_x += lead_x_change
        lead_y += lead_y_change
        
        kolor=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        gameDisplay.fill(pink)

        
        #pygame.draw.rect(gameDisplay, red, [randjablkoX, randjablkoY, jablkoThickness, jablkoThickness])

        gameDisplay.blit(jablkoimg, (randjablkoX, randjablkoY))
        gameDisplay.blit(badjablkoimg, (randObstacleX, randObstacleY))


        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                pygame.mixer.Sound.stop(intro_sound) 
                gameOver = True

        
        snake(block_rozmiar, snakeList)

        wynik(snakeLength-1)
        

        '''hisc=open('C:/Users/Ela/Desktop/snake/highwynik.txt',"w+")
        highwynik1=hisc.read()
        highwynik2=int(highwynik1)
        highwynik_in_no=highwynik2
        if wynik>highwynik_in_no:
                hisc.write(str(wynik))
                highwynik_in_no=wynik
 
        hisc.close()
        
        wypisz(highwynik_in_no,black,100)
        wypisz("Najlepszy wynik",black,110)'''

        
        przycisk("pauza", 350,0,100,50, red, light_red, action="pauza")
        
        pygame.display.update()

        if lead_x > randjablkoX and lead_x < randjablkoX + jablkoThickness or lead_x + block_rozmiar > randjablkoX and lead_x + block_rozmiar < randjablkoX + jablkoThickness:

            if lead_y > randjablkoY and lead_y < randjablkoY + jablkoThickness:

                randjablkoX,randjablkoY = jablko()
                snakeLength += 1
                gameDisplay.fill(kolor)
                pygame.display.update()
                

            elif lead_y + block_rozmiar > randjablkoY and lead_y + block_rozmiar < randjablkoY + jablkoThickness:

                randjablkoX,randjablkoY = jablko()
                randObstacleX,randObstacleY = randObstacleGen()
                snakeLength += 1
                gameDisplay.fill(kolor)
                pygame.display.update()
                
        if lead_x > randObstacleX and lead_x < randObstacleX + obstacle or lead_x + block_rozmiar > randObstacleX and lead_x + block_rozmiar < randObstacleX + obstacle:

            if lead_y > randObstacleY and lead_y < randObstacleY + obstacle:

                randObstacleX,randObstacleY = randObstacleGen()
                pygame.mixer.Sound.stop(intro_sound) 
                gameOver = True

            elif lead_y + block_rozmiar > randObstacleY and lead_y + block_rozmiar < randObstacleY + obstacle:

                randObstacleX,randObstacleY = randObstacleGen()
                pygame.mixer.Sound.stop(intro_sound) 
                gameOver = True

            
            

        
            
        
        

        clock.tick(FPS+snakeLength)
           
    pygame.quit()
    quit()

game_intro()
