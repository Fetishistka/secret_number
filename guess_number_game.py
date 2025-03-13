import random

# Генерируем случайное число от 1 до 100
secret_number = random.randint(1, 100)
attempts = 7  # Ограничиваем количество попыток до 7

print("Добро пожаловать в игру 'Угадай число'!")
print(f"Я загадал число от 1 до 100. У тебя есть {attempts} попыток.")

# Основной цикл игры
while attempts > 0:
    # Запрашиваем у пользователя число
    try:
        guess = int(input("Введи свое предположение: "))
        
        # Проверяем, находится ли число в допустимом диапазоне
        if guess < 1 or guess > 100:
            print("Пожалуйста, введи число от 1 до 100!")
            continue
            
        # Уменьшаем количество оставшихся попыток
        attempts -= 1
        
        # Проверяем предположение
        if guess == secret_number:
            print(f"Поздравляю! Ты угадал число {secret_number}!")
            print(f"Осталось попыток: {attempts}")
            break
        elif guess < secret_number:
            print(f"Слишком маленькое число! Осталось попыток: {attempts}")
        else:
            print(f"Слишком большое число! Осталось попыток: {attempts}")
            
        # Если попытки закончились
        if attempts == 0:
            print(f"Игра окончена! Загаданное число было: {secret_number}")
            
    except ValueError:
        print("Пожалуйста, введи целое число!")