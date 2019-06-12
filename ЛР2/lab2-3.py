import random

s = ""
for i in range(5):
    s += (chr(random.randint(0x0410, 0x042F))) #Случайная русская заглавная буква, юникод
    
print(s)
