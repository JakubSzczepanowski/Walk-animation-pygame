import pygame
pygame.init()

width,height = 1028,769

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Walk')
FPS = 24
clock = pygame.time.Clock()
ground = pygame.image.load('ground.png')
forward,backward = [],[]
for i in range(8):
    forward.append(pygame.image.load(f'sheet/sprite_{i}.png'))
    backward.append(pygame.image.load(f'sheet/sprite_{i+8}.png'))

f_index,b_index = 0,0

class Hero:
    def __init__(self,x,y,v,s):
        self.x = x
        self.y = y
        self.v = v
        self.s = s
        self.jump = False
        self.turn = 'r'
        self.width = 108
        self.height = 140

class Blast:
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.v = 8 * facing

    def draw(self,screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)

player = Hero(20,395,0,10)
bullets = []
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.blit(ground,(0,0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] != 0:
        player.turn = 'r'
        screen.blit(forward[f_index%8],(player.x+player.v,player.y))
        f_index += 1
        player.v += 15
    elif keys[pygame.K_LEFT] != 0:
        player.turn = 'l'
        screen.blit(backward[b_index%8],(player.x+player.v,player.y))
        b_index += 1
        player.v -= 15
    else:
        if player.turn == 'r':
            screen.blit(forward[0],(player.x+player.v,player.y))
        else:
            screen.blit(backward[3],(player.x+player.v,player.y))
            
    if not player.jump:
        if keys[pygame.K_UP] != 0:
            player.jump = True
    else:
        if player.s >= -10:
            player.y -= round((player.s * abs(player.s)) * 0.5)
            player.s -= 1
        else:
            player.s = 10
            player.jump = False

    if keys[pygame.K_SPACE] != 0:
        if player.turn == 'r':
            facing = 1
        else:
            facing = -1

        if len(bullets) < 5:
            bullets.append(Blast(round(player.x+player.v+player.width/2),round(player.y+player.height/2),6,(169,169,169),facing))

    for bullet in bullets:
        if bullet.x < width and bullet.x > 0:
            bullet.x += bullet.v
            bullet.draw(screen)
        else:
            bullets.remove(bullet)
            
    
    pygame.display.update()
    clock.tick(FPS)
