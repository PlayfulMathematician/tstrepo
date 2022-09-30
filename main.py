import pygame
from pygame.locals import *
import pygame.image as image
pygame.init()

# Set up the drawing window


class Entity:
    def __init__(self, x, y, img_ls, **kwargs):
        self.x = x
        self.y = y
        self.xv = 0
        self.yv = 0
        self.img_ls = list(map(lambda img: pygame.transform.scale(image.load(img), kwargs.get("imgsize", (1, 1))), \
                               img_ls))
        self.max_xv = kwargs.get("max_xv", 1)

    def render(self):
        g.screen.blit(self.img_ls[0], dest=(self.x, self.y))


class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, ["pixil-frame-0 (1).png"], imgsize=(50, ) * 2, max_xv=5)

    def handle(self):
        self.xv *= 0.99
        if self.xv > self.max_xv:
            self.xv = self.max_xv
        if self.xv < -self.max_xv:
            self.xv = -self.max_xv
        if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]:
            self.x += self.xv
            self.xv -= 0.1
            return

        if pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]:
            self.x += self.xv
            self.xv += 0.1


class Game:
    def __init__(self, w, h, title):
        self.screen = pygame.display.set_mode([w, h])
        pygame.display.set_caption(title, title)
        pygame.display.set_icon(pygame.image.load("pixil-frame-0.png"))
        self.player = Player(500, 500)

    def game_loop(self):
        running = True
        while running:

            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.player.handle()
            self.screen.fill((255, 255, 255))
            self.player.render()
            pygame.display.update()

        # Done! Time to quit.
        pygame.quit()


g = Game(1000, 1000, "Hi")
g.game_loop()