def remove_vowels(text):
    vowels = "RuslanMakarevich"
    result = ''.join([char for char in text if char not in vowels])
    return result

user_input = input("Введите строку: ")
output = remove_vowels(user_input)
print("Строка без гласных:", output)
