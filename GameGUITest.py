import pygame
import Base_Classes

class Game():
    sprites = pygame.sprite.Group()
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
        text = [smallfont.render('Track',True,color),smallfont.render('Point',True,color),smallfont.render('Quit',True,color),smallfont.render('Inglenook',True,color)]
        positions = [[0,470,100,30],
                     [100,470,100,30],
                     [200,470,100,30],
                     [300,470,100,30]]### Need to move to be resizable possibly.

        running = True
        while running:
            mouse = pygame.mouse.get_pos()  ###GforG the correct places.

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:  ###GforG
                    if positions[0][0] <= mouse[0] <= positions[0][0] + positions[0][2] and positions[0][1] <= mouse[1] <= positions[0][1] + positions[0][3]:
                        self.sprites.add(self.map.add_track())
                    elif positions[1][0] <= mouse[0] <= positions[1][0] + positions[1][2] and positions[1][1] <= mouse[1] <= positions[1][1] + positions[1][3]:
                        self.map.add_point()
                    elif positions[2][0] <= mouse[0] <= positions[2][0] + positions[2][2] and positions[2][1] <= mouse[1] <= positions[2][1] + positions[2][3]:
                        running = False
                    elif positions[3][0] <= mouse[0] <= positions[3][0] + positions[3][2] and positions[3][1] <= mouse[1] <= positions[3][1] + positions[3][3]:
                        self.add_list_sprites(self.map.build_inglenook())### This was my idea bit.

            screen.fill((255, 255, 255))


            for i in range(len(positions)):
                if positions[i][0] <= mouse[0] <= positions[i][0] + positions[i][2] and positions[i][1] <= mouse[1] <= positions[i][1] + positions[i][3]: ### Altered from GforG
                    pygame.draw.rect(screen, color_light, [positions[i][0],positions[i][1],positions[i][2],positions[i][3]])
                else:
                    pygame.draw.rect(screen, color_dark, [positions[i][0],positions[i][1],positions[i][2],positions[i][3]])
                screen.blit(text[i], (positions[i][0] + 20, positions[i][1]+5))

            self.sprites.update()## Code need to get the Group of sprites to update.
            self.sprites.draw(screen)

            pygame.display.flip()

        pygame.quit()

    def add_sprite(self,sprite):### Probably don't need.
        self.sprites.add(sprite)

    def add_list_sprites(self,sprites):
        for i in range(len(sprites)):
            self.add_sprite(sprites[i])

class Map():
    map = []
    def __init__(self):
        print('Hi')

    def add_track(self):### need to change to add to map
        print('Hi')
        track=Base_Classes.Track([0,0],0,[0,-1,-1])
        return track

    def add_point(self):
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

game = Game()
game.build_GUI()
