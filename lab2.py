def z1():
    a = input()
    b = input()
    if a == b:
        print("пароль совпадает")
    else:
        print("пароль не совпадает")
z1()
def z2():
    n = int(input('введите номер места в вагоне'))
    print()
    if n > 36 and n % 2:
        print('боковое место сверху')
    elif n > 36 and n != n % 2:
        print('боковое место сверху')
    elif n < 36 and n % 2:
    print('купе сверху')
    else:
    print('купе сверху')
z2()

def z3():
    year = int(input())
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print('да високосный')
    else:
        print('нет не високосный')
z3()

def z4():
    a, b = input(), input()
    if a != 'красный' and a != 'желтый' and a != 'синий':
        print('ошибка цвета ')
    elif b != 'красный' and b != 'желтый' and b != 'синий':
        print('ошибка цвета ')
    elif a == 'красный' and b == 'синий' or b == 'красный' and a == 'синий':
        print('фиолетовый')
    elif a == 'красный' and b == 'желтый' or b == 'красный' and a == 'желтый':
        print('оранжевый')
    elif a == 'синий' and b == 'желтый' or b == 'синий' and a == 'желтый':
        print('зеленый')
    elif a == 'красный' and b == 'красный':
        print('красный')
    elif a == 'синий' and b == 'синий':
        print('синий')
    elif a == 'желтый' and b == 'желтый':
        print('желтый')
z4()