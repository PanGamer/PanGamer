import pygame

pygame.init()

okno = pygame.display.set_mode((620,620))
pygame.display.set_caption("moje okno")
sprite = pygame.image.load("figury.png").convert_alpha()
pionek = pygame.Surface( (210,215), pygame.SRCALPHA,32 ).convert_alpha()
kon = pygame.Surface( (210,215), pygame.SRCALPHA,32 ).convert_alpha()
wieza = pygame.Surface( (210,215), pygame.SRCALPHA,32 ).convert_alpha()
goniec = pygame.Surface( (210,215), pygame.SRCALPHA,32 ).convert_alpha()
hetman = pygame.Surface( (210,215), pygame.SRCALPHA,32 ).convert_alpha()

pionek.blit( sprite, ( 0, 0 ), (0,0,210,215))
pionek = pygame.transform.scale(pionek,(210*0.25,215*0.25))


hetman.blit( sprite, ( 0, 0 ), (1050,0,210,215))
hetman = pygame.transform.scale(hetman,(210*0.25,215*0.25))


wieza.blit( sprite, ( 0, 0 ), (630,0,210,215))
wieza = pygame.transform.scale(   wieza,(210*0.25,215*0.25))





kon.blit( sprite, ( 0, 0 ), (210,0,210,215))
kon = pygame.transform.scale(   kon,(210*0.25,215*0.25))





goniec.blit( sprite, ( 0, 0 ), (420,0,210,215))
goniec = pygame.transform.scale(   goniec,(210*0.25,215*0.25))



while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    tło = pygame.Color('#222222')

    okno.fill( tło )
    board = pygame.Surface((600, 600))
    board.fill((0, 0, 0))
    for x in range(0, 8, 2):
        for y in range(0, 8, 2):
            pygame.draw.rect(board, (255, 255, 255), (x*72, y*72, 72, 72))
            pygame.draw.rect(board, (255, 255, 255), ((x+1)*72, (y+1)*72, 72, 72))
    okno.blit(board, (20, 20))


  

    okno.blit(pionek,(15,90))
    okno.blit(pionek,(90,90))
    okno.blit(pionek,(155,90))
    okno.blit(pionek,(230,90))
    okno.blit(pionek,(305,90))
    okno.blit(pionek,(380,90))
    okno.blit(pionek,(455,90))
    okno.blit(pionek,(525,90))


    okno.blit(hetman,(230,20))

    okno.blit(kon,(90,20))
    okno.blit(kon,(455,20))

    okno.blit(wieza,(525,20))
    okno.blit(wieza,(15,20))

    okno.blit(goniec,(155,20))
    okno.blit(goniec,(380,20))

    pygame.display.update()
