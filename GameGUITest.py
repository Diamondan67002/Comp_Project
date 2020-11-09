import pygame
import Base_Classes

class Game():
    def __init__(self):
        self.map=Map()

    def build_GUI(self):
        pygame.init()

        screen = pygame.display.set_mode([500, 500])

        color = (255, 255, 255)  ######GforG
        color_light = (170, 170, 170)
        color_dark = (100, 100, 100)
        width = screen.get_width()
        height = screen.get_height()
        smallfont = pygame.font.SysFont('Corbel', 25)
        text = [smallfont.render('Track',True,color),smallfont.render('Point',True,color),smallfont.render('Quit',True,color)]
        positions = [[0,470],
                     [100,470],
                     [200,470]]### Need to move to be resizable possibly.

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:  ###GforG
                    if positions[0][0] <= mouse[0] <= positions[0][0] + 100 and positions[0][1] <= mouse[1] <= positions[0][1] + 30:
                        print("Hi")## self.map.add_Track
                    elif positions[1][0] <= mouse[0] <= positions[1][0] + 100 and positions[1][1] <= mouse[1] <= positions[1][1] + 30:
                        print("Hi")## self.map.add_point
                    elif positions[2][0] <= mouse[0] <= positions[2][0] + 100 and positions[2][1] <= mouse[1] <= positions[2][1] + 30:
                        running = False

            screen.fill((255, 255, 255))

            mouse = pygame.mouse.get_pos()  ###GforG the correct places.
            for i in range(3):
                if positions[i][0] <= mouse[0] <= positions[i][0] + 100 and positions[i][1] <= mouse[1] <= positions[i][1] + 30: ### Altered from GforG
                    pygame.draw.rect(screen, color_light, [positions[i][0],positions[i][1], 100, 30])
                else:
                    pygame.draw.rect(screen, color_dark, [positions[i][0],positions[i][1], 100, 30])
                screen.blit(text[i], (positions[i][0] + 20, positions[i][1]+5))

            pygame.display.flip()

        pygame.quit()

class Map():
    def __init__(self):
        print('Hi')

game=Game()
game.build_GUI()