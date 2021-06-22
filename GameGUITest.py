import pygame
import Base_Classes

class Game():
    sprites = pygame.sprite.Group()

    positions = [[0, 470, 100, 30],### Positions of all the buttons/rectangles
                 [100, 470, 100, 30],
                 [200, 470, 100, 30],
                 [300, 470, 100, 30],
                 [400, 470, 100, 30],
                 [0, 0, 32, 32]]  ### Need to move to be resizable possibly.

    def __init__(self):
        self.map = Map()

    def build_GUI(self):
        pygame.init()

        screen = pygame.display.set_mode([500, 500])

        color = (255, 255, 255)# #####GforG
        color_light = (170, 170, 170)
        color_dark = (100, 100, 100)
        width = screen.get_width()
        height = screen.get_height()
        smallfont = pygame.font.SysFont('Corbel', 25)
        text = [smallfont.render('Track',True,color),smallfont.render('Point',True,color),smallfont.render('Quit',True,color),smallfont.render('Inglenook',True,color),smallfont.render('Wagon Creation',True,color),False]### Text for all the buttons
        colors = [0,0,0,0,0,1]### Probably going to need to make self for all of these lists and move them out of the functions
        color_pairs = [[color_light,color_dark],### paired colors for the variations if it is being hovered over.
                       [(220,200,0),(255,255,0)]]

        running = True
        while running:
            mouse = pygame.mouse.get_pos()  ###GforG the correct places.

            for event in pygame.event.get():### Checks for all events that have happened
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:  ###GforG ### CHecks for presses of the GUI buttons
                    if self.positions[0][0] <= mouse[0] <= self.positions[0][0] + self.positions[0][2] and self.positions[0][1] <= mouse[1] <= self.positions[0][1] + self.positions[0][3]:
                        self.map.add_track([self.positions[5][0] / 32, self.positions[5][1] / 32])
                    elif self.positions[1][0] <= mouse[0] <= self.positions[1][0] + self.positions[1][2] and self.positions[1][1] <= mouse[1] <= self.positions[1][1] + self.positions[1][3]:
                        self.map.add_point([self.positions[5][0] / 32, self.positions[5][1] / 32])
                    elif self.positions[2][0] <= mouse[0] <= self.positions[2][0] + self.positions[2][2] and self.positions[2][1] <= mouse[1] <= self.positions[2][1] + self.positions[2][3]:
                        running = False
                    elif self.positions[3][0] <= mouse[0] <= self.positions[3][0] + self.positions[3][2] and self.positions[3][1] <= mouse[1] <= self.positions[3][1] + self.positions[3][3]:
                        self.map.build_inglenook()
                    elif self.positions[4][0] <= mouse[0] <= self.positions[4][0] + self.positions[4][2] and self.positions[4][1] <= mouse[1] <= self.positions[4][1] + self.positions[4][3]:
                        self.create_wagons()
                elif event.type == pygame.KEYDOWN:### Checks though all the key operations
                    if event.key == pygame.K_KP8:
                        self.move_mover_y(-1)
                    elif event.key == pygame.K_KP2:
                        self.move_mover_y(1)
                    elif event.key == pygame.K_KP4:
                        self.move_mover_x(-1)
                    elif event.key == pygame.K_KP6:
                        self.move_mover_x(1)
                    elif event.key == pygame.K_UP:
                        self.move_selector_y(-32)
                    elif event.key == pygame.K_DOWN:
                        self.move_selector_y(32)
                    elif event.key == pygame.K_LEFT:
                        self.move_selector_x(-32)
                    elif event.key == pygame.K_RIGHT:
                        self.move_selector_x(32)
                    elif event.key == pygame.K_p:
                        self.place_pickup_component()
                    elif event.key == pygame.K_e:
                        self.rotate_component(-1)
                    elif event.key == pygame.K_q:
                        self.rotate_component(1)

            screen.fill((255, 255, 255))


            for i in range(len(self.positions)):### Changes the rectangle colors if the mouse is hovered over them.
                if self.positions[i][0] <= mouse[0] <= self.positions[i][0] + self.positions[i][2] and self.positions[i][1] <= mouse[1] <= self.positions[i][1] + self.positions[i][3]: ### Altered from GforG
                    pygame.draw.rect(screen, color_pairs[colors[i]][0], [self.positions[i][0],self.positions[i][1],self.positions[i][2],self.positions[i][3]])
                else:
                    pygame.draw.rect(screen, color_pairs[colors[i]][1], [self.positions[i][0],self.positions[i][1],self.positions[i][2],self.positions[i][3]])
                if text[i] != False:
                    screen.blit(text[i], (self.positions[i][0] + 20, self.positions[i][1]+5))

            sprites = self.map.update_map()
            sprites.update()## Code needed to get the Group of sprites to update. ### Don't need now as map updates the sprites and then returns them.
            sprites.draw(screen)

            pygame.display.flip()

        pygame.quit()

    def move_selector_x(self,direction):### Need to make sure it doesn't go off the edges of the screen. Fixed
        if 0 <= self.positions[5][0] + direction <= 500:### Moves the selector in the x direction
            self.positions[5][0]=self.positions[5][0] + direction

    def move_selector_y(self,direction):### Moves the selector in the y direction
        if 0 <= self.positions[5][1] + direction <= 500:
            self.positions[5][1] = self.positions[5][1] + direction

    def move_mover_x(self,direction):### Moves the mover and slector and therefore a component where the selector is in the x direction
        coords = [self.positions[5][0]/32,self.positions[5][1]/32]
        self.map.move_component_x(coords)
        self.move_selector_x(direction*32)### Converting position movement into Pixels.

    def move_mover_y(self,direction):### Moves the mover and selector and therefore a component where the selector is in the y direction
        coords = [self.positions[5][0] / 32, self.positions[5][1] / 32]### Maybe make coords the new coords?? ### Could make self.coords and refresh every GUI cycle.
        self.map.move_component_y(coords)
        self.move_selector_y(direction*32)

    def place_pickup_component(self):
        self.map.place_pickup_component([int(self.positions[5][0] / 32), int(self.positions[5][1] / 32)])### Shouldn't need int's

    def rotate_component(self,direction):
        coords = [int(self.positions[5][0] / 32), int(self.positions[5][1] / 32)]
        self.map.rotate_componnent(direction,coords)

    def create_wagons(self):
        wagon_no = int(input("How many wagons do you want??"))
        self.map.create_wagons(wagon_no)

class Map():
    map = []
    component = -1
    sprites = pygame.sprite.Group()
    wagons = []
    siding_tracks = []
    def __init__(self):
        print('Hi')

    def add_track(self,coords):
        if self.component == -1:
            track = Base_Classes.Track([0,0],0)
            self.add_sprite(track)
            self.component = track
            self.place_component(coords)

    def add_point(self,coords):
        if self.component == -1:### Tbh It probably doesn't matter if you were to delete a component. They are easy to make.
            point = Base_Classes.Point([0,0],0)
            self.add_sprite(point)
            self.component = point
            self.place_component(coords)
        print('Hi')

    def build_inglenook(self):
        startCoords = [0,0]
        setup = [[[3,[0,0,0]],[-1,0],[5,[0,0,0,0,0]]],### Each row is a Line()
                 [[-1,1],[3,[0,0,0]]],### Each item in a row is a Siding() or Point()
                 [[3,[1,0,0]]]]### Each of these then have a list or number which shows the images used from left to right
        connections = [[0,0,-1],
                       [0,0,3],
                       [0,1,0]]
        for i in range(3):### Creates each Line()
            self.map.append(Base_Classes.Line(setup[i],[0,startCoords[1]+i],connections[i]))##need to configure the y coords and the orientations
        ### set back connections between lines.
        #self.set_back_connection(connections)
        self.map[0].set_track_connection(3,[2,1,0])
        self.map[1].set_track_connection(0,[1,2,0])

        self.get_sprites()

        ### Need to get all the connections going back down the map.

    def set_back_connection(self,connections):
        for i in range(len(connections)):
            if connections[i][1] != -1 and connections[i][2] != -1:
                print("Hi")
                ### Not quite sure what I was doing.

    def move_component_x(self,coords):## Would have a issue if we  had the start cooords of 0,0
        print("Hi")

    def move_component_y(self,coords):### Will have issues if there is already a component at a certain position
        print("Hi")

    def place_pickup_component(self,coords):
        if self.component == -1:
            self.pickup_component(coords)
        else:
            self.place_component(coords)

    def pickup_component(self,coords):
        self.component = self.map[coords[1]].get_track_point(coords[0])
        self.map[coords[1]].remove_track_point(coords[0])
        self.reconfigure_connections(self.component.get_connection(),coords)

    def place_component(self,coords):
        check = self.map[coords[1]].check_track_point(coords[0])
        self.map[coords[1]].place_track_point(coords,self.component,check)
        ### need to put in some form of make connections function.

    def rotate_componnent(self,direction,coords):
        print(coords)
        self.map[coords[1]].rotate_component(coords[0],direction)

    def reconfigure_connections(self,connections,coords):### Not complete yet
        for i in range(len(connections)):
            self.map[coords[1]].delete_connection(connections[i][0],coords)

    def update_map(self):### Moved all the dealing with the sprite group into Map as it actually has the map of sprites
        self.sprites.update()
        return self.sprites

    def add_sprite(self,sprite):### Probably don't need.
        self.sprites.add(sprite)

    def add_list_sprites(self,sprites):### Adds all the objects in a list to a group
        for i in range(len(sprites)):
            self.add_sprite(sprites[i])

    def get_sprites(self):### Gets the sprites already in a map. Useful for loading maps like building the inglenook.
        for i in range(len(self.map)):
            sprite_list = self.map[i].get_sprites()
            self.add_list_sprites(sprite_list)

    def create_wagons(self,wagon_no):
        for i in range(wagon_no):
            current_wagon = Base_Classes.Wagon(str(i))
            self.wagons.append(current_wagon)
        self.add_list_sprites(self.wagons)

    ### Solving algorithmn in here.

game = Game()
game.build_GUI()
