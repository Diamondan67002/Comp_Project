import pygame


class GUI():
    def __init__(self):
        pygame.init()

        screen = pygame.display.set_mode([500, 500])

        width=screen.get_width()
        height=screen.get_height()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                        pygame.quit()

            mouse=pygame.mouse.get_pos()
            screen.fill((255, 255, 255))
            pygame.display.flip()

        pygame.quit()

    def load_Map(self):
        print("Hi")

GUI()
