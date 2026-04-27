import pygame, random

class GameObject(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()                      # инициализация базового класса Sprite
        self.image = image                      # картинка объекта
        self.rect = self.image.get_rect(center=(x, y))  # прямоугольник для позиции и столкновений

class Enemy(GameObject):
    def __init__(self, image, speed, width):
        # создаём врага в случайной позиции по оси X, сверху экрана
        super().__init__(image, random.randint(50, width-50), -100)
        self.speed = speed                      # скорость движения врага

    def update(self):
        # обновление позиции врага (движение вниз)
        self.rect.y += self.speed