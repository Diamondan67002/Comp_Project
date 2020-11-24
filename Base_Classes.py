import pygame

class Track(pygame.sprite.Sprite):
    images=["Track-Straight.png","Track-Curved.png","Track-Diagonal.png"]
    def __init__(self,coords,img,initConnect):
        print("Track Commenced")
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(self.images[img]))
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)###????????
        self.rect = self.image.get_rect()
        self.rect.x = coords[0]*32
        self.rect.y = coords[1]*32

        self.connections=[-1,-1]
        self.vehicle=''
        self.orientation=0
        self.curve=0
        ##self.image=self.images[0]
        self.add_connection(initConnect[0],initConnect[1],initConnect[2])

    def add_connection(self,direction,lineNum,posNum):
        self.connections[direction]=[lineNum,posNum]

    def add_vehicle(self,vehicle):
        self.vehicle=vehicle

    def remove_vehicle(self):
        self.vehicle=''

    def check_vehicle(self):
        return self.vehicle

    def change_orientation(self):
        self.orientation=1-self.orientation

    def change_curve(self):
        self.curve=1-self.curve

    def set_image(self,img_num):### Integrated into constructor
        self.image=self.images[img_num]

class Point(Track):
    images=["Point-straight.png","Point-diagonal.png"]
    def __init__(self,coords,img,initConnect):
        print("Point Commenced")
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(self.images[img]))
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)  ###????????
        self.rect = self.image.get_rect()
        self.rect.x = coords[0]*32
        self.rect.y = coords[1]*32

        ###???????????????????? You need to call the parent constructor (Track.__init__()  ) explicitly IF you wish to use it....
        self.connections=[-1,-1,-1]
        self.pointBlade=PointBlade()
        self.hand=0
        self.add_connection(initConnect[0],initConnect[1],initConnect[2])

    def change_hand(self):
        self.hand=1-self.hand

class PointBlade():
    images=["PointBlade-Straight.png","PointBlade-Curved.png"]
    def __init__(self):
        self.image=self.images[0]
        self.direction=0

    def changeDirection(self):
        self.direction=1-self.direction ### Probably need to do this for all the other places I need to flip orientation as it is much cleaner.

class Siding():
    def __init__(self,length,startCoords,imgNums):
        print("Siding Commenced")
        self.track=[]
        self.length=length
        self.connections=[-1,-1]
        self.startCoords=startCoords ### Not sure if I need.

    def add_track(self):
        self.track.append(Track([0,self.track[-1].],0,))
        self.length=self.length+1

    def pre_add_track(self):
        self.track.insert(0,Track)
        self.length=self.length+1

    def buildSiding(self,length,imgNums):
        for i in range(length):
            self.track.append(Track())### Need to set up all the alignments of x and y coords coming down from the initial map function.

class DeadEndSiding(Siding):
    def __init__(self):
        super().__init__()###???????????????????
        self.connections=[-1]

class Wagon():
    def __init__(self,name):
        self.name=name

class Line():
    def __init__(self,setup,startCoords):
        self.line=[]
        self.buildLine(setup,startCoords)

    def buildLine(self,setup,coords):
        for i in range(len(setup)):
            if setup[i][0]==-1:
                self.line.append(Point(coords,setup[i][1]))#### Need to continue passing though the GUI coords.
                coords[0]=coords[0]+1
            elif setup[i][0]>=1:
                self.line.append(Siding(setup[i],coords,setup[i][1]))
                coords[0]=coords[0]+setup[i][0]