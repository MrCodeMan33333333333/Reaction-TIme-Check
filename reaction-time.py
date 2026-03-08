import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 900, 550
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reaction Speed Test")

font_big = pygame.font.SysFont("Arial", 60)
font_mid = pygame.font.SysFont("Arial", 35)
font_small = pygame.font.SysFont("Arial", 25)

clock = pygame.time.Clock()

state = "start"
green = False
start_time = 0
reaction_time = 0

delay = random.randint(2,5)
start_ticks = 0

def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img,(x,y))

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if state == "start":
                if event.key == pygame.K_SPACE:
                    state = "wait"
                    start_ticks = time.time()

            elif state == "go":
                if event.key == pygame.K_SPACE:
                    reaction_time = int((time.time()-start_time)*1000)
                    state = "result"

            elif state == "result":
                if event.key == pygame.K_r:
                    state = "start"
                    delay = random.randint(2,5)
                    green = False

    # ---------- STATES ----------

    if state == "start":

        screen.fill((20,20,40))
        draw_text("Reaction Speed Test", font_big,(0,255,255),240,120)
        draw_text("Press SPACE to Start", font_mid,(255,255,255),310,260)
        draw_text("Press SPACE when screen turns GREEN", font_small,(180,180,180),270,320)

    elif state == "wait":

        screen.fill((200,40,40))
        draw_text("WAIT...", font_big,(255,255,255),350,220)

        if time.time()-start_ticks > delay:
            state = "go"
            start_time = time.time()

    elif state == "go":

        screen.fill((40,200,80))
        draw_text("PRESS SPACE!", font_big,(255,255,255),280,220)

    elif state == "result":

        screen.fill((20,20,40))
        draw_text("Your Reaction Time", font_mid,(255,255,255),310,160)
        draw_text(str(reaction_time)+" ms", font_big,(0,255,255),350,240)
        draw_text("Press R to Restart", font_small,(200,200,200),350,340)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
