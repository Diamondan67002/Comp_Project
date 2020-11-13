import pygame

class Track(pygame.sprite.Sprite):
    images=[]
    def __init__(self,x,y,img):
        pygame.sprite.Sprite.__init__(self)##Need to continue
        self.image = pygame.image.load(os.path.join(self.images[img]))
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)###????????
        self.rect = self.image.get_rect
        self.rect.x = x
        self.rect.y = y

        self.connections=[-1,-1]
        ##self.vehicle=''
        ##self.orientation=False
        ##self.curve=False
        ##self.image=self.images[0]

    def add_connection(self,direction,object,object_end):
        self.connections[direction]=[object,object_end]

    def add_vehicle(self,vehicle):
        self.vehicle=vehicle

    def remove_vehicle(self):
        self.vehicle=''

    def check_vehicle(self):
        return self.vehicle

    def change_orientation(self):
        if self.orientation == True:
            self.orientation = False
        elif self.orientation == False:
            self.orientation = True

    def change_curve(self):
        if self.curve == True:
            self.curve = False
        elif self.curve== False:
            self.curve = True

    def set_image(self,img_num):### Integrated into constructor
        self.image=self.images[img_num]

class Point(Track):
    images=[]
    def __init__(self):
        super().__init__()###???????????????????? You need to call the parent constructor (Track.__init__()  ) explicitly IF you wish to use it....
        self.connections=[-1,-1,-1]
        self.pointBlade=PointBlade()
        self.hand=0

    def change_hand(self):
        self.hand=1-self.hand

class PointBlade():
    images=[]
    def __init__(self):
        self.image=self.images[0]
        self.direction=0

    def changeDirection(self):
        self.direction=1-self.direction ### Probably need to do this for all the other places I need to flip orientation as it is much cleaner.

class Siding():
    def __init__(self):
        self.track=[]
        self.length=0
        self.connections=['','']

    def add_track(self):
        self.track.append(Track)
        self.length=self.length+1

class DeadEndSiding(Siding):
    def __init__(self):
        super().__init__()###???????????????????
        self.connections=['']

class Wagon():
    def __init__(self,name):
        self.name=name