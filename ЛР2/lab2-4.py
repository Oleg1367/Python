s = input("Введите строку: ")
z = "" #новая строка
for i in range(0, len(s)):
    if(s[i].isdigit()): #Если символ - цифра, добавляем его
        z += s[i]
print(z)
