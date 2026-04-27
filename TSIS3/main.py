import pygame, random, sys, os
from persistence import load_data, save_data   # функции для работы с JSON (настройки, таблица лидеров)
from ui import UI                             # класс интерфейса (меню, текст)

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # рабочая директория = папка файла

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))     # создаём окно
pygame.display.set_caption("Racer Extended")          # заголовок окна
clock = pygame.time.Clock()

# загрузка настроек и таблицы лидеров
settings = load_data("settings.json", {"sound": True, "diff": 1, "user": "Player"})
leaderboard = load_data("leaderboard.json", [])
ui = UI(screen)

IMG_P = "assets/images/"   # путь к картинкам
SND_P = "assets/sounds/"   # путь к звукам

def get_img(name, size):
    # загружает картинку и масштабирует её
    return pygame.transform.scale(pygame.image.load(IMG_P + name), size).convert_alpha()

# загрузка изображений
ROAD = pygame.transform.scale(pygame.image.load(IMG_P + "background.png"), (WIDTH, HEIGHT))
PLAYER_IMG = get_img("player_car.png", (100, 120))
ENEMY_IMG = get_img("enemy_car.png", (140, 120))
COIN_IMG = get_img("oil.png", (50, 50))
NITRO_IMG = get_img("nitro.png", (50, 50))
SHIELD_IMG = get_img("shield.png", (50, 50))
REPAIR_IMG = get_img("repair.png", (50, 50))

# загрузка звуков
try:
    BG_MUSIC = SND_P + "sonican-lo-fi-music-loop-sentimental.mp3"
    CRASH_SND = pygame.mixer.Sound(SND_P + "vau-vau-vau--trombon-neudachi.mp3")
    COIN_SND = pygame.mixer.Sound(SND_P + "button-click-sharp-clear-sonorous.mp3")
except:
    BG_MUSIC = None

def start_game():
    # основной игровой цикл
    if settings['sound'] and BG_MUSIC and os.path.exists(BG_MUSIC):
        pygame.mixer.music.load(BG_MUSIC)
        pygame.mixer.music.play(-1)

    player_rect = PLAYER_IMG.get_rect(center=(WIDTH//2, HEIGHT-70))  # позиция игрока
    
    enemy_rect = None 
    items = []   # список бонусов
    score, dist, speed = 0, 0, 5 + settings['diff']
    active_pu, pu_timer, has_shield = None, 0, False

    running = True
    while running:
        screen.blit(ROAD, (0, 0))
        dist += speed / 60   # дистанция

        # обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.mixer.music.stop()
                return 0 

        # управление машиной
        keys = pygame.key.get_pressed()
        move = 10 if active_pu == "Nitro" else 6
        if keys[pygame.K_LEFT] and player_rect.left > 0: player_rect.x -= move
        if keys[pygame.K_RIGHT] and player_rect.right < WIDTH: player_rect.x += move

        # появление врага
        if enemy_rect is None:
            ex = random.choice([75, 155, 245, 325]) 
            enemy_rect = ENEMY_IMG.get_rect(center=(ex, -100))

        enemy_rect.y += speed

        # столкновение с врагом
        if player_rect.colliderect(enemy_rect):
            if has_shield:
                has_shield = False; active_pu = None
                enemy_rect = None 
            else:
                if settings['sound']: pygame.mixer.music.stop(); CRASH_SND.play()
                return int(score + dist)

        # враг ушёл за экран
        if enemy_rect and enemy_rect.top > HEIGHT:
            enemy_rect = None
            score += 1
            speed += 0.1 

        # появление бонусов
        if random.random() < 0.01:
            itype = random.choice(["Nitro", "Shield", "Repair", "Coin"])
            img = {"Nitro": NITRO_IMG, "Shield": SHIELD_IMG, "Repair": REPAIR_IMG, "Coin": COIN_IMG}[itype]
            items.append({"type": itype, "rect": img.get_rect(center=(random.randint(50, WIDTH-50), -50)), "img": img})

        # обработка бонусов
        for i in items[:]:
            i['rect'].y += 5
            if player_rect.colliderect(i['rect']):
                if settings['sound']: COIN_SND.play()
                if i['type'] == "Nitro": active_pu = "Nitro"; pu_timer = 180 # 3 сек
                elif i['type'] == "Shield": active_pu = "Shield"; has_shield = True
                elif i['type'] == "Repair": score += 5
                elif i['type'] == "Coin": score += 2
                items.remove(i)
            elif i['rect'].top > HEIGHT: items.remove(i)

        # таймер бонусов
        if pu_timer > 0: pu_timer -= 1
        else: active_pu = None if active_pu == "Nitro" else active_pu

        # отрисовка объектов
        screen.blit(PLAYER_IMG, player_rect)
        if enemy_rect: screen.blit(ENEMY_IMG, enemy_rect)
        for i in items: screen.blit(i['img'], i['rect'])
        
        ui.draw_text(f"Score: {score}  Dist: {int(dist)}m", 10, 10, (255,255,255))
        if active_pu: ui.draw_text(f"BUFF: {active_pu}", 10, 40, (255,255,0))
        
        pygame.display.update()
        clock.tick(60)

def main_menu():
    # главное меню
    while True:
        ui.show_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    res = start_game()
                    if res > 0:
                        leaderboard.append({"name": settings['user'], "score": res})
                        leaderboard.sort(key=lambda x: x['score'], reverse=True)
                        save_data("leaderboard.json", leaderboard[:10])
                if event.key == pygame.K_2: show_leaderboard()
                if event.key == pygame.K_3: settings_menu()
                if event.key == pygame.K_q: pygame.quit(); sys.exit()

def show_leaderboard():
    # экран таблицы лидеров
    waiting = True
    while waiting:
        ui.show_leaderboard(leaderboard)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b or event.key == pygame.K_q: waiting = False

def settings_menu():
    # переключение звука в настройках
    settings['sound'] = not settings['sound']
    save_data("settings.json", settings)

if __name__ == "__main__":
    main_menu()   # запуск программы