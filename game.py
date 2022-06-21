import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Set Caption")

def menu():
    image = pygame.image.load('menu.png')
    image = pygame.transform.scale(image, (640,480))
    while True:
        screen.blit(image, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(300, 325) and event.pos[1] in range(200,228): #add play button at this location on the screen
                    game()
def game():
    image = pygame.image.load('level1.png')
    image = pygame.transform.scale(image, (640,480))
    bgx = 0
    
    player = pygame.image.load('idle.png')
    player = pygame.transform.rotozoom(player, 0,0.2)
    while True:
        screen.blit(image, (bgx - 640,0))
        screen.blit(image, (bgx,0))
        screen.blit(image, (bgx + 640,0))
        
        bgx = bgx -1
        if bgx <= -640:
            bgx = 0
        screen.blit(player, (50,325))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                print('jump')
    
menu()