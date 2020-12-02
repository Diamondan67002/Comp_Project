import pygame, os

class Track(pygame.sprite.Sprite):
    images=["Track-Straight.png","Track-Curved.png","Track-Diagonal.png"]
    colourKey=(255,255,255)
    def __init__(self,coords,img,initConnect):### Image loading could be made bettter by preloading all the png's into python rather than loading 1 everytime an object is created or image altered
        print("Track Commenced")
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('photos',self.images[img]))
        self.image.convert_alpha()
        self.image.set_colorkey(self.colourKey)###????????
        self.rect = self.image.get_rect()
        self.rect.x = coords[0]*32
        self.rect.y = coords[1]*32

        self.connections=[-1,-1]
        self.vehicle=''
        self.orientation=0
        self.curve=0
        self.add_connection(initConnect[0],initConnect[1],initConnect[2])

    def add_connection(self,direction,lineNum,posNum):
        self.connections[direction]=[lineNum,posNum]

    def get_connections(self):### Don't really need
        return self.connections

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
        self.image = pygame.image.load(os.path.join('photos',self.images[img]))## Need to resolve alterations of image.

    def get_image(self):
        return self.image

    def move_track_point(self,coords):
        self.rect.x = coords[0]*32
        self.rect.y = coords[1]*32

    def move_track(self,coords,connections):
        self.move_track_point(coords)
        for i in range(len(connections)):
            self.add_connection(connections[i][0],connections[i][1],connections[i][2])

class Point(Track):
    images=["Point-straight.png","Point-diagonal.png"]
    def __init__(self,coords,img,initConnect):
        print("Point Commenced")
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('photos',self.images[img]))
        self.image.convert_alpha()
        self.image.set_colorkey(self.colourKey)  ###????????
        self.rect = self.image.get_rect()
        self.rect.x = coords[0]*32
        self.rect.y = coords[1]*32

        ###???????????????????? You need to call the parent constructor (Track.__init__()  ) explicitly IF you wish to use it....
        self.connections=[-1,-1,-1]
        self.pointBlade=PointBlade(coords,self.colourKey)
        self.hand=0
        self.add_connection(initConnect[0],initConnect[1],initConnect[2])

    def change_hand(self):
        self.hand=1-self.hand

class PointBlade(pygame.sprite.Sprite):### Need to add pygame.sprite.Sprite to the inheritance
    images=["PointBlade-Straight.png","PointBlade-Curved.png"]### Might need an additional png but would alter the the changeing system unless I just rebuilt it as a 2d list.
    def __init__(self,coords,colourkey):
        self.colourkey=colourkey
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('photos',self.images[0]))
        self.image.convert_alpha()
        self.image.set_colorkey(self.colourkey)  ###????????
        self.rect = self.image.get_rect()
        self.rect.x = coords[0] * 32
        self.rect.y = coords[1] * 32

        self.direction=0

    def changeDirection(self):
        self.direction=1-self.direction ### Probably need to do this for all the other places I need to flip orientation as it is much cleaner.

class Siding():
    def __init__(self,length,startCoords,imgNums,initConnect):
        print("Siding Commenced")
        self.track=[]
        self.length=length
        self.connections=[-1,-1]
        self.coords=startCoords ### Not sure if I need.
        self.add_connection(initConnect[0],initConnect[1],initConnect[2])
        self.buildSiding(imgNums,self.coords,initConnect)

    def add_track(self,initConnect):
        self.track.append(Track([self.coords[0],self.coords[1]+self.length],0,initConnect))
        self.length=self.length+1

    def pre_add_track(self,initConnect):
        self.coords[1]=self.coords[1]-1
        self.track.insert(0,Track(self.coords,0,initConnect))
        self.length=self.length+1

    def buildSiding(self,imgNums,coords,initConnect):
        for i in range(self.length):
            if i>0:
                initConnect[2]=initConnect[2]+1
            self.track.append(Track(coords,imgNums[i],initConnect))### Need to set up all the alignments of x and y coords coming down from the initial map function.
            coords[1]=coords[1]+1

    def add_connection(self,direction,lineNum,posNum):
        self.connections[direction]=[lineNum,posNum]

    def get_connections(self):### Don't really need
        return self.connections

    def check_length(self):
        return self.length

class DeadEndSiding(Siding):
    def __init__(self):
        super().__init__()###???????????????????
        self.connections=[-1]

class Wagon():
    def __init__(self,name):
        self.name=name

class Line():### A Line probably going to have a fixed y value but could be altered in future.
    def __init__(self,setup,startCoords,connections):
        self.line=[]
        self.buildLine(setup,startCoords,connections)

    def buildLine(self,setup,coords,connections):### Actually builds and configures the line. Passing variable into Point() and Siding()
        for i in range(len(setup)):
            if setup[i][0]==-1:
                self.line.append(Point(coords,setup[i][1],[0,connections[0],connections[1]]))#### Need to continue passing though the GUI coords.
                coords[0]=coords[0]+1
                connections[1]=connections[1]+1
            elif setup[i][0]>=1:
                self.line.append(Siding(setup[i][0],coords,setup[i][1],[0,connections[0],connections[1]]))### Issues. Coords and connections are effectively duplicates that should be in tegrated together.
                coords[0]=coords[0]+setup[i][0]
                connections[1]=connections[1]+setup[i][0]

    def get_component_no(self,y_coord):### Can we chack what type of object an item in a list is??
        y = 0
        linePos = 0
        running = True
        while running:
            if len(self.line[y].get_connections()) == 2:
                y +=1
            elif len(self.line[y].get_connections()) == 3:
                y = y + self.line[y].check_length()

            linePos += 1
            if y > y_coord:
                sidingPos = y_coord - y
                point = False
                running = False
            elif y == y_coord:
                running = False
                point = True

        if point == True:
            return linePos,sidingPos
        return linePos