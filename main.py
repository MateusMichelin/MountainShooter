import pygame

pygame.init()

print("Setup Start")
window = pygame.display.set_mode(size = (600, 480))

print("Loop Start")
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Quiting...')
            pygame.quit()# Close Window
            quit() # End pygame






