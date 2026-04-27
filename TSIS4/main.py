import pygame, sys, json, random
from db import save_result, top10, personal_best   # работа с базой данных
from game import Snake, Food, Obstacle, PowerUp, CELL_SIZE, GRID_WIDTH, GRID_HEIGHT  # игровые классы

pygame.init()
screen = pygame.display.set_mode((GRID_WIDTH*CELL_SIZE, GRID_HEIGHT*CELL_SIZE))  # создаём окно
pygame.display.set_caption("Snake Game")

# загрузка настроек из JSON
with open("settings.json") as f: settings = json.load(f)

pygame.mixer.init()
# загрузка звуков
import os
import pygame

pygame.init()
pygame.mixer.init()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOUNDS_DIR = os.path.join(BASE_DIR, "assets", "sounds")

eat_sound = pygame.mixer.Sound(
    os.path.join(SOUNDS_DIR, "free-sound-1674743464.mp3")
)

gameover_sound = pygame.mixer.Sound(
    os.path.join(SOUNDS_DIR, "free-sound-1675012530.mp3")
)

pygame.mixer.music.load(
    os.path.join(SOUNDS_DIR, "super-mario-bros_2.mp3")
)

# установка громкости
eat_sound.set_volume(1.0 if settings["sound"] else 0.0)
gameover_sound.set_volume(1.0 if settings["sound"] else 0.0)
pygame.mixer.music.set_volume(1.0 if settings["sound"] else 0.0)

if settings["sound"]:
    pygame.mixer.music.play(-1)   # фоновая музыка

def load_scaled(path):
    # загружает картинку и масштабирует под размер клетки
    img = pygame.image.load(path)
    return pygame.transform.scale(img, (CELL_SIZE, CELL_SIZE))

# загрузка изображений
import os
import pygame
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
IMAGES_DIR = os.path.join(ASSETS_DIR, "images")

background_img = pygame.image.load(
    os.path.join(IMAGES_DIR, "background.png")
)

snake_img = load_scaled(
    os.path.join(IMAGES_DIR, "snake.png")
)

food_img = load_scaled(
    os.path.join(IMAGES_DIR, "food.png")
)

poison_img = load_scaled(
    os.path.join(IMAGES_DIR, "poison.png")
)

username = ""   # имя игрока

def username_entry():
    # ввод имени пользователя
    global username
    font = pygame.font.SysFont("Arial", 36)
    input_box = pygame.Rect(250, 250, 300, 50)
    active = True
    text = ""
    while active:
        screen.blit(background_img, (0,0))
        txt_surface = font.render("Enter Username: " + text, True, (255,255,255))
        screen.blit(txt_surface, (250,200))
        pygame.draw.rect(screen, (255,255,255), input_box, 2)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    username = text
                    active = False
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

def main_menu():
    # главное меню
    running = True
    font = pygame.font.SysFont("Arial", 36)
    while running:
        screen.blit(background_img, (0,0))
        play_text = font.render("Play (P)", True, (255,255,255))
        score_text = font.render("Leaderboard (L)", True, (255,255,255))
        settings_text = font.render("Settings (S)", True, (255,255,255))
        quit_text = font.render("Quit (Q)", True, (255,255,255))
        screen.blit(play_text, (300,160))
        screen.blit(score_text, (270,260))
        screen.blit(settings_text, (280,360))
        screen.blit(quit_text, (320,460))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p: run_game(username)
                elif event.key == pygame.K_l: leaderboard_screen()
                elif event.key == pygame.K_s: settings_screen()
                elif event.key == pygame.K_q: pygame.quit(); sys.exit()

def leaderboard_screen():
    # экран таблицы лидеров
    rows = top10()
    font = pygame.font.SysFont("Arial", 24)
    running = True
    while running:
        screen.fill((0,0,0))
        y = 50
        for i,row in enumerate(rows):
            text = font.render(f"{i+1}. {row[0]} {row[1]} pts Level {row[2]} {row[3]}", True, (255,255,255))
            screen.blit(text, (20,y)); y+=30
        back_text = font.render("Press ESC to return", True, (255,255,255))
        screen.blit(back_text, (20, y+40))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

def settings_screen():
    # экран настроек (звук ON/OFF)
    running = True
    font = pygame.font.SysFont("Arial", 24)
    while running:
        screen.fill((0,0,0))
        text = font.render(f"Sound: {'ON' if settings['sound'] else 'OFF'}", True, (255,255,255))
        screen.blit(text, (250,250))
        back_text = font.render("Press ESC to return", True, (255,255,255))
        screen.blit(back_text, (250,300))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # переключение звука
                    settings["sound"] = not settings["sound"]
                    with open("settings.json","w") as f: json.dump(settings,f)
                    if settings["sound"]:
                        pygame.mixer.music.play(-1)
                        pygame.mixer.music.set_volume(1.0)
                        eat_sound.set_volume(1.0)
                        gameover_sound.set_volume(1.0)
                    else:
                        pygame.mixer.music.stop()
                        eat_sound.set_volume(0.0)
                        gameover_sound.set_volume(0.0)
                elif event.key == pygame.K_ESCAPE:
                    running = False

def game_over_screen(username, score, level):
    # экран Game Over
    best = personal_best(username)
    save_result(username, score, level)
    running = True
    font = pygame.font.SysFont("Arial", 36)
    while running:
        screen.blit(background_img, (0,0))
        if settings["sound"]: gameover_sound.play()
        text = font.render(f"Game Over! Score: {score} Best: {best}", True, (255,255,255))
        screen.blit(text, (100, 200))
        back_text = font.render("Press ESC to return", True, (255,255,255))
        screen.blit(back_text, (100, 260))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

def run_game(username):
    # основной игровой цикл
    snake = Snake(tuple(settings["snake_color"]))
    food = Food("normal")
    poison = Food("poison")
    obstacles = Obstacle(1)
    powerup = None
    clock = pygame.time.Clock()
    score, level = 0, 1
    speed = 10
    running = True
    powerup_start = None

    while running:
        # обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: snake.direction=(0,-1)
                elif event.key == pygame.K_DOWN: snake.direction=(0,1)
                elif event.key == pygame.K_LEFT: snake.direction=(-1,0)
                elif event.key == pygame.K_RIGHT: snake.direction=(1,0)

        snake.move()

        # проверка еды
        if snake.body[0] == food.pos:
            snake.eat_food("normal")
            score += 10
            if settings["sound"]: eat_sound.play()
            food = Food("normal", obstacles.blocks)

        # проверка яда
        if snake.body[0] == poison.pos:
            if snake.eat_food("poison") == "gameover":
                game_over_screen(username, score, level)
                return
            if settings["sound"]: gameover_sound.play()
            poison = Food("poison", obstacles.blocks)

        # появление бонусов
        if powerup is None and random.randint(0,200) == 1:
            powerup = PowerUp(obstacles.blocks)
        if powerup and powerup.expired():
            powerup = None

        if powerup and snake.body[0] == powerup.pos:
            # активация бонуса
            if powerup.kind == "speed":
                speed = 20; powerup_start = pygame.time.get_ticks()
            elif powerup.kind == "slow":
                speed = 5; powerup_start = pygame.time.get_ticks()
            elif powerup.kind == "shield":
                snake.shield = True
            powerup = None

        # проверка столкновений
        head_x, head_y = snake.body[0]
        if (head_x < 0 or head_x >= GRID_WIDTH or head_y < 0 or head_y >= GRID_HEIGHT
            or snake.body[0] in snake.body[1:]
            or snake.body[0] in obstacles.blocks):
            if snake.shield:
                snake.shield = False   # щит спасает один раз
            else:
                game_over_screen(username, score, level)
                return

        # повышение уровня каждые 50 очков
        if score // 50 + 1 > level:
            level += 1
            obstacles = Obstacle(level, snake.body[0])

        # отрисовка объектов
        screen.blit(background_img, (0,0))
        screen.blit(food_img, (food.pos[0]*CELL_SIZE, food.pos[1]*CELL_SIZE))
        screen.blit(poison_img, (poison.pos[0]*CELL_SIZE, poison.pos[1]*CELL_SIZE))
        if powerup:
            pygame.draw.rect(screen, powerup.color,
                             (powerup.pos[0]*CELL_SIZE, powerup.pos[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
        for ox, oy in obstacles.blocks:
            pygame.draw.rect(screen, (150,150,150), (ox*CELL_SIZE, oy*CELL_SIZE, CELL_SIZE, CELL_SIZE))
        for x,y in snake.body:
            screen.blit(snake_img, (x*CELL_SIZE, y*CELL_SIZE))

        # вывод текста (очки, уровень, игрок)
        font = pygame.font.SysFont("Arial", 24)
        score_text = font.render(f"Score: {score}  Level: {level}", True, (255,255,255))
        screen.blit(score_text, (10,10))
        user_text = font.render(f"Player: {username}", True, (255,255,255))
        screen.blit(user_text, (10,40))

        pygame.display.flip()

        # возврат скорости после бонуса
        if powerup_start and pygame.time.get_ticks() - powerup_start > 5000:
            speed = 10 + level
            powerup_start = None

        clock.tick(speed)

if __name__ == "__main__":
    username_entry()   # ввод имени игрока
    main_menu()        # запуск главного меню