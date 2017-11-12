# modify the Player class so that, instead of having the player just stay at the edge if they
# try and move past it, they'll appear at the other side (like in PacMan)

import pygame
import random

class Ball:
  def __init__(self,color,coords,size,speed):
    self.color = color
    self.initial_coords = list(coords)
    self.coords = coords
    self.size = size
    self.speed = speed

  def move(self, direction):
    if direction == 'up':
      self.coords[1] -= self.speed
    elif direction == 'down':
      self.coords[1] += self.speed
    elif direction == 'left':
      self.coords[0] -= self.speed
    else:
      self.coords[0] += self.speed

  def draw(self, window):
    pygame.draw.rect(window, self.color, (self.coords, self.size))

  def check_boundaries(self, screen_size):
    for i in [0, 1]:
      if (self.coords[i] < 0):
        self.coords[i] = 0
      elif (self.coords[i] >= screen_size[i] - self.size[i]):
        self.coords[i] = screen_size[i] - self.size[i]

  def has_collided(self, player):
    return ((self.coords[0] < player.coords[0] + player.size[0]) and
            (player.coords[0] < self.coords[0] + self.size[0]) and
            (self.coords[1] < player.coords[1] + player.size[1]) and
            (player.coords[1] < self.coords[1] + self.size[1]))

class Player:
  def __init__(self, color, coords, size, speed):
    self.color = color
    self.initial_coords = list(coords)
    self.coords = coords
    self.size = size
    self.speed = speed

  def move(self, direction):
    if direction == 'up':
      self.coords[1] -= self.speed
    elif direction == 'down':
      self.coords[1] += self.speed
    elif direction == 'left':
      self.coords[0] -= self.speed
    else:
      self.coords[0] += self.speed

  def draw(self, window):
    pygame.draw.rect(window, self.color, (self.coords, self.size))

  def check_boundaries(self, screen_size):
    for i in [0, 1]:
      if (self.coords[i] < 0):
        self.coords[i] = 0
      elif (self.coords[i] >= screen_size[i] - self.size[i]):
        self.coords[i] = screen_size[i] - self.size[i]

  def has_collided(self, player):
    return ((self.coords[0] < player.coords[0] + player.size[0]) and
            (player.coords[0] < self.coords[0] + self.size[0]) and
            (self.coords[1] < player.coords[1] + player.size[1]) and
            (player.coords[1] < self.coords[1] + self.size[1]))

  def reset(self):
    self.coords = list(self.initial_coords)

WINDOW_SIZE = [1800, 750]
PLAYER_SIZE = [9, 45]
BALL_SIZE = [15,15]

ball = Ball(
  pygame.Color('white'),
  [900,325],
  BALL_SIZE,
  8
  )

#############

northwall = Player(
  pygame.Color('green'),
  [0,0],
  [1800,5],
  0
  )

eastwall = Player(
pygame.Color('green'),
[1799,5],
[1,750],
0
)

#############

rgtul = Player(
  pygame.Color('red'),
  [300, 0],
  PLAYER_SIZE,
  8
)

rgtur = Player(
  pygame.Color('red'),
  [309,0],
  PLAYER_SIZE,
  8
)

rgtml = Player(
  pygame.Color('red'),
  [300,45],
  PLAYER_SIZE,
  8
)

rgtmr = Player(
  pygame.Color('red'),
  [309, 45],
  PLAYER_SIZE,
  8
)

rgtbl = Player(
  pygame.Color('red'),
  [300, 90],
  PLAYER_SIZE,
  8
)

rgtbr = Player(
  pygame.Color('red'),
  [309, 90],
  PLAYER_SIZE,
  8
)

################

rgmul = Player(
  pygame.Color('red'),
  [300, 210],
  PLAYER_SIZE,
  8
)

rgmur = Player(
  pygame.Color('red'),
  [309,210],
  PLAYER_SIZE,
  8
)

rgmml = Player(
  pygame.Color('red'),
  [300,255],
  PLAYER_SIZE,
  8
)

rgmmr = Player(
  pygame.Color('red'),
  [309, 255],
  PLAYER_SIZE,
  8
)

rgmbl = Player(
  pygame.Color('red'),
  [300, 300],
  PLAYER_SIZE,
  8
)

rgmbr = Player(
  pygame.Color('red'),
  [309, 300],
  PLAYER_SIZE,
  8
)

##############

rgbul = Player(
  pygame.Color('red'),
  [300,420],
  PLAYER_SIZE,
  8
)

rgbur = Player(
  pygame.Color('red'),
  [309,420],
  PLAYER_SIZE,
  8
)

rgbml = Player(
  pygame.Color('red'),
  [300,465],
  PLAYER_SIZE,
  8
)

rgbmr = Player(
  pygame.Color('red'),
  [309,465],
  PLAYER_SIZE,
  8
)

rgbbl = Player(
  pygame.Color('red'),
  [300, 510],
  PLAYER_SIZE,
  8
)

rgbbr = Player(
  pygame.Color('red'),
  [309, 510],
  PLAYER_SIZE,
  8
)

##############

window = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
ball_direction = random.randint(1,6)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit()

  keys = pygame.key.get_pressed()
  if keys[pygame.K_q]:
    rgtul.move('up')
    rgtur.move('up')
    rgtml.move('up')
    rgtmr.move('up')
    rgtbl.move('up')
    rgtbr.move('up')
    rgmul.move('up')
    rgmur.move('up')
    rgmml.move('up')
    rgmmr.move('up')
    rgmbl.move('up')
    rgmbr.move('up')
    rgbul.move('up')
    rgbur.move('up')
    rgbml.move('up')
    rgbmr.move('up')
    rgbbl.move('up')
    rgbbr.move('up')
  elif keys[pygame.K_a]:
    rgtul.move('down')
    rgtur.move('down')
    rgtml.move('down')
    rgtmr.move('down')
    rgtbl.move('down')
    rgtbr.move('down')
    rgmul.move('down')
    rgmur.move('down')
    rgmml.move('down')
    rgmmr.move('down')
    rgmbl.move('down')
    rgmbr.move('down')
    rgbul.move('down')
    rgbur.move('down')
    rgbml.move('down')
    rgbmr.move('down')
    rgbbl.move('down')
    rgbbr.move('down')

  if ball_direction==1:
    ball.move('up')
    ball.move('left')
    ball.move('left')
  elif ball_direction==2:
    ball.move('up')
    ball.move('right')
    ball.move('right')
  elif ball_direction==3:
    ball.move('left')
    ball.move('left')
  elif ball_direction==4:
    ball.move('right')
    ball.move('right')
  elif ball_direction==5:
    ball.move('down')
    ball.move('left')
    ball.move('left')
  else:
    ball.move('down')
    ball.move('right')
    ball.move('right')

  if ball.has_collided(northwall) & ball_direction == 1:
    ball_direction = 2
  elif ball.has_collided(northwall) & ball_direction == 2:
    ball_direction = 1
  elif ball.has_collided(eastwall) & ball_direction == 4:
    ball_direction = 3
  elif ball.has_collided(eastwall) & ball_direction == 1:
    ball_direction = 2

  if ball.has_collided(rgtur):
    ball.move('up')
    ball.move('right')
    ball.move('right')
    ball_direction = 2

  rgtul.check_boundaries([309,0])
  rgtur.check_boundaries([318,0])
  rgtml.check_boundaries([309,45])
  rgtmr.check_boundaries([318,45])
  rgtbl.check_boundaries([309,90])
  rgtbr.check_boundaries([318,90])
  rgmul.check_boundaries([309,210])
  rgmur.check_boundaries([318,210])
  rgmml.check_boundaries([309,255])
  rgmmr.check_boundaries([318,255])
  rgmbl.check_boundaries([309,300])
  rgmbr.check_boundaries([318,300])
  rgbul.check_boundaries([309,420])
  rgbur.check_boundaries([318,420])
  rgbml.check_boundaries([309,465])
  rgbmr.check_boundaries([318,465])
  rgbbl.check_boundaries([309,510])
  rgbbr.check_boundaries([318,510])
  ball.check_boundaries(WINDOW_SIZE)

  window.fill(pygame.Color('green'))

  rgtul.draw(window)
  rgtur.draw(window)
  rgtml.draw(window)
  rgtmr.draw(window)
  rgtbl.draw(window)
  rgtbr.draw(window)
  rgmul.draw(window)
  rgmur.draw(window)
  rgmml.draw(window)
  rgmmr.draw(window)
  rgmbl.draw(window)
  rgmbr.draw(window)
  rgbul.draw(window)
  rgbur.draw(window)
  rgbml.draw(window)
  rgbmr.draw(window)
  rgbbl.draw(window)
  rgbbr.draw(window)
  ball.draw(window)

  pygame.display.update()
  clock.tick(60)