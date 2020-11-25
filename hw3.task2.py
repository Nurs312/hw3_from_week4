text = input("Введите слова через пробел: ").split(' ')
print(sorted(text, key=len))