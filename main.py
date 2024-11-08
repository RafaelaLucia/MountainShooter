import pygame

print('Setup começou')
pygame.init()
window = pygame.display.set_mode(size = (600,480))
print('Setup terminou')

print('Loop começou')
while True:
   # Verifica todos os eventos
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit() #fecha janela
           quit() #termina pygame

