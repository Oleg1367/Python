l = list(input("Введите строки через пробел:").split()) #ввод строк
for i in range(0, len(l)): #Основной цикл задания
    if ((len(l[i]) <= 10) and (len(l[i]) >= 5)): #Условие
        print(l[i])
