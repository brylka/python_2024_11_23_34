from time import sleep

import pygame

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Aplikacja pygame")


color = (255,255,255)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            elif event.key == pygame.K_r:
                color = (255,0,0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                #print(mouse_x, mouse_y)
                #screen.set_at((mouse_x, mouse_y), color)
                #pygame.draw.rect(screen,color,(mouse_x-5, mouse_y-5, 10, 10))
                pygame.draw.circle(screen, color, (mouse_x, mouse_y), 5)
    pygame.display.flip()

