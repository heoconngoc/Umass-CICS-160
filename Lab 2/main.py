import pygame
import Vehicle

def main():
    pygame.init()
    canvas      = pygame.display.set_mode((1240, 820))
    car1        = Vehicle.Vehicle("./Images/orange_truck.png")
    tree        = Vehicle.Vehicle("./Images/tree.png")
    keepRunning = True
    while (keepRunning):
        canvas.blit(car1.getImage(),car1.getPosition())
        canvas.blit(tree.getImage(),(canvas.get_width() - tree.getImage().get_width(),0))
        tree.setPosition(canvas.get_width() - tree.getImage().get_width(),0)
        pygame.display.flip()
        pressedKeys =  pygame.key.get_pressed()
        if pressedKeys[pygame.K_d]:
            car1.setPosition(car1.getX() + 1, car1.getY())
            if car1.isCollidingWith(tree):
                print("The car and the tree have collided!!!")
            
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                keepRunning = False


if __name__ == "__main__":
    main()