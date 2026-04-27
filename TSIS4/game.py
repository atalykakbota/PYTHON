import pygame, random

CELL_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = 40, 30

class Snake:
    def __init__(self, color):
        # начальные параметры змейки
        self.body = [(10,10)]        # список координат сегментов
        self.length = 3              # длина змейки
        self.direction = (1,0)       # направление движения (по X вправо)
        self.color = color           # цвет змейки
        self.shield = False          # наличие щита

    def move(self):
        # движение змейки
        head = (self.body[0][0]+self.direction[0], self.body[0][1]+self.direction[1])
        self.body.insert(0, head)    # добавляем новую голову
        if len(self.body) > self.length:
            self.body.pop()          # удаляем хвост, если длина превышает

    def eat_food(self, food_type):
        # обработка еды
        if food_type == "normal":
            self.length += 1
        elif food_type == "poison":
            self.length -= 2
            if self.length <= 1:
                return "gameover"    # проигрыш, если длина <= 1
        return "ok"

class Food:
    def __init__(self, kind="normal", obstacles=[]):
        # создаём еду в случайной позиции, избегая препятствий
        self.kind = kind
        while True:
            pos = (random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))
            if pos not in obstacles:
                self.pos = pos
                break

class Obstacle:
    def __init__(self, level, snake_pos=(10,10)):
        # создаём препятствия начиная с уровня 3
        self.blocks = []
        if level >= 3:
            while len(self.blocks) < level*2:
                pos = (random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))
                # условие: препятствие не должно появиться на змейке
                if pos != snake_pos and pos not in self.blocks:
                    self.blocks.append(pos)

class PowerUp:
    TYPES = ["speed","slow","shield"]
    def __init__(self, obstacles=[]):
        # создаём бонус в случайной позиции, избегая препятствий
        while True:
            pos = (random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))
            if pos not in obstacles:
                self.pos = pos
                break
        self.kind = random.choice(PowerUp.TYPES)   # тип бонуса
        self.spawn_time = pygame.time.get_ticks()  # время появления
        self.color = {"speed":(0,0,255),"slow":(255,255,0),"shield":(255,0,255)}[self.kind]

    def expired(self):
        # проверка: бонус исчезает через 8 секунд
        return pygame.time.get_ticks() - self.spawn_time > 8000