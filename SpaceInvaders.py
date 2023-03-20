import pygame
from entities import *
import sys
import time


class SpaceInvaders:
    def __init__(self, screen, clock, difficulty=1):
        pygame.init()
        pygame.display.set_caption("Space Invaders")
        self.screen = screen
        self.clock = clock
        
        self.gameState = False
        
        if difficulty == 1:
            self.update_time = 500
        elif difficulty == 2:
            self.update_time = 300
        elif difficulty == 3:
            self.update_time = 100

        self.EnemyTimer = 0
  
        self.allowShoot = True

        self.startTime = time.time()

        # Fixed the Enemy grid initialization
        self.EnemyGrid = [[] for _ in range(5)]

        # Load sprites
        topSprite = pygame.Surface((30, 30))
        topSprite.fill((255, 0, 0))
        middleSprite = pygame.Surface((30, 30))
        middleSprite.fill((0, 255, 0))
        bottomSprite = pygame.Surface((30, 30))
        bottomSprite.fill((0, 0, 255))
        self.playerSprite = pygame.Surface((30, 30))
        self.playerSprite.fill((255, 255, 255))

        # Generate enemies
        for i in range(10):
            self.EnemyGrid[0].append(Enemy(topSprite, (50+i * 50, 0)))
            self.EnemyGrid[1].append(Enemy(middleSprite, (50+i * 50, 50)))
            self.EnemyGrid[2].append(Enemy(middleSprite, (50+i * 50, 100)))
            self.EnemyGrid[3].append(Enemy(bottomSprite, (50+i * 50, 150)))
            self.EnemyGrid[4].append(Enemy(bottomSprite, (50+i * 50, 200)))

        # Generate barriers
        self.barriers = []
        for i in range(4):
            self.barriers.append(Barrier((100 + i * 175, 450)))

        # Generate player
        self.player = Player(self.playerSprite, (400, 550))

    def handle_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.player.move_left()
        if keys[pygame.K_RIGHT]:
            self.player.move_right()
        if keys[pygame.K_SPACE]:
            if self.allowShoot:
                self.player.shoot()
                self.allowShoot = False
                
        if keys[pygame.K_BACKSPACE]:
            self.gameState = True
            return


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Add more input
   

    def update(self):
        # Add game update logic here, e.g. updating Enemy, bullet and player positions, collision detection
        # Update player bullets
        for bullet in self.player.bullets:
            bullet.update()
   
        # Update enemies every 0.5 seconds
        self.EnemyTimer += self.clock.get_time()
        if self.EnemyTimer >= self.update_time:
            self.allowShoot = True
            self.EnemyTimer = 0
            for row in self.EnemyGrid:
                for Enemy in row:
                    Enemy.update()
     
        for row in self.EnemyGrid:
            for Enemy in row:
                for bullet in Enemy.bullets:
                    bullet.update()
                    #player collision
                    if self.player.sprite.get_rect(topleft=self.player.position).colliderect(bullet.sprite.get_rect(topleft=bullet.position)):
                        self.gameState = True
                        print("You lose!")
                        return
                    
                    #barrier collision
                    if len(self.barriers) > 0:
                        for barrier in self.barriers:
                            if barrier.sprite.get_rect(topleft=barrier.position).colliderect(bullet.sprite.get_rect(topleft=bullet.position)):
                                self.barriers.remove(barrier)
                                Enemy.bullets.remove(bullet)
                                break
                
                
                for bullet in self.player.bullets:
                    if Enemy.sprite.get_rect(topleft=Enemy.position).colliderect(bullet.sprite.get_rect(topleft=bullet.position)):
                        row.remove(Enemy)
                        self.player.bullets.remove(bullet)
                        break
                    
        #check win condition
        if len(self.EnemyGrid[0]) == 0 and len(self.EnemyGrid[1]) == 0 and len(self.EnemyGrid[2]) == 0 and len(self.EnemyGrid[3]) == 0 and len(self.EnemyGrid[4]) == 0:
            self.gameState = True
            return self.startTime-time.time()
            
            
    def render(self):
        self.screen.fill((0, 0, 0))

        # Draw enemies
        for row in self.EnemyGrid:
            for Enemy in row:
                self.screen.blit(Enemy.sprite, Enemy.position)
                
        for row in self.EnemyGrid:
            for Enemy in row:
                for bullet in Enemy.bullets:
                    self.screen.blit(bullet.sprite, bullet.position)

        # Draw barriers
        # Assuming Barrier class has a sprite attribute
        for barrier in self.barriers:
            self.screen.blit(barrier.sprite, barrier.position)

        # Draw player
        self.screen.blit(self.player.sprite, self.player.position)
  
        # Draw player bullets
        for bullet in self.player.bullets:
            self.screen.blit(bullet.sprite, bullet.position)

        pygame.display.flip()

    def run(self):
        while True:
            self.handle_input()
            self.update()
            self.render()
            self.clock.tick(60)
            
            if self.gameState == True:
                return self.startTime
            
if __name__ == "__main__":
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 600))
    SpaceInvaders(screen,clock).run()