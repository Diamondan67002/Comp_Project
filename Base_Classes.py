import pygame, os

class Track(pygame.sprite.Sprite):
    images=["Track-Straight.png","Track-Curved.png","Track-Diagonal.png"]
    colourKey=(255,255,255)
    curved_track_rotations = [[False,False,0],### The  Rotation and reflections to get from the identity curved track image to the one
                              [False,True,90],### with a angle of 45 degrees to 180 as over 180 is the same but rotated 180 degrees to
                              [False,False,90],### start with.
                              [True,False,0]]

    def __init__(self,coords,img,initConnect):### Image loading could be made bettter by preloading all the png's into python rather than loading 1 everytime an object is created or image altered
        print("Track Commenced")
        pygame.sprite.Sprite.__init__(self)### Initiates the Sprite class
        self.image = pygame.image.load(os.path.join('photos',self.images[img]))### Sets the Image for the Track
        self.image.convert_alpha()
        self.image.set_colorkey(self.colourKey)###????????
        self.rect = self.image.get_rect()
        self.set_coords(coords)
        self.imgNum = img

        self.connections = [-1,-1]
        self.vehicle = ''
        self.orientation = 0
        self.curve = 0
        self.set_connection(initConnect[0],initConnect[1],initConnect[2])

    def set_connection(self,direction,lineNum,posNum):### Could change to rationalise it and all the remove connection functions
        self.connections[direction] = [lineNum,posNum]

    def get_connection(self):### Don't really need
        return self.connections

    def get_connection(self,direction):### Duplicated to allow for 2 different sets of arguments.
        return self.connections[direction]

    def remove_connection(self):### Also duplicated to allow for difffernt arguments. Might actually be used.
        self.connections=[-1,-1]

    def remove_connection(self,direction):
        self.connections[direction] = -1

    def get_connection_direction(self,connection):
        connections = self.get_connection()
        for i in range(len(connections)):
            if connections[i][0] == connection[0] and connections[i][1] == connection[1]:
                return i

    def add_vehicle(self,vehicle):
        self.vehicle = vehicle

    def remove_vehicle(self):
        self.vehicle = ''

    def check_vehicle(self):
        return self.vehicle

    #def change_orientation(self):### Using a number to represent true false given it is really neat and clean to change
    #    self.orientation = 1-self.orientation### Not 100% sure what I was using orientation for before.

    def change_curve(self):
        self.curve = 1-self.curve

    def set_image(self,img):### Integrated into constructor. But allows changing of images
        self.image = pygame.image.load(os.path.join('photos',self.images[img]))## Need to resolve alterations of image.
        self.imgNum = img

    def get_image(self):
        return self.image

    def get_image_num(self):
        return self.imgNum

    def rotate_image(self,angle):
        pygame.transform.rotate(self.image,angle)

    def reflect_image(self,x_bool,y_bool):
        pygame.transform.flip(self.image,x_bool,y_bool)

    def track_image_rotator(self,direction):
        self.orientation = (self.orientation + direction * 45) % 360
        if self.orientation < 0:### Shouldn't need.
            self.orientation = self.orientation + 360
        if self.get_image_num() == 0:
            self.set_image(2)
            self.rotate_image(self.orientation-45)
        elif self.get_image_num() == 2:
            self.set_image(0)
            self.rotate_image(self.orientation)
        elif self.get_image_num() == 1:
            orientation = self.orientation
            self.set_image(1)### reseting the image to make sure we have the original quality image.
            if self.orientation > 180:### Hopefully the mod function works for keeping the orientation value below 360 deg
                self.rotate_image(180)### Could change to reflect in both x & y which would give a better quality image due to non-desctructivity.
                orientation = orientation - 180
            index = orientation / 45
            self.reflect_image(self.curved_track_rotations[index][0],self.curved_track_rotations[index][1])
            self.rotate_image(self.curved_track_rotations[index][2])


    def get_coords(self):
        return self.coords

    def set_coords(self,coords):
        self.coords = coords### Don't really need but means I don't have to manipulate the values of self.rect.cx and self.rect.y
        self.rect.x = coords[0]*32
        self.rect.y = coords[1]*32

    def move_track_point(self,coords,connections):### Duplicated again for whether we know the new connections
        self.set_coords(coords)
        self.remove_connection()### Added in case less new connections than old ones
        for i in range(len(connections)):
            self.add_connection(connections[i][0],connections[i][1],connections[i][2])

    def move_track_point(self,coords):
        self.set_coords(coords)
        self.remove_connection()### Added to delete all of the connections. Not 100% sure if it is a point if it will call the corrrect function

class Point(Track):
    images=["Point-straight.png","Point-diagonal.png"]
    def __init__(self,coords,img,initConnect):
        print("Point Commenced")
        pygame.sprite.Sprite.__init__(self)### Same as track
        self.image = pygame.image.load(os.path.join('photos',self.images[img]))
        self.image.convert_alpha()
        self.image.set_colorkey(self.colourKey)  ###????????
        self.rect = self.image.get_rect()
        self.rect.x = coords[0]*32
        self.rect.y = coords[1]*32
        self.imgNum = img

        ###???????????????????? You need to call the parent constructor (Track.__init__()  ) explicitly IF you wish to use it....
        self.coords=coords
        self.connections = [-1,-1,-1]
        self.vehicle = ''
        self.pointBlade = PointBlade(coords,self.colourKey)### Creating the point Blade to be put over the point
        self.hand = 0
        self.add_connection(initConnect[0],initConnect[1],initConnect[2])

    def change_hand(self):
        self.hand = 1-self.hand

    def remove_connection(self):
        self.connections = [-1,-1,-1]

class PointBlade(pygame.sprite.Sprite):### Need to add pygame.sprite.Sprite to the inheritance
    images=["PointBlade-Straight.png","PointBlade-diagonal.png","PointBlade-Curved.png"]### Might need to rebuild as a 2d list.
    def __init__(self,coords,colourkey):
        self.colourkey=colourkey
        pygame.sprite.Sprite.__init__(self)### Similar to before
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
        self.set_connection(initConnect[0],[initConnect[1],initConnect[2]])
        self.buildSiding(imgNums,self.coords,initConnect)

    def add_track(self,initConnect):### Appends a track object to the end of the list
        self.track.append(Track([self.coords[0],self.coords[1]+self.length],0,initConnect))
        self.length=self.length+1

    def pre_add_track(self,initConnect):### Adds a track at the start of the list
        self.coords[1]=self.coords[1]-1
        self.track.insert(0,Track(self.coords,0,initConnect))
        self.length=self.length+1

    def remove_track(self,sidingPos):### Removes a track but need to write the algoritmn that goes and reconfigure both the connections and all the coordinates.
        self.track[sidingPos] = -1 ### There is quite a few possibilities there though.

    def buildSiding(self,imgNums,coords,initConnect):### Ran upon initiation
        for i in range(self.length):
            if i>0:
                initConnect[2]=initConnect[2]+1### Need to get it to go back thoug and add all the connections the other way as well.
            self.track.append(Track(coords,imgNums[i],initConnect))### Need to set up all the alignments of x and y coords coming down from the initial map function.
            coords[1]=coords[1]+1

    def set_connection(self,direction,connection):
        self.connections[direction] = connection

    def get_connection(self):### Don't really need
        return self.connections

    def get_connection(self,direction):
        return self.connections[direction]

    def get_connection_direction(self,connection):
        connections = self.get_connection()
        for i in range(len(connections)):
            if connections[i][0] == connection[0] and connections[i][1] == connection[1]:
                return i

    def get_track_connection(self,sidingPos):### Again duplication for different arguments
        return self.track[sidingPos].get_connections()

    def get_track_connection(self,direction,sidingPos):
        return self.track[sidingPos].get_connection(direction)

    def check_length(self):
        return self.length

    def get_vehicle(self,sidingPos):
        return self.track[sidingPos].check_vehicle()

    def remove_vehicle(self,sidingPos):
        self.track[sidingPos].remove_vehicle()

    def get_track(self,sidingPos):
        return self.track[sidingPos]

    def pop_track(self,sidingPos):
        return self.track.pop(sidingPos)

    def set_track_coords(self,coords,sidingPos):
        self.track[sidingPos].set_coords(coords)

    def reconfigure_conections_pop(self,sidingPos):
        print("Hi")

    def delete_connection(self,sidingPos,connection):
        if 0 < sidingPos < self.check_length() - 1:### Need this for all of them.
            direction = self.track[sidingPos].get_connection_direction(connection)
            self.track[sidingPos].remove_connection(direction)
        elif sidingPos == 0:
            self.set_connection(0,-1)
            direction = self.track[sidingPos].get_connection_direction(connection)
            self.track[sidingPos].remove_connection(direction)
        elif sidingPos == self.check_length() - 1:
            self.set_connection(1,-1)
            direction = self.track[sidingPos].get_connection_direction(connection)
            self.track[sidingPos].remove_connection(direction)

class DeadEndSiding(Siding):### Don't think it will every actually be used.
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
            if setup[i][0]==-1:### If it has a value of -1 then it should be a Point()
                self.line.append(Point(coords,setup[i][1],[0,connections[0],connections[1]]))#### Need to continue passing though the GUI coords.
                coords[0]=coords[0]+1
                connections[1]=connections[1]+1
            elif setup[i][0]>=1:### Is a Siding of length setup[i][0]
                self.line.append(Siding(setup[i][0],coords,setup[i][1],[0,connections[0],connections[1]]))### Issues. Coords and connections are effectively duplicates that should be in tegrated together.
                coords[0]=coords[0]+setup[i][0]
                connections[1]=connections[1]+setup[i][0]

    def get_component_no(self,x_coord):### Can we chack what type of object an item in a list is??
        x = 0 ### This converts a normal x_coord into a linePos and sidingPos where if it is a Point sidingPos = False
        linePos = 0
        running = True
        point = False
        sidingPos = False
        while running:### Goes and iterates though until the x reaches or is greater than x_coord
            if len(self.line[x].get_connections()) == 3:### Had these 2 the wrong way around
                x +=1
            elif len(self.line[x].get_connections()) == 2:
                x = x + self.line[x].check_length()

            linePos += 1
            if x > x_coord:
                sidingPos = x_coord - x
                running = False
            elif x == x_coord:
                running = False
                point = True

            if linePos > len(self.line):
                running = False
                sidingPos = False

        if point == True:
            return linePos, False
        return linePos, sidingPos

    def get_vehicle(self,x_coord):## meed to re configure for when vehichle is empty. Maybe use False and then check for that before passing it back up the chain??
        linePos, sidingPos = self.get_component_no(x_coord)
        if sidingPos == False:
            return self.line[linePos].check_vehicle()
        return self.line[linePos].get_vehicle(sidingPos)

    def remove_vehicle(self,x_coord):### Removes a vehicle at a certain x_coord
        linePos, sidingPos = self.get_component_no(x_coord)
        if sidingPos == False:
            self.line[linePos].remove_vehicle()
        else:
            self.line[linePos].remove_vehicle(sidingPos)

    def move_vehicle(self,x_coord,direction):### Moves a vehicle 1 space
        wagon = self.get_vehicle(x_coord)
        self.remove_vehicle(x_coord)
        new_location = self.get_connection(x_coord,direction)
        return wagon, new_location

    def get_connection(self,x_coord,direction):### Gets a connection for a Track()/Point()
        linePos, sidingPos = self.get_component_no(x_coord)#### Should I move these calls into the previous method as move_vehicle() is calling it a lot of times.
        if sidingPos == False:
            return self.line[linePos].get_connection(direction)
        return self.line[linePos].get_track_connection(direction,sidingPos)

    def get_track_point(self,x_coord):### Returns a Track/Point object to be moved
        linePos, sidingPos = self.get_component_no(x_coord)
        if sidingPos == False:
            return self.line[linePos]
        return self.line[linePos].get_track(sidingPos)

    def pop_track_point(self,x_coord):
        linePos, sidingPos = self.get_component_no(x_coord)
        if sidingPos == False:
            return self.line.pop(linePos)
        return self.line[linePos].pop_track(sidingPos)

    def remove_track_point(self,x_coord):### Need to sort out the connections and chnaging/deleting them.
        linePos, sidingPos = self.get_component_no(x_coord)
        if sidingPos == False:
            self.line[linePos] = -1 ### Removes it but doesn;t delete the space it was in
        else:
            self.line[linePos].remove_track(sidingPos)

    def set_track_point_coords(self,coords):### Sets a Track()/Point()'s internal coords
        linePos, sidingPos = self.get_component_no(coords[1])
        if sidingPos == False:
            self.line[linePos].set_coords(coords)
        else:
            self.line[linePos].set_track_coords(coords,sidingPos)

    def place_track_point(self,coords,component,check):
        linePos, sidingPos = self.get_component_no(coords[1])
        if sidingPos == False:
            print("Hi")

    def check_track_point(self,x_coord):
        linePos, sidingPos = self.get_component_no(x_coord)
        if linePos > len(self.line):
            print("This position doesn't currently exist in the map")
            return False
        return True

    def reconfigure_connections(self,x_coord):### reconfigures connections for popped objects was the intention
        print("Hi")

    def delete_conection(self,x_coord,coords_connection):### Deletes a connection of a component that has been removed.
        linePos, sidingPos = self.get_component_no(x_coord)
        if sidingPos == False:
            direction = self.line[linePos].get_connection_direction(coords_connection)
            self.line[linePos].remove_connection(direction)
        else:
            self.line[linePos].delete_connection(sidingPos,coords_connection)