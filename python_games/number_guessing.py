import random
import math

def is_valid(i):
    if True != i.isdigit():
        return False
    i = float(i)
    if i != int(i):
        return False
    else: 
        if 1 <= i <= 100:
            return True
        else:
            return False

count = 0
print('Добро пожаловать в числовую угадайку')
print('Каким максимально возможным может быть загаданное число? ')
end = int(input())
n = random.randint(1,end)
while True:
    print(f'Введите любое целое число от 1 до {end}')
    n1 = input()
    if is_valid(n1) == True:
        print("Число корректно")
        n1 = int(n1)
        count += 1
        if n1 == n:
            print(f'Вы угадали c {count} попытки, поздравляем!')
            print('Хотите сыграть ещё раз? Введите "да" или "нет"')
            answer = input().lower()
            if answer == 'да' or answer == 'lf':
                continue
            else:
                break
        if n1 > n:
            print('Ваше число больше загаданного, попробуйте еще разок')
        if n1 < n:
            print('Ваше число меньше загаданного, попробуйте еще разок')
    else:
        print(f'А может быть все-таки введем целое число от 1 до {end}?')

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')