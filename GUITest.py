import pygame


class GUI():
    def __init__(self):
        pygame.init()

        screen = pygame.display.set_mode([500, 500])

        color = (255,255,255)######GforG
        color_light = (170,170,170)
        color_dark = (100,100,100)
        width=screen.get_width()
        height=screen.get_height()
        smallfont = pygame.font.SysFont('Corbel',35)
        text = smallfont.render('quit',True,color)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:###GforG
                    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                        running = False

            mouse=pygame.mouse.get_pos()
            screen.fill((255, 255, 255))
            if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:###GforG
                pygame.draw.rect(screen, color_light, [width / 2, height / 2, 140, 40])
            else:
                pygame.draw.rect(screen, color_dark, [width / 2, height / 2, 140, 40])
            screen.blit(text, (width / 2 + 50, height / 2))

            pygame.display.flip()

        pygame.quit()

    def load_Map(self):
        print("Hi")

GUI()
