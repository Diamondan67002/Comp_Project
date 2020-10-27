import pygame

class Track():
    images=[]
    def __init__(self):
        self.connections=['','']
        self.vehicle=''
        self.orientation=False
        self.curve=False
        self.image=self.images[0]

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

    def set_image(self,img_num):
        self.image=self.images[img_num]

class Point(Track):
    images=[]
    def __init__(self):
        super().__init__()###????????????????????
        self.connections=['','','']
        self.direction=False
        self.hand=0

    def change_point(self):
        if self.direction==True:
            self.direction=False
        elif self.direction==False:
            self.direction=True

    def change_hand(self):
        if self.hand==True:
            self.hand=False
        elif self.hand==False:
            self.hand=True

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