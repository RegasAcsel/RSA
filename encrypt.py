# Функция переводаиз текста в Unicode
def text_to_numbers(text):
    """Каждый символ заменяется на его код ASCII/Unicode"""
    return [ord(c) for c in text]

# Ввод текста для шифровки
text = input("Введите текст для шифровки: ")
result = text_to_numbers(text)

# Ввод названия файла
filename = input("Введите название файла: ")

# Чтение файла
with open(filename, 'r', encoding='utf-8') as file:
    content = file.read().strip()

# Разделение по запятой и преобразование в числа
e_str, mod_str = content.split(',')
e = int(e_str.strip())
mod = int(mod_str.strip())

# Шифровка текста открытым ключом 
encrypted = [pow(num, e, mod) for num in result]

# Результат выполнения программы
print(f"Зашифрованный текст: {encrypted}")

output_filename = input("Введите имя файла для сохранения результата: ")
with open(output_filename, 'w', encoding='utf-8') as file:
    # Преобразуем список в строку с числами через запятую
    encrypted_str = ', '.join(str(num) for num in encrypted)
    file.write(encrypted_str)

print(f"Результат сохранен в файл {output_filename}")
