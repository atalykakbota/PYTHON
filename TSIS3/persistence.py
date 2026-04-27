import json   # модуль для работы с JSON

def load_data(file, default):
    # загружает данные из JSON файла
    # если файл отсутствует или ошибка чтения — возвращает значение по умолчанию
    try:
        with open(file, "r") as f:
            return json.load(f)
    except:
        return default

def save_data(file, data):
    # сохраняет данные в JSON файл с отступами для удобного чтения
    with open(file, "w") as f:
        json.dump(data, f, indent=4)