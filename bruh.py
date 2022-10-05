import pygame
import time
pygame.init()
pygame.display.set_caption("data structures")
screen = pygame.display.set_mode((800,800))


frend=("Lukas", "Ricky", "Rey", "Googy", "Simon")

xyz = [(100,100),(300,300),(300,500),(500,300),(700,700)]


borger={"BLT": 6.65,
        "Single":5.95,
        "Double":8.45,
        "Chicken Sandwich":8.20,
        "Grilled Cheese":3.25}

#colores-------------------------

YELLOW = (250,250,0)
RED = (200,0,0)




for i in range(len(xyz)):
    pygame.draw.circle(screen, RED, (xyz[i]),100)
print(YELLOW)
print(YELLOW[1])

print(frend)
print(frend[2])



pygame.display.flip()
time.sleep(100)
pygame.quit()
