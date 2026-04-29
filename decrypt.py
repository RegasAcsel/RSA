# Ввод названия файла шифротекста
cyphertext_file = input("Введите название файла шифртекста: ")
# Чтение файла шифротекста
with open(cyphertext_file, 'r', encoding='utf-8') as file:
    cyphertext_content = file.read().strip()
# Преобразуем строку с числами через запятую в список чисел
cyphertext = [int(x.strip()) for x in cyphertext_content.split(',')]

# Ввод названия файла приватного ключа
filename = input("Введите название файла ключа: ")
# Чтение файла приватного ключа
with open(filename, 'r', encoding='utf-8') as file:
    key_content = file.read().strip()
# Разделение по запятой и преобразование в числа
d_str, mod_str = key_content.split(',')
d = int(d_str.strip())
mod = int(mod_str.strip())

# Расшифровка шифртекста приватным ключом 
decrypted = [pow(num, d, mod) for num in cyphertext]
# Перевод чисел в буквы 
decrypted_text = ''.join(chr(num) for num in decrypted)

# Результат выполнения программы
print(f"Зашифрованный текст: {decrypted_text}")

output_filename = input("Введите имя файла для сохранения результата: ")
with open(output_filename, 'w', encoding='utf-8') as file:
    file.write(decrypted_text)

print(f"Результат сохранен в файл {output_filename}")
