import random

def model(mod):
    n = mod
    count = 0
    p = None
    q = None
    
    for i in range(2, n):
        if n % i == 0:
            count += 1
            if count == 1:
                p = i
            elif count == 2:
                q = i
            if count > 2:
                break
    
    if count == 2:
        return p, q
    else:
        return None, None

def is_prime_simple(num):
    if num < 2:
        return False
    
    # Проверяем, есть ли делители у числа
    for i in range(2, num):
        if num % i == 0:
            return False  # если нашли делитель, число не простое
    
    return True  # если делителей нет, число простое

def find_e(fi):     # Поиск числа e, которое является простым, меньше fi, и fi не делится на e
    e = random.randint(2, fi)
    if is_prime_simple(e):
        # Проверяем, что fi не делится на e
        if fi % e != 0:
            return e
    return None

def find_d(e, fi):
    d = pow(e, -1, fi)
    return d

def random_number():
    while True:
        mod = random.randint(100, 1000000)
        p, q = model(mod)
        
        if p and q:
            fi = (p - 1) * (q - 1)
            e = find_e(fi)
            
            if e:
                # Находим обратное число d
                d = find_d(e, fi)
                
                if d:
                    
                    # Записываем e и mod в файл open.txt (открытый ключ)
                    with open('open.txt', 'w', encoding='utf-8') as file:
                        file.write(f"{e},{mod}")
                    
                    # Записываем d и mod в файл private.txt (закрытый ключ)
                    with open('private.txt', 'w', encoding='utf-8') as file:
                        file.write(f"{d},{mod}")
                    
                    print("Ключи успешно созданы")
                    input("\nНажмите Enter для выхода...")
                    break
                else:
                    print(f"Для e = {e} не найдено обратное число d")
            else:
                print(f"Для φ = {fi} не найдено подходящее e")

# Запускаем функцию
random_number()
