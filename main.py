import pygame
from constants import *
# from circleshape import CircleShape
from player import Player
from asteroid import Asteroid, Shot
from asteroidfield import AsteroidField


def main():
    print("Starting Asteroids!")
    # Set the screen size
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    
    clock = pygame.time.Clock()
    dt = 0   

    # Set the background color
    # background_color = (0, 0, 0)
    background_color = "black"
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    
    # Instantiate the player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # Instantiate the asteroid field
    asteroid_field = AsteroidField()

    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(background_color)
        updatable.update(dt)
        # Check for collisions
        for asteroid in asteroids:
            if player.collide(asteroid):
                print("Game over!")
                running = False
            for shot in shots:
                if shot.collide(asteroid):
                    print("Shot hit asteroid!")
                    # Remove the asteroid and shot from their respective groups
                    asteroid.split()
                    shot.kill()
                    # break
        # Draw the game objects
        for drawing in drawable:
            drawing.draw(screen)
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
    # Quit the game
    pygame.quit()




if __name__ == "__main__":
    main()
