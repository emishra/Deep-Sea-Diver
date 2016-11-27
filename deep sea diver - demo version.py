
#Eshani Mishra
#Term Project
#Section J

import pygame
import random
import math
import os

### uses pygamegame.py from the Pygame Optional Lecture, 11/11/15 as the run function
from pygamegame import PygameGame


#from course notes on strings under Basic File IO
def readFile(path):
    with open(path, "rt") as f:
        return f.read()


class InteractiveObject(pygame.sprite.Sprite):

    COlOR_BROWN = (92, 51, 23) #RGB triplet

    def __init__(self, x, y, image):
        super(InteractiveObject, self).__init__()
        self.x=x
        self.y=y
        self.image=image
        self.width, self.height = self.image.get_size()
        self.updateRect()

    def updateRect(self):
        self.rect = pygame.Rect(self.x - self.width / 2, 
            self.y - self.height / 2, 
            self.width, self.height)


class Coin(InteractiveObject):

    @staticmethod
    def loadImage():
        coin1 = pygame.image.load(os.path.join("coins", "1.png")).convert_alpha()
        w, h = coin1.get_size()
        scale = 2
        coin1 = pygame.transform.scale(coin1, (w/scale, h/scale))

        coin2 = pygame.image.load(os.path.join("coins", "2.png")).convert_alpha()
        coin2 = pygame.transform.scale(coin2, (w/scale, h/scale))

        coin3 = pygame.image.load(os.path.join("coins", "3.png")).convert_alpha()
        coin3 = pygame.transform.scale(coin3, (w/scale, h/scale))

        coin4 = pygame.image.load(os.path.join("coins", "4.png")).convert_alpha()
        coin4 = pygame.transform.scale(coin4, (w/scale, h/scale))

        coin5 = pygame.image.load(os.path.join("coins", "5.png")).convert_alpha()
        coin5 = pygame.transform.scale(coin5, (w/scale, h/scale))

        coin6 = pygame.image.load(os.path.join("coins", "6.png")).convert_alpha()
        coin6 = pygame.transform.scale(coin6, (w/scale, h/scale))

        Coin.images = [coin1, coin2, coin3, coin4, coin5, coin6]

        Coin.numImages = 6

    def __init__(self, x, y):
        super(InteractiveObject, self).__init__()
        self.x = x
        self.y = y
        self.curImage = 0
        self.updateCount = 0
        self.image = Coin.images[self.curImage]
        self.width, self.height = self.image.get_size()
        self.radius = self.width - 1
        self.updateRect()

    #curImage is used to loop through images to show objects as an animation
    def update(self):
        self.updateRect()
        self.updateCount+=1
        if self.updateCount % 2 == 0:
            self.curImage = (self.curImage+1)%Coin.numImages
            self.image = Coin.images[self.curImage]

class Cave(InteractiveObject):

    #location can be 1, 4, or 7
    def __init__(self, screenWidth, screenHeight, location):
        super(InteractiveObject, self).__init__()
        numCaves = 7 #screenWidth is divided into 7 positions
        self.width = screenWidth/numCaves
        self.height = screenHeight*(0.75)
        self.x = self.width*(location-1) + self.width/2
        self.y = screenHeight + self.height/2
        self.image = pygame.Surface((self.width, self.height))
        self.image.convert()
        self.image.set_alpha(255)
        self.image.fill(InteractiveObject.COlOR_BROWN)
        self.updateRect()

    def update(self):
        self.updateRect()

class DarkCave(Cave):

    #location can be 2, 3, 5 or 6
    def __init__(self, screenWidth, screenHeight, location):
        super(DarkCave, self).__init__(screenWidth, screenHeight, location)
        self.image.fill((0, 0, 0))
        self.isFading = False

    def update(self):
        self.updateRect()
        if self.isFading:
            self.image.set_alpha(int(self.image.get_alpha()/1.01))


#Diver class uses code from pygame optional lecture asteriods game
class Diver(InteractiveObject):

    @staticmethod
    def loadImage():
        diver1 = pygame.image.load(os.path.join("diverpngs", "diver1.png")).convert_alpha()
        diver1 = pygame.transform.rotate(diver1, 60)
        

        diver2 = pygame.image.load(os.path.join("diverpngs", "diver2.png")).convert_alpha()
        diver2 = pygame.transform.rotate(diver2, 60)

        diver3 = pygame.image.load(os.path.join("diverpngs", "diver2.png")).convert_alpha()
        diver3 = pygame.transform.rotate(diver3, 60)

        diver4 = pygame.image.load(os.path.join("diverpngs", "diver4.png")).convert_alpha()
        diver4 = pygame.transform.rotate(diver4, 60)

        diver5 = pygame.image.load(os.path.join("diverpngs", "diver5.png")).convert_alpha()
        diver5 = pygame.transform.rotate(diver5, 60)

        diver6 = pygame.image.load(os.path.join("diverpngs", "diver6.png")).convert_alpha()
        diver6 = pygame.transform.rotate(diver6, 60)

        Diver.images = [diver1, diver2, diver3, diver4, diver5, diver6]

        fdiver1 = pygame.image.load(os.path.join("diverpngs-loselife", "diver1.png")).convert_alpha()
        fdiver1 = pygame.transform.rotate(fdiver1, 60)

        fdiver2 = pygame.image.load(os.path.join("diverpngs-loselife", "diver2.png")).convert_alpha()
        fdiver2 = pygame.transform.rotate(fdiver2, 60)

        fdiver3 = pygame.image.load(os.path.join("diverpngs-loselife", "diver3.png")).convert_alpha()
        fdiver3 = pygame.transform.rotate(fdiver3, 60)

        fdiver4 = pygame.image.load(os.path.join("diverpngs-loselife", "diver4.png")).convert_alpha()
        fdiver4 = pygame.transform.rotate(fdiver4, 60)

        fdiver5 = pygame.image.load(os.path.join("diverpngs-loselife", "diver5.png")).convert_alpha()
        fdiver5 = pygame.transform.rotate(fdiver5, 60)

        fdiver6 = pygame.image.load(os.path.join("diverpngs-loselife", "diver6.png")).convert_alpha()
        fdiver6 = pygame.transform.rotate(fdiver6, 60)

        blink = pygame.Surface((2, 2))
        blink.set_alpha(0)

        Diver.fadedImages =[fdiver1, blink, fdiver3, blink, fdiver5, blink]

        Diver.numImages = len(Diver.images)
        Diver.fadeTime = 75

    def __init__(self, x, y, image):
        super(Diver, self).__init__(x, y, image)
        self.speed=5
        self.curImage = 0
        self.isFaded = False
        self.updateCount = 0

    def update(self, isKeyPressed, screenWidth, screenHeight):
        self.dx = 0
        self.dy = 0
        self.updateCount+=1
        #checks if keys are held down in timer fired for smooth motion
        if isKeyPressed(pygame.K_LEFT):
            self.x-=self.speed
            self.dx = -self.speed

        if isKeyPressed(pygame.K_RIGHT):
            self.x+=self.speed
            self.dx = self.speed

        if isKeyPressed(pygame.K_UP):
            self.y-=self.speed
            self.dy = -self.speed

        if isKeyPressed(pygame.K_DOWN):
            self.y+=self.speed
            self.dy = self.speed

        #wrap around
        if self.rect.left < 0:
            self.x = self.width/2
        elif self.rect.right > screenWidth:
            self.x = screenWidth - self.width/2
        if self.rect.top < 0:
            self.y = self.height/2
        elif self.rect.bottom > screenHeight:
            self.y = screenHeight - self.height/2
        self.updateRect()
        if self.updateCount%2 == 0:
            self.curImage = (self.curImage+1)%Diver.numImages
            if self.isFaded:
                imagesList = Diver.fadedImages
            else:
                imagesList = Diver.images
            self.image = imagesList[self.curImage]


class Mine(InteractiveObject):
    
    @staticmethod
    def loadImage():
        Mine.image = pygame.image.load(os.path.join("naval mine.png")).convert_alpha()
        w, h = Mine.image.get_size()
        scale=12
        Mine.image = pygame.transform.scale(Mine.image, (w/scale, h/scale))

    def __init__(self, x, y, image):
        super(Mine, self).__init__(x, y, image)
        self.radius = self.width-2

    def update(self):
        self.updateRect()

#abstract class, instance of fish is never created
class Fish(InteractiveObject):

    def __init__(self):
        super(InteractiveObject, self).__init__()
        self.direction=random.choice([1, -1]) #(right, left)
        self.speed=2
        self.curImage = 0
        
    def update(self):
        self.x+=self.direction*self.speed
        self.updateRect()

class NonDangerousFish(Fish):

    @staticmethod
    def loadImage():
        rfish1 = pygame.image.load(os.path.join("Swim_to_right", "1.png")).convert_alpha()
        w, h = rfish1.get_size()
        scale = 5
        rfish1 = pygame.transform.scale(rfish1, (w/scale, h/scale))
        rfish2 = pygame.image.load(os.path.join("Swim_to_right", "2.png")).convert_alpha()
        rfish2 = pygame.transform.scale(rfish2, (w/scale, h/scale))
        rfish3 = pygame.image.load(os.path.join("Swim_to_right", "3.png")).convert_alpha()
        rfish3 = pygame.transform.scale(rfish3, (w/scale, h/scale))
        rfish4 = pygame.image.load(os.path.join("Swim_to_right", "4.png")).convert_alpha()
        rfish4 = pygame.transform.scale(rfish4, (w/scale, h/scale))
        rfish5 = pygame.image.load(os.path.join("Swim_to_right", "5.png")).convert_alpha()
        rfish5 = pygame.transform.scale(rfish5, (w/scale, h/scale))
        rfish6 = pygame.image.load(os.path.join("Swim_to_right", "6.png")).convert_alpha()
        rfish6 = pygame.transform.scale(rfish6, (w/scale, h/scale))
        NonDangerousFish.swimRightImages = [rfish1, rfish2, rfish3, rfish4, rfish5, rfish6]
        lfish1 = pygame.image.load(os.path.join("swim_to_left", "1.png")).convert_alpha()
        lfish1 = pygame.transform.scale(lfish1, (w/scale, h/scale))
        lfish2 = pygame.image.load(os.path.join("swim_to_left", "2.png")).convert_alpha()
        lfish2 = pygame.transform.scale(lfish2, (w/scale, h/scale))
        lfish3 = pygame.image.load(os.path.join("swim_to_left", "3.png")).convert_alpha()
        lfish3 = pygame.transform.scale(lfish3, (w/scale, h/scale))
        lfish4 = pygame.image.load(os.path.join("swim_to_left", "4.png")).convert_alpha()
        lfish4 = pygame.transform.scale(lfish4, (w/scale, h/scale))
        lfish5 = pygame.image.load(os.path.join("swim_to_left", "5.png")).convert_alpha()
        lfish5 = pygame.transform.scale(lfish5, (w/scale, h/scale))
        lfish6 = pygame.image.load(os.path.join("swim_to_left", "6.png")).convert_alpha()
        lfish6 = pygame.transform.scale(lfish6, (w/scale, h/scale))
        NonDangerousFish.swimLeftImages = [lfish1, lfish2, lfish3, lfish4, lfish5, lfish6]
        NonDangerousFish.numImages = len(NonDangerousFish.swimRightImages)

    def __init__(self, screenWidth, screenHeight):
        super(NonDangerousFish, self).__init__()
        if self.direction == 1: #right
            self.images = NonDangerousFish.swimRightImages
        else: #left
            self.images = NonDangerousFish.swimLeftImages
        self.image = self.images[self.curImage]
        self.width, self.height = self.image.get_size()
        self.y = random.randint(0, screenHeight-self.height/2)
        if self.direction == 1: #right
            self.x = 0+self.width/2
        else: #left
            self.x = screenWidth - self.width/2
        self.updateRect()
        self.diversion = 5
        

    def update(self):
        super(NonDangerousFish, self).update()
        self.curImage = (self.curImage+1)%NonDangerousFish.numImages
        self.image = self.images[self.curImage]


    #called when diver collides with this type of fish
    #diver bounces off fish
    def divertDiver(self, diver):
        if type(diver)==Diver:
            diver.x-=self.diversion
            diver.y-=self.diversion
            diver.updateRect()

class DangerousFish(Fish):

    @staticmethod
    def loadImage():
        rshark1 = pygame.image.load(os.path.join("shark swim right", "1.png")).convert_alpha()
        w, h = rshark1.get_size()
        scale = 6
        rshark1 = pygame.transform.scale(rshark1, (w/scale, h/scale))
        rshark2 = pygame.image.load(os.path.join("shark swim right", "2.png")).convert_alpha()
        rshark2 = pygame.transform.scale(rshark2, (w/scale, h/scale))
        rshark3 = pygame.image.load(os.path.join("shark swim right", "3.png")).convert_alpha()
        rshark3 = pygame.transform.scale(rshark3, (w/scale, h/scale))
        rshark4 = pygame.image.load(os.path.join("shark swim right", "4.png")).convert_alpha()
        rshark4 = pygame.transform.scale(rshark4, (w/scale, h/scale))
        rshark5 = pygame.image.load(os.path.join("shark swim right", "5.png")).convert_alpha()
        rshark5 = pygame.transform.scale(rshark5, (w/scale, h/scale))
        rshark6 = pygame.image.load(os.path.join("shark swim right", "6.png")).convert_alpha()
        rshark6 = pygame.transform.scale(rshark6, (w/scale, h/scale))
        DangerousFish.swimRightImages = [rshark1, rshark2, rshark3, rshark4, rshark5, rshark6]

        lshark1 = pygame.image.load(os.path.join("shark swim left", "1.png")).convert_alpha()
        lshark1 = pygame.transform.scale(lshark1, (w/scale, h/scale))
        lshark2 = pygame.image.load(os.path.join("shark swim left", "2.png")).convert_alpha()
        lshark2 = pygame.transform.scale(lshark2, (w/scale, h/scale))
        lshark3 = pygame.image.load(os.path.join("shark swim left", "3.png")).convert_alpha()
        lshark3 = pygame.transform.scale(lshark3, (w/scale, h/scale))
        lshark4 = pygame.image.load(os.path.join("shark swim left", "4.png")).convert_alpha()
        lshark4 = pygame.transform.scale(lshark4, (w/scale, h/scale))
        lshark5 = pygame.image.load(os.path.join("shark swim left", "5.png")).convert_alpha()
        lshark5 = pygame.transform.scale(lshark5, (w/scale, h/scale))
        lshark6 = pygame.image.load(os.path.join("shark swim left", "6.png")).convert_alpha()
        lshark6 = pygame.transform.scale(lshark6, (w/scale, h/scale))
        DangerousFish.swimLeftImages = [lshark1, lshark2, lshark3, lshark4, lshark5, lshark6]
        DangerousFish.numImages = len(DangerousFish.swimRightImages)

    def __init__(self, screenWidth, screenHeight):
        super(DangerousFish, self).__init__()
        if self.direction == 1: #right
            self.images = DangerousFish.swimRightImages
        else: #left
            self.images = DangerousFish.swimLeftImages
        self.image = self.images[self.curImage]
        self.width, self.height = self.image.get_size()
        self.y = random.randint(0, screenHeight-self.height/2)
        if self.direction == 1: #right
            self.x = 0+self.width/2
        else: #left
            self.x = screenWidth - self.width/2
        self.updateRect()
        self.updateCount = 0

    def update(self):
        self.updateCount+=1
        super(DangerousFish, self).update()
        #change the image every time update is called to animate character
        if self.updateCount%2 == 0:
            self.curImage = (self.curImage+1)%DangerousFish.numImages
            self.image = self.images[self.curImage]


class AnglerFish(Fish):

    @staticmethod
    def loadImage():
        AnglerFish.left = pygame.image.load(os.path.join("angler.png")).convert_alpha()
        w, h = AnglerFish.left.get_size()
        scale = 3
        AnglerFish.left = pygame.transform.scale(AnglerFish.left, (w/scale, h/scale))

    def __init__(self, screenWidth, screenHeight):
        super(AnglerFish, self).__init__()
        self.canFollow = True
        self.distaceToFollow = 150
        self.image = AnglerFish.left
        self.width, self.height = self.image.get_size()
        self.x = random.randint(0, screenWidth)
        self.y = screenHeight + 10
        self.updateRect()


    @staticmethod
    def getDistance(x0, y0, x1, y1):
        return math.sqrt((x1-x0)**2 + (y1-y0)**2)


    def followDiver(self, diver):
        if self.canFollow:
            if (AnglerFish.getDistance(self.x, self.y, diver.x, diver.y) 
                <= self.distaceToFollow):
                if self.x<=diver.x:
                    dx = 1
                elif self.x>diver.x:
                    dx = -1
                if self.y<=diver.y:
                    dy = 1
                elif self.y>diver.y:
                    dy = -1
                self.x += dx*self.speed
                self.y += dy*self.speed

    def update(self, diver):
        self.followDiver(diver)
        self.updateRect()


class Lives(object):

    @staticmethod
    def loadImage():
        Lives.image = pygame.image.load(os.path.join('heartlife.png')).convert_alpha()
        w, h = Mine.image.get_size()
        scale=3
        Lives.image = pygame.transform.scale(Lives.image, (w/scale, h/scale))

    def __init__(self, x, y):
        self.x, self.y = x, y

    def draw(self, screen):
        screen.blit(Lives.image, (self.x, self.y))


class Button(object):

    COLOR = (198, 226, 255) #light gray
    HOVER_COLOR = (159, 182, 205) #dark blue

    @staticmethod
    def loadImage():
        Button.panel = pygame.image.load(os.path.join("button-panel.png")).convert_alpha()
        scale = 13
        w, h = Button.panel.get_size()
        Button.panel = pygame.transform.scale(Button.panel, (w/scale, h/scale))
        Button.width, Button.height = Button.panel.get_size()
        Button.margin = 6


    def __init__(self, x, y, text):
        self.x, self.y = x, y
        self.text = text
        self.color = Button.COLOR
        self.rect = pygame.Rect(self.x, 
            self.y, 
            Button.width, Button.height)
        

    def draw(self, screen):
        screen.blit(Button.panel, (self.x, self.y))
        rect = (self.x+Button.margin, self.y+Button.margin, 
            Button.width-2*Button.margin, Button.height-2*Button.margin)
        AAfilledRoundedRect(screen, rect, self.color, 0.2)


class LightRay(InteractiveObject):

    @staticmethod
    def loadImage():
        scale = 10
        image = pygame.image.load(os.path.join("yellowArc.png")).convert_alpha()
        image = pygame.transform.rotate(image, 47)
        w, h = image.get_size()
        LightRay.big = pygame.transform.scale(image, (w/(int(scale/1.5)), h/scale))
        scale = 15
        LightRay.medium = pygame.transform.scale(image, (w/(int(scale/1.5)), h/scale))
        scale = 20
        LightRay.small = pygame.transform.scale(image, (w/(int(scale/1.5)), h/scale))


    def __init__(self, x, y, image):
        super(LightRay, self).__init__(x, y, image)
        self.speed = 5

    def update(self):
        self.y += self.speed
        self.updateRect()

class Explosion(InteractiveObject):

    timeOnScreen = 20

    @staticmethod
    def loadImage():
        image = pygame.image.load(os.path.join("explosion.png")).convert_alpha()
        w, h = image.get_size()
        scale = 7
        image = pygame.transform.scale(image, (w/scale, h/scale))
        Explosion.image = image

    def __init__(self, x, y, image):
        super(Explosion, self).__init__(x, y, image)
        self.counter = 0

    def update(self):
        self.counter+=1
        if self.counter > Explosion.timeOnScreen:
            self.kill()


#AAfilledRoundedRect function from pygame.org/project-AAfilledRoundedRect-2349-.html
def AAfilledRoundedRect(surface,rect,color,radius=0.4):

    """
    AAfilledRoundedRect(surface,rect,color,radius=0.4)

    surface : destination
    rect    : rectangle
    color   : rgb or rgba
    radius  : 0 <= radius <= 1
    """

    rect         = pygame.Rect(rect)
    color        = pygame.Color(*color)
    alpha        = color.a
    color.a      = 0
    pos          = rect.topleft
    rect.topleft = 0,0
    rectangle    = pygame.Surface(rect.size,pygame.SRCALPHA)

    circle       = pygame.Surface([min(rect.size)*3]*2,pygame.SRCALPHA)
    pygame.draw.ellipse(circle,(0,0,0),circle.get_rect(),0)
    circle       = pygame.transform.smoothscale(circle,[int(min(rect.size)*radius)]*2)

    radius              = rectangle.blit(circle,(0,0))
    radius.bottomright  = rect.bottomright
    rectangle.blit(circle,radius)
    radius.topright     = rect.topright
    rectangle.blit(circle,radius)
    radius.bottomleft   = rect.bottomleft
    rectangle.blit(circle,radius)

    rectangle.fill((0,0,0),rect.inflate(-radius.w,0))
    rectangle.fill((0,0,0),rect.inflate(0,-radius.h))

    rectangle.fill(color,special_flags=pygame.BLEND_RGBA_MAX)
    rectangle.fill((255,255,255,alpha),special_flags=pygame.BLEND_RGBA_MIN)

    return surface.blit(rectangle,pos)


#mode code from mode demo in event based animation notes
class Game(PygameGame):

    COLOR_ORANGE = (255, 165, 0)

    COLOR_BLUE = (0, 0, 255)

    games_played = 0

    scores = []

####################################
# init
####################################

    def init(self):
        self.mode = "splashScreen"
        self.title = "Deep Sea Diver"
        self.gameOver = False
        self.counter = 0
        self.bgImage = pygame.image.load(os.path.join('tpbackground.jpeg')).convert_alpha()
        self.bgImage = pygame.transform.scale(self.bgImage, (self.width, self.height))
        self.initSplashScreenDiver()
        self.diverLives = 3
        self.loadAllImages()
        self.font = pygame.font.Font(os.path.join("janda-manatee.solid.ttf"), Button.height/2)
        self.score_font = pygame.font.SysFont("Arial Rounded MT Bold", 30)
        self.helpFont = pygame.font.SysFont("Arial", 13)
        self.scoresFont = pygame.font.SysFont("Arial Rounded MT Bold", 20)
        self.diverGroup = pygame.sprite.Group(Diver(self.width/2, 
            self.height/10,
            Diver.images[0]))
        self.diver = self.diverGroup.sprites()[0]
        self.mineGroup = pygame.sprite.Group()
        self.coinGroup = pygame.sprite.Group()
        self.nonDangerousFishGroup = pygame.sprite.Group()
        self.dangerousFishGroup = pygame.sprite.Group()
        self.anglerGroup = pygame.sprite.Group()
        self.caveGroup = pygame.sprite.Group()
        self.darkCaveGroup = pygame.sprite.Group()
        self.rayGroup = pygame.sprite.Group()
        self.explosionGroup = pygame.sprite.Group()
        self.newMine()
        self.initLives()
        self.initUIButtons()
        self.initGameOverButtons()
        self.initOtherButtons()
        self.initLevelButtons()
        self.blinkCount = None
        self.score = 0

        #scrolling code adapted from www.youtube.com/watch?v=qKyy6374V8E 

        self.worldshift = 0.75
        self.shiftChange = 2
        self.caveOnScreen = False

        self.demoOn = True

    def loadAllImages(self):
        Diver.loadImage()
        Mine.loadImage()
        Lives.loadImage()
        Coin.loadImage()
        NonDangerousFish.loadImage()
        DangerousFish.loadImage()
        AnglerFish.loadImage()
        Button.loadImage()
        LightRay.loadImage()
        Explosion.loadImage()

    def initSplashScreenDiver(self):
        image = pygame.image.load(os.path.join("splashscreendiver.gif")).convert_alpha()
        w, h = image.get_size()
        scale = 10
        self.splashScreenDiver = pygame.transform.scale(image, (w/scale, h/scale))

    def initLives(self):
        L1 = Lives(10, 10)
        L2 = Lives(25, 10)
        L3 = Lives(40, 10)
        self.lives = [L1, L2, L3]

    def initUIButtons(self):
        left = (self.width/5)*3
        top = self.height/5
        verticalGap = 10+Button.height
        playButton = Button(left, top, "PLAY")
        scoresButton = Button(left, top+verticalGap, "SCORES")
        helpButton = Button(left, top+2*verticalGap, "HELP")
        quitButton = Button(left, top+3*verticalGap, "QUIT")
        self.UIButtons = [playButton, scoresButton, helpButton,
                          quitButton]

    def initGameOverButtons(self):
        left = self.width/3
        top = self.height/3
        verticalGap = 10+Button.height
        menuButton = Button(left, top, "MENU")
        quitButton = Button(left, top+verticalGap, "QUIT")
        self.overButtons = [menuButton, quitButton]

    def initLevelButtons(self):
        left = self.width/3
        top = self.height/4
        verticalGap = 10+Button.height
        easyButton = Button(left, top, "EASY")
        mediumButton = Button(left, top+verticalGap, "MEDIUM")
        hardButton = Button(left, top+verticalGap*2, "HARD")
        self.levelButtons = [easyButton, mediumButton, hardButton]

    def initOtherButtons(self):
        left = self.width/3
        top = self.height/15
        helpMenuButton = Button(left, top, "MENU")
        scoresMenuButton = Button(left, top, "MENU")
        self.helpMenuButton = helpMenuButton
        self.scoresMenuButton = scoresMenuButton

    def drawButtonText(self, button, screen):
        button.draw(screen)
        text = self.font.render(button.text, True, Game.COLOR_BLUE)
        if button.text == "SCORES" or button.text == "MEDIUM":
            xShift = 1.5
        else:
            xShift = 5
        pos = (button.x+xShift*Button.margin,
               button.y+2*Button.margin)
        screen.blit(text, pos)


####################################
# mode dispatcher
####################################

    def mousePressed(self, x, y):
        if (self.mode == "splashScreen"): self.splashScreenMousePressed(x, y)
        elif (self.mode == "playGame"):   self.gameMousePressed(x, y)
        elif (self.mode == "help"):       self.helpMousePressed(x, y)
        elif (self.mode == "over"): self.overMousePressed(x, y)
        elif (self.mode == "scores"): self.scoresMousePressed(x, y)
        elif (self.mode == "levels"): self.levelsMousePressed(x, y)

    def mouseMotion(self, x, y):
        if (self.mode == "splashScreen"): self.splashScreenMouseMotion(x, y)
        elif (self.mode == "help"): self.helpMouseMotion(x, y)
        elif (self.mode == "over"): self.overMouseMotion(x, y)
        elif (self.mode == "scores"): self.scoresMouseMotion(x, y)
        elif (self.mode == "levels"): self.levelsMouseMotion(x, y)

    def keyPressed(self, keyCode, modifier):
        if (self.mode == "splashScreen"): self.splashScreenKeyPressed(keyCode, modifier)
        elif (self.mode == "playGame"): self.gameKeyPressed(keyCode, modifier)
        elif (self.mode == "help"): self.helpKeyPressed(keyCode, modifier)

    def keyReleased(self, keyCode, modifier):
        if (self.mode == "playGame"): self.gameKeyReleased(keyCode, modifier)

    def timerFired(self, dt):
        if (self.mode == "splashScreen"): self.splashScreenTimerFired()
        elif (self.mode == "playGame"):   self.gameTimerFired()
        elif (self.mode == "help"):       self.helpTimerFired()
        elif (self.mode == "over"): self.overTimerFired()

    def redrawAll(self, screen):
        if (self.mode == "splashScreen"): self.splashScreenRedrawAll(screen)
        elif (self.mode == "playGame"):   self.gameRedrawAll(screen)
        elif (self.mode == "help"):       self.helpRedrawAll(screen)
        elif (self.mode == "over"): self.overRedrawAll(screen)
        elif (self.mode == "scores"): self.scoresRedrawAll(screen)
        elif (self.mode == "levels"): self.levelsRedrawAll(screen)

####################################
# splashScreen mode
####################################

    def splashScreenMousePressed(self, x, y):
        for button in self.UIButtons:
             if button.rect.collidepoint(x, y):
                if button.text == "PLAY":
                    if Game.games_played!=0:
                        self.reset()
                    self.mode = "levels"
                elif button.text == "SCORES":
                    self.mode = "scores"
                    self.organizeScores()
                elif button.text == "HELP":
                    self.mode = "help"
                elif button.text == "QUIT":
                    pygame.quit()
                button.color = Button.COLOR


    def splashScreenMouseMotion(self, x, y):
        for button in self.UIButtons:
            if button.rect.collidepoint(x, y):
                button.color = Button.HOVER_COLOR
            else:
                button.color = Button.COLOR

    def splashScreenKeyPressed(self, keyCode, modifier):
        pass
        
    def splashScreenTimerFired(self):
        pass

    def splashScreenRedrawAll(self, screen):
        self.drawBackground(screen)
        screen.blit(self.splashScreenDiver, (self.width/20, self.height/3))
        title = self.font.render(self.title, True, Game.COLOR_BLUE)
        screen.blit(title, (self.width/5, self.height/15))
        for button in self.UIButtons:
            self.drawButtonText(button, screen)

##################################
# level mode
##################################

    def easySettings(self):
        self.coinFrequency = 25
        self.fishFrequency = 180
        self.sharkFrequency = 300
        self.anglerFrequency = 700
        self.caveFrequency = 500

    def mediumSettings(self):
        self.coinFrequency = 25
        self.fishFrequency = 180
        self.sharkFrequency = 250
        self.anglerFrequency = 400
        self.caveFrequency = 600

    def hardSettings(self):
        self.coinFrequency = 25
        self.fishFrequency = 180
        self.sharkFrequency = 100
        self.anglerFrequency = 300
        self.caveFrequency = 500

    def levelsMousePressed(self, x, y):
        for button in self.levelButtons:
             if button.rect.collidepoint(x, y):
                if button.text == "EASY":
                    self.easySettings()
                elif button.text == "MEDIUM":
                    self.mediumSettings()
                elif button.text == "HARD":
                    self.hardSettings()
                self.mode = "playGame"
                button.color = Button.COLOR

    def levelsMouseMotion(self, x, y):
        for button in self.levelButtons:
            if button.rect.collidepoint(x, y):
                button.color = Button.HOVER_COLOR
            else:
                button.color = Button.COLOR


    def levelsRedrawAll(self, screen):
        self.drawBackground(screen)
        for button in self.levelButtons:
            self.drawButtonText(button, screen)


          
####################################
# help mode
####################################

    def helpMousePressed(self, x, y):
        if self.helpMenuButton.rect.collidepoint(x, y):
            self.mode = "splashScreen"
            self.helpMenuButton.color = Button.COLOR

    def helpMouseMotion(self, x, y):
        if self.helpMenuButton.rect.collidepoint(x, y):
            self.helpMenuButton.color = Button.HOVER_COLOR
        else:
            self.helpMenuButton.color = Button.COLOR

    def helpKeyPressed(self, keyCode, modifier):
        pass

    def helpTimerFired(self):
        pass

    def helpRedrawAll(self, screen):
        gap = 15
        margin = 5
        self.drawBackground(screen)
        instructions = readFile(os.path.join("instructions.txt"))
        lines = instructions.splitlines()
        for lineNumber in xrange(len(lines)):
            line = lines[lineNumber]
            toPrint = self.helpFont.render(line, True, (255,255,255))
            screen.blit(toPrint, (margin, (lineNumber+1)*gap+self.height/4))
        self.helpMenuButton.draw(screen)
        self.drawButtonText(self.helpMenuButton, screen)

####################################
# playGame mode
###################################

    def reset(self):
        self.initLives()
        self.score = 0
        self.diverGroup = pygame.sprite.Group(Diver(self.width/2, 
            self.height/10,
            Diver.images[0]))
        self.diver = self.diverGroup.sprites()[0]
        self.mineGroup = pygame.sprite.Group()
        self.coinGroup = pygame.sprite.Group()
        self.nonDangerousFishGroup = pygame.sprite.Group()
        self.dangerousFishGroup = pygame.sprite.Group()
        self.anglerGroup = pygame.sprite.Group()
        self.caveGroup = pygame.sprite.Group()
        self.darkCaveGroup = pygame.sprite.Group()
        self.rayGroup = pygame.sprite.Group()
        self.explosionGroup = pygame.sprite.Group()
        self.counter = 0
        self.blinkCount = None
        self.worldshift = 0.75
        self.newMine()
        self.newFish()
     
    def newMine(self):
        #add code to make sure mine does not appear where diver is positioned
        collided = True
        while collided:
            mineX = random.randint(10, self.width-10)
            mineY = random.randint(self.height/3, self.height-2)
            #check to make sure Mine doesnt spawn on top of diver
            checkMine = Mine(mineX, mineY, Mine.image)
            collided = pygame.sprite.collide_rect(checkMine, self.diver)
        self.mineGroup.add(checkMine)

    def newFish(self):
        if self.counter%self.fishFrequency==0:
            self.nonDangerousFishGroup.add(NonDangerousFish(self.width, self.height))
        if self.counter%self.sharkFrequency==0 and self.counter!=0:
            self.dangerousFishGroup.add(DangerousFish(self.width, self.height))
        if self.counter%self.anglerFrequency==0 and self.counter!=0:
            self.anglerGroup.add(AnglerFish(self.width, self.height))

    def newGreenFish(self):
        self.nonDangerousFishGroup.add(NonDangerousFish(self.width, self.height))

    def newShark(self):
        self.dangerousFishGroup.add(DangerousFish(self.width, self.height))

    def newAngler(self):
        self.anglerGroup.add(AnglerFish(self.width, self.height))

    def newCoin(self):
        if self.counter%self.coinFrequency==0:
            coinX = random.randint(0, self.width-5)
            self.coinGroup.add(Coin(coinX, self.height))

    def newCave(self):
        if (len(self.caveGroup.sprites())==0
            and self.counter%self.caveFrequency==0 and self.counter!=0):
            for loc in xrange(1, 8, 3):
                self.caveGroup.add(Cave(self.width, self.height, loc))
            for loc in [2, 3, 5, 6]:
                self.darkCaveGroup.add(DarkCave(self.width, self.height, loc))
            avoidCave = random.choice([2,5])
            width = self.darkCaveGroup.sprites()[0].width
            mineY = self.darkCaveGroup.sprites()[0].y
            self.mineGroup.add(Mine(width*avoidCave, mineY, Mine.image))
        if (len(self.caveGroup.sprites())>0 
            and self.caveGroup.sprites()[0].rect.bottom > self.diver.rect.top):
            self.caveOnScreen = True
        else:
            self.caveOnScreen = False



    def gameTimerFired(self):
        if self.lives == []:
            self.mode = "over"
            Game.games_played+=1
            Game.scores+=[self.score]
        self.diverGroup.update(self.isKeyPressed, self.width, self.height)
        self.nonDangerousFishGroup.update()
        self.dangerousFishGroup.update()
        self.coinGroup.update()
        self.mineGroup.update()
        self.anglerGroup.update(self.diver)
        self.caveGroup.update()
        self.darkCaveGroup.update()
        self.rayGroup.update()
        self.explosionGroup.update()
        self.removeOffscreenObjects()
        self.shiftWorld()
        self.checkAllCollisions()
        if not self.caveOnScreen:
            if not self.demoOn:
                self.newFish()
            self.newCave()
            self.newCoin()
        self.counter+=1
        if self.blinkCount!=None: self.blinkCount+=1
        if self.blinkCount>Diver.fadeTime: self.fadedDiverOnAndOff()

    def checkAllCollisions(self):
        if not self.diver.isFaded:
            self.checkMineCollisions()
            self.checkNonDangerousFishCollisions()
            self.checkDangerousFishCollisions()
            self.checkAnglerCollisions()
            self.checkCoinCollisions()
        self.checkDiverCaveCollisions()
        self.checkLightRayDarkCaveCollisions()

    def checkMineCollisions(self):
        if pygame.sprite.groupcollide(self.diverGroup, self.mineGroup, False, True, pygame.sprite.collide_circle):
            self.newMine()
            if len(self.lives)!=0: self.lives.pop()
            self.explosionGroup.add(Explosion(self.diver.x, self.diver.y,
                Explosion.image))
            self.fadedDiverOnAndOff()

    def checkCoinCollisions(self):
        if pygame.sprite.groupcollide(self.diverGroup, self.coinGroup, False, True, pygame.sprite.collide_circle):
            self.score+=10

    def checkDangerousFishCollisions(self):
        if pygame.sprite.spritecollideany(self.diver, self.dangerousFishGroup)!=None:
            self.fadedDiverOnAndOff()
            if len(self.lives)!=0: self.lives.pop()
            self.explosionGroup.add(Explosion(self.diver.x, self.diver.y,
                Explosion.image))
       
    def fadedDiverOnAndOff(self):
        if self.blinkCount == None: self.blinkCount = 0
        else: self.blinkCount = None
        self.diver.isFaded = not self.diver.isFaded

    def checkNonDangerousFishCollisions(self):
        check = pygame.sprite.spritecollideany(self.diver, self.nonDangerousFishGroup, pygame.sprite.collide_circle)
        if check!= None:
            check.divertDiver(self.diver)

    def checkAnglerCollisions(self):
        if pygame.sprite.spritecollideany(self.diver, self.anglerGroup)!=None:
            for angler in self.anglerGroup.sprites(): angler.canFollow = False
            self.fadedDiverOnAndOff()
            if len(self.lives)!=0: self.lives.pop()
            self.explosionGroup.add(Explosion(self.diver.x, self.diver.y,
                Explosion.image))

    #based on collision code from pygame.org/project-Rect+Collision+Response-1061-.html
    def checkDiverCaveCollisions(self):
        collide_dict = pygame.sprite.groupcollide(self.diverGroup, self.caveGroup, False, False)
        if collide_dict != {}:
            cave = collide_dict[self.diver][0]
            if self.diver.rect.bottom>cave.rect.top and self.diver.rect.top<cave.rect.bottom:
                if self.diver.dx > 0 and self.diver.rect.left < cave.rect.left: # Moving right; Hit the left side of the cave
                    self.diver.x = cave.rect.left - self.diver.width/2
                elif self.diver.dx < 0 and self.diver.rect.right > cave.rect.right: # Moving left; Hit the right side of the cave
                    self.diver.x = cave.rect.right + self.diver.width/2
            if self.diver.dy > 0 and self.diver.rect.top < cave.rect.top: # Moving down; Hit the top side of the cave
                self.diver.y = cave.rect.top - self.diver.height/2
            elif self.diver.dy < 0 and self.diver.rect.bottom > cave.rect.bottom: # Moving up; Hit the bottom side of the cave
                self.diver.y = cave.rect.bottom + self.diver.height/2

    def checkLightRayDarkCaveCollisions(self):
        if pygame.sprite.groupcollide(self.rayGroup, self.darkCaveGroup, True, False):
            for cave in self.darkCaveGroup.sprites():
                cave.isFading = True

    def removeOffscreenObjects(self):
        toKill = []
        for fish in self.nonDangerousFishGroup.sprites():
            if fish.x<0 or fish.x>self.width or fish.y<0:
                toKill.append(fish)
        self.nonDangerousFishGroup.remove(toKill)
        toKill = []
        for shark in self.dangerousFishGroup.sprites():
            if shark.x<0 or shark.x>self.width or shark.y<0:
                toKill.append(shark)
        self.dangerousFishGroup.remove(toKill)
        toKill = []
        for angler in self.anglerGroup.sprites():
            if angler.x<0 or angler.x>self.width or angler.y<0 or angler.y>self.height*1.5:
                toKill.append(angler)
        self.anglerGroup.remove(toKill)
        toKill = []
        for mine in self.mineGroup.sprites():
            if mine.x<0 or mine.x>self.width or mine.y<0 or mine.y>self.height*1.5:
                toKill.append(mine)
        self.mineGroup.remove(toKill)
        toKill = []
        for coin in self.coinGroup.sprites():
            if coin.x<0 or coin.x>self.width or coin.y<0 or coin.y>self.height*1.5:
                toKill.append(coin)
        self.coinGroup.remove(toKill)
        toKill = []
        for ray in self.rayGroup.sprites():
            if ray.x<0 or ray.x>self.width or ray.y<0 or ray.y>self.height*1.5:
                toKill.append(ray)
        self.rayGroup.remove(toKill)
        toKill = []
        for cave in self.caveGroup.sprites():
            if cave.rect.bottom < 0:
                toKill.append(cave)
        self.caveGroup.remove(toKill)
        toKill = []
        for darkCave in self.darkCaveGroup.sprites():
            if darkCave.rect.bottom < 0:
                toKill.append(darkCave)
        self.darkCaveGroup.remove(toKill)
   
    def shiftWorld(self):
        allObjects = (self.mineGroup.sprites()
                    +self.nonDangerousFishGroup.sprites()
                    +self.dangerousFishGroup.sprites()
                    +self.anglerGroup.sprites()
                    +self.coinGroup.sprites()
                    +self.caveGroup.sprites()
                    +self.darkCaveGroup.sprites())

        for obj in allObjects:
            if type(obj) == Coin:
                obj.y-=3*self.worldshift
            #Caves and Mines move at the same pace because mine are inside caves sometimes
            #Caves move fast so the diver doesn't have to wait for them to pass
            elif isinstance(obj, Cave) or type(obj)==Mine:
                obj.y-=2*self.worldshift
            else:
                obj.y-=self.worldshift

    # key pressed function controls scrolling in the game
    # it is easier to move downwards than upwards because the diver is meant to be falling downwards

    def gameKeyPressed(self, keyCode, modifier):
        if keyCode == pygame.K_f:
            x = self.diver.x
            yBig = self.diver.rect.bottom + self.diver.height
            yMedium = self.diver.rect.bottom + self.diver.height/2
            ySmall = self.diver.rect.bottom + self.diver.height/4
            self.rayGroup.add(LightRay(x, yBig, LightRay.big))
            self.rayGroup.add(LightRay(x, yMedium, LightRay.medium))
            self.rayGroup.add(LightRay(x, ySmall, LightRay.small))
        elif keyCode == pygame.K_DOWN:
            self.worldshift += self.shiftChange
        elif keyCode == pygame.K_UP:
            self.worldshift -= 1
        elif keyCode == pygame.K_ESCAPE:
            self.mode = "splashScreen"
        elif keyCode == pygame.K_g:
            self.newGreenFish()
        elif keyCode == pygame.K_s:
            self.newShark()
        elif keyCode == pygame.K_a:
            self.newAngler()
        elif keyCode == pygame.K_c:
            self.newCave()

    def gameKeyReleased(self, keyCode, modifier):
        if keyCode == pygame.K_DOWN:
            self.worldshift -= self.shiftChange
        elif keyCode == pygame.K_UP:
            self.worldshift += 1

    def gameMousePressed(self, x, y):
        pass

    def gameRedrawAll(self, screen):
        self.drawBackground(screen)
        self.coinGroup.draw(screen)
        self.mineGroup.draw(screen)
        self.nonDangerousFishGroup.draw(screen)
        self.dangerousFishGroup.draw(screen)
        self.anglerGroup.draw(screen)
        self.caveGroup.draw(screen)
        self.darkCaveGroup.draw(screen)
        self.rayGroup.draw(screen)
        self.explosionGroup.draw(screen)
        self.diverGroup.draw(screen)
        for life in self.lives: life.draw(screen)
        score = self.score_font.render(str(self.score), True, Game.COLOR_ORANGE)
        scoreX = 0.88*self.width
        screen.blit(score, (scoreX, 7))

    def drawBackground(self, screen):
        screen.blit(self.bgImage, (0, 0))


################################################
# scores mode
################################################

    #makes sure only top ten scores are displayed
    def organizeScores(self):
        if len(Game.scores) > 10:
            minIndex = Game.scores.index(min(Game.scores))
            Game.scores.pop(minIndex)
        Game.scores.sort(reverse = True)

    def scoresMousePressed(self, x, y):
        if self.scoresMenuButton.rect.collidepoint(x, y):
            self.mode = "splashScreen"
            self.scoresMenuButton.color = Button.COLOR

    def scoresMouseMotion(self, x, y):
        if self.scoresMenuButton.rect.collidepoint(x, y):
            self.scoresMenuButton.color = Button.HOVER_COLOR
        else:
            self.scoresMenuButton.color = Button.COLOR

    def scoresKeyPressed(self, keyCode, modifier):
        pass

    def scoresTimerFired(self):
        pass

    def scoresRedrawAll(self, screen):
        self.drawBackground(screen)
        self.scoresMenuButton.draw(screen)
        self.drawButtonText(self.scoresMenuButton, screen)
        gamesPlayed = self.scoresFont.render("Games played: "+str(Game.games_played), 
            True, (255, 255, 255))
        verticalGap = 20
        screen.blit(gamesPlayed, (self.width/3, self.height/4))
        #######breaks in case there are not 10 scores yet
        for score in xrange(10):
            if score == len(Game.scores):
                break
            scoreStr = self.scoresFont.render(str(score+1)+". "+
                str(Game.scores[score]), True, (255, 255, 255))
            screen.blit(scoreStr, (self.width/3, 
            self.height/3+verticalGap*score))

##################################################
# game over mode
##################################################

    def overMousePressed(self, x, y):
        for button in self.overButtons:
             if button.rect.collidepoint(x, y):
                button.color = Button.COLOR
                if button.text == "MENU":
                    self.mode = "splashScreen"
                elif button.text == "QUIT":
                    pygame.quit()
                
    def overMouseMotion(self, x, y):
        for button in self.overButtons:
            if button.rect.collidepoint(x, y):
                button.color = Button.HOVER_COLOR
            else:
                button.color = Button.COLOR

    def overTimerFired(self):
        pass

    def overRedrawAll(self, screen):
        self.drawBackground(screen)
        score = self.font.render("SCORE: "+str(self.score), True, Game.COLOR_ORANGE)
        screen.blit(score, (self.width/3, self.height/5))
        for button in self.overButtons:
            self.drawButtonText(button, screen)

Game(500, 500, 20).run()
        







