import pygame

class Track():
    images=[]
    def __init__(self,type_num):
        self.connections=['','']
        self.vehicle=''
        self.image=self.images[type_num]

    def add_connection(self,direction,object,object_end):
        self.connections[direction]=[object,object_end]

    def add_vehicle(self,vehicle):
        self.vehicle=vehicle

    def remove_vehicle(self):
        self.vehicle=''

    def check_vehicle(self):
        return self.vehicle

class Point(Track):
    images=[]
    def __init__(self,type_num,hand_type):
        super().__init__()###????????????????????
        self.connections=['','','']
        self.direction=False
        self.hand=hand_type

    def change_point(self):
        if self.direction==True:
            self.directions=False
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