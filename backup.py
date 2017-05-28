import pygame
import sys, random
from pygame.locals import *
from threading import _start_new_thread
import threading
import math
w = 800
h = 400
lifecolor = (0,0,255)
z = 0
pygame.init()
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption('White Balls')


fartbutt = pygame.image.load('fartbutt.png')
fartbutt = pygame.transform.scale(fartbutt, (500, 200))

whiteballs = pygame.image.load('ballswhite.jpg')
whiteballs = pygame.transform.scale(whiteballs, (100, 100))

bg = pygame.image.load('bggg.jpg')
bg = pygame.transform.scale(bg, (800, 400))

realscore = 0


def playmulti( file, loop=1):
    filee = file

    sound = pygame.mixer.Sound(filee)
    sound.play(loop)
    # pygame.time.wait(wait)

def playone(file):
    filee = file
    pygame.mixer.music.load(filee)
    pygame.mixer.music.play()

lifecounter = 5
liferaduis = 200
class Warrior:
    def __init__(self, radius, y,x, color, size , maxforce, force, life):
        self.y = y
        self.x = x
        self.color = color
        self.size = size
        self.maxforce = maxforce
        self.force = force
        self.radius = radius
        self.life = life



        # pygame.draw.circle(screen, self.color, (self.x, self.y), 6)


    def postup(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y),self.radius)





    def bullet(self,col):

        if self.y > 0:
            self.y -= 15

        elif self.y <= 0:
            bullets.remove(self)

        pygame.draw.circle(screen, col, (self.x, self.y-25), 5)
        return self.x,self.y


    def enemies(self,col):
        w = pygame.rect.Rect((self.x,self.y,25,25))
        if self.y < 400 :
            self.y += 6
        if self.y >= 400:
            enemiestroop.remove(self)
            enemiestroop.append(Warrior(20, 0, random.randint(10, 790), (50, 50, 50), 'L', 25, 1, 100))

        pygame.draw.rect(screen,col,w)

        return w.left,w.top
        # print(w.left)

    def lifecount(self):



        life = str(lifecounter)[:1]
        font = pygame.font.SysFont('Lucida Grande', 20)
        text = font.render(life, 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = screen.get_rect().centerx
        pygame.draw.rect(screen, (255,255,255),(350+220,textpos[1],220,15))
        screen.blit(text, (textpos[0]+180,textpos[1]))
        pygame.draw.rect(screen, (0,255,0),(350+240,textpos[1],200,10))
        pygame.draw.rect(screen,lifecolor,(350+240,textpos[1],liferaduis,10))
    def scores(self):


        score = 'Score: ' + str(realscore)
        font = pygame.font.SysFont('Lucida Grande', 36)
        text = font.render(score, 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = screen.get_rect().centerx
        screen.blit(text, textpos)

    def stop(self,file):
        pygame.mixer.Sound.stop(file)

soundlist = []

warrior_cordinatex = 300
warrior_cordinatey = 400
check = 0
clock = pygame.time.Clock()
var = 0
s = 0
enemiestroop = []
enemiestroop.append(Warrior(20, 0, random.randint(10,790), (50, 50, 50), 'L', 25, 1, 100))

bullets = []
bullets.append(Warrior(20, warrior_cordinatey -20 , warrior_cordinatex, (50, 50, 50), 'L', 25, 1, 100))

whiteballstextcolorcheck = 1
yp = 0
def start_page():
    global text
    global whiteballstextcolorcheck
    soundObj = pygame.mixer.Sound('startupmusic.wav')
    soundObj.play()
    while True:

        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()
        clock.tick(60)
        green  = (0,150,0)
        brightgreen = (0,255,0)
        red = (150,0,0)
        brightred = (255,0,0)
        screen.fill([0,0,0])
        screen.blit(whiteballs, (680,30))

        font = pygame.font.Font('BalaCynwyd.ttf', 36)
        if whiteballstextcolorcheck == 1:
            text = font.render('White Balls', 1, (255, 255, 255))
            whiteballstextcolorcheck = 2
        elif whiteballstextcolorcheck == 2:
            text = font.render('White Balls', 1, (100, 100, 100))
            whiteballstextcolorcheck = 1
        textpos = text.get_rect()
        textpos.centerx = screen.get_rect().centerx
        screen.blit(text, (textpos[0]-5,textpos[1]+60))
        if 150 + 150 > mouse_pos[0] > 150 and 200 + 80 > mouse_pos[1] > 200:
            pygame.draw.rect(screen,brightgreen,(150,200,150,80))
            core = 'Play'
            font = pygame.font.SysFont('Lucida Grande', 36)
            text = font.render(core, 1, (10, 10, 10))
            screen.blit(text, (190, 220))
            if mouse_clicked[0] == 1:

                soundObj.stop()
                gameloop()
                break
        else:
            pygame.draw.rect(screen,green,(150,200,150,80))
            core = 'Play'
            font = pygame.font.SysFont('Lucida Grande', 36)
            text = font.render(core, 1, (10, 10, 10))
            screen.blit(text, (190, 220))


        if 500 + 150 > mouse_pos[0] > 500 and 200 + 80 > mouse_pos[1] > 200:
            pygame.draw.rect(screen,brightred,(500,200,150,80))
            core = 'Quit'
            font = pygame.font.SysFont('Lucida Grande', 36)
            text = font.render(core, 1, (10, 10, 10))
            screen.blit(text, (540,220))

            if mouse_clicked[0] ==1:

                sys.exit()
                # return 00
        else:

            pygame.draw.rect(screen,red,(500,200,150,80))
            core = 'Quit'
            font = pygame.font.SysFont('Lucida Grande', 36)
            text = font.render(core, 1, (10, 10, 10))
            screen.blit(text, (540, 220))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    soundObj.stop()
                    gameloop()
                    break

        pygame.display.update()


def gameover():

    def ndthread():
        global nb
        global bn
        nb = pygame.mixer.Sound('fart.wav')

        bn = pygame.mixer.music
        bn.load('fart2.wav')
        bn.play()
        while pygame.mixer.music.get_busy():
            nb.stop()

        nb.play()
    nd = threading.Thread(group=None,target=ndthread)
    nd.start()

    while True:
        clock.tick(60)
        screen.fill([0,0,0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    global realscore
                    realscore = 0
                    nb.stop()
                    bn.stop()
                    pygame.mixer.music.stop()
                    # del ndthread
                    gameloop()
                    break

        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()

        screen.blit(fartbutt, (200,90))
        # screen.blit(whiteballs, (680,30))

        font = pygame.font.Font('BalaCynwyd.ttf', 36)
        text = font.render('You lose!', 1, (255, 255, 255))
        textpos = text.get_rect()
        textpos.centerx = screen.get_rect().centerx
        screen.blit(text, (textpos[0], textpos[1]+30))
        if 250 + 300 > mouse_pos[0] > 250 and 300 + 80 > mouse_pos[1] > 300:
            pygame.draw.rect(screen, (10,10,255), (250, 300, 300, 80))
            core = 'Try Again'
            # print('wwee')
            font = pygame.font.SysFont('Lucida Grande', 36)
            text = font.render(core, 1, (255, 255, 255))
            screen.blit(text, (340, 320))

            # pygame.display.update()
            if mouse_clicked[0] == 1:
                # soundObcj.stop()
                # lifecounter = 5
                realscore = 0

                nb.stop()
                bn.stop()
                pygame.mixer.music.stop()
                # del ndthread
                gameloop()
                break
        else:
            pygame.draw.rect(screen, (10,10,150), (250, 300, 300, 80))
            core = 'Try Again'
            font = pygame.font.SysFont('Lucida Grande', 36)
            text = font.render(core, 1, (255, 255, 255))
            screen.blit(text, (340, 320))
        if 680 + 100 > mouse_pos[0] > 680 and 30 + 60 > mouse_pos[1] > 30:
            pygame.draw.rect(screen,(255,0,0),(680,30,100,60))
            core = 'Quit'
            font = pygame.font.SysFont('Lucida Grande', 36)
            text = font.render(core, 1, (10, 10, 10))
            screen.blit(text, (700,50))

            if mouse_clicked[0] ==1:
                pygame.quit()

                sys.exit()
                # return 00
        else:

            pygame.draw.rect(screen,(175,0,0),(680,30,100,60))
            core = 'Quit'
            font = pygame.font.SysFont('Lucida Grande', 36)
            text = font.render(core, 1, (10, 10, 10))
            screen.blit(text, (700, 50))

        pygame.display.update()





def gameloop():
    lifecolorblink = 1
    global liferaduis
    global lifecounter
    global warrior_cordinatex
    global var
    global s
    global realscore
    global z
    global lifecolor
    pygame.mixer.music.stop()

    lifecounter = 5
    lifecolor = (0,0,255)
    liferaduis = 200
    while True:
        screen.fill([0, 0, 0])

        clock.tick(60)

        warrior = Warrior(20, warrior_cordinatey -20, warrior_cordinatex, (46, 134, 193), 'L', 25, 1, 100)


        screen.blit(bg,(0,0))

        if lifecounter < 4:
            if lifecolorblink ==1:
                lifecolor = (255,0,0)
                lifecolorblink = 2
            elif lifecolorblink == 2:
                lifecolor = (150,0,0)
                lifecolorblink = 1
        if warrior_cordinatex > 780:
            warrior_cordinatex = 20
        elif warrior_cordinatex < 20:
            warrior_cordinatex = 780

        warrior.postup()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif 0 ==0:
                z = 1
            elif event.type == MOUSEBUTTONUP:
                z= 0

            if event.type == KEYUP:
                var = 0


            if event.type == KEYDOWN:
                if event.key == K_RIGHT:

                        var = 15
                        print('moving right..')
                elif event.key == K_LEFT:
                        var = -15
                        print('moving left..')


        warrior_cordinatex += var
        s += 1

        if z == 1 :
            bullets.append(Warrior(20, warrior_cordinatey - 20, warrior_cordinatex, (50, 50, 50), 'L', 25, 1, 100))

            z = 5
        elif z > 1:
            z -= 1


        try:
            for kill in enemiestroop:
                # print(bul_location)
                troop_pos = kill.enemies((random.randint(10,255),0,random.randint(10,255)))

                if troop_pos[1] >= 380:
                    lifecounter -= 1/3
                    lifecounter = int((lifecounter * 100) + 0.5) / 100.0

                    liferaduis -= (1/3)*liferaduis
                # print(troop_pos)
                if troop_pos[1]> 380 and troop_pos[0] + 25 > warrior_cordinatex > troop_pos[0] or\
                                                        warrior_cordinatex + 20 > troop_pos[0] >warrior_cordinatex and troop_pos[1] > 380:

                    gameover()

                for i in bullets:
                    bul_location = i.bullet((255, 255, 255))
                    # playone('laser3.wav')



                    if troop_pos[0] + 25 > bul_location[0] > troop_pos[0] and troop_pos[1] + 25 > bul_location[1] > troop_pos[1] or \
                    bul_location[0] + 7 > troop_pos[0] > bul_location[0] and bul_location[1] + 7 > troop_pos[1] > bul_location[1]:
                        print('hit')
                        bullets.remove(i)
                        enemiestroop.remove(kill)
                        enemiestroop.append(Warrior(20, 0, random.randint(10, 770), (50, 50, 50), 'L', 25, 1, 100))
                        realscore += 1
                        playmulti('explosion.wav')




        except ValueError:
            continue
        # print(warrior_cordinatex)
        warrior.lifecount()
        warrior.scores()
        if liferaduis< 1:
            gameover()
        pygame.display.update()


start_page()
# gameover()