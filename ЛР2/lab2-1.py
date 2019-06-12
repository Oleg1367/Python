import random

my_number = random.randint(1, 100) #генерация случайного числа от 1 до 100
user_number = int(input("Введите число user_number:")) #ввод числа
while(user_number >= my_number): #Запрос, пока не угадает
    print("Это число слишком большое.")
    user_number = int(input("Введите число user_number:"))
    
print("Да, это число меньше my_number!")


