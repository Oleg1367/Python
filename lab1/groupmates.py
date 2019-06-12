#coding:utf-8
groupmates = [
    {
     "name": u"Василий",
     "group": u"912-2",
     "age": 19,
     "marks": [4, 3, 5, 5, 4]
    },
    {
     "name": u"Анна",
     "group": u"912-1",
     "age": 18,
     "marks": [3, 2, 3, 4, 3]
    },
    {
     "name": u"Георгий",
     "group": u"912-2",
     "age": 19,
     "marks": [3, 5, 4, 3, 5]
    },
    {
     "name": u"Валентина",
     "group": u"912-1",
     "age": 18,
     "marks": [5, 5, 5, 4, 5]
    }

]
    
def print_students(students):
    print u"Имя студента".ljust(15), \
          u"Группа".ljust(8), \
          u"Возраст".ljust(8), \
          u"Оценки".ljust(20)
    for student in students:
        print \
              student["name"].ljust(15), \
              student["group"].ljust(8), \
              str(student["age"]).ljust(8), \
              str(student["marks"]).ljust(20)
        print "\n"

print_students(groupmates)        
n = 0
def print_avr(avr,students):
    print u"Имя студента".ljust(15), \
          u"Группа".ljust(8), \
          u"Возраст".ljust(8), \
          u"Оценки".ljust(20)
    for student in students:
        if (sum(student["marks"])/len(student["marks"]) > avr):
            print \
                  student["name"].ljust(15), \
                  student["group"].ljust(8), \
                  str(student["age"]).ljust(8), \
                  str(student["marks"]).ljust(20)
av = input(u"Введите средний коэффициент оценки: ")
print_avr(av,groupmates)
