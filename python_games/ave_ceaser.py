def decription_en(s):
    upper_en =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_en = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    st = str()

    for i in range(1, 26):
        for j in s:
            if j in upper_en:
                find_i = upper_en.find(j)
                find_i += i
                st += upper_en[find_i]
            elif j in lower_en:
                find_i = lower_en.find(j)
                find_i += i
                st += lower_en[find_i]
            else:
                st += j
    print(st)

def rus_encription(n, s):
    upper_ru =  'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    lower_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
    st = str()

    for i in s:
        if i in upper_ru:
            find_i = upper_ru.find(i)
            find_i += n
            st += upper_ru[find_i]
        elif i in lower_ru:
            find_i = lower_ru.find(i)
            find_i += n
            st += lower_ru[find_i]
        else:
            st += i
    print(st)

def eng_encription(n, s):
    upper_en =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_en = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    st = str()

    for i in s:
        if i in upper_en:
            find_i = upper_en.find(i)
            find_i += n
            st += upper_en[find_i]
        elif i in lower_en:
            find_i = lower_en.find(i)
            find_i += n
            st += lower_en[find_i]
        else:
            st += i
    print(st)

def rus_decription(n, s):
    upper_ru =  'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    lower_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
    st = str()

    for i in s:
        if i in upper_ru:
            find_i = upper_ru.find(i)
            find_i -= n
            st += upper_ru[find_i]
        elif i in lower_ru:
            find_i = lower_ru.find(i)
            find_i -= n
            st += lower_ru[find_i]
        else:
            st += i
    print(st)


def eng_decription(n, s):
    upper_en =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_en = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    st = str()

    for i in s:
        if i in upper_en:
            find_i = upper_en.find(i)
            find_i -= n
            st += upper_en[find_i]
        elif i in lower_en:
            find_i = lower_en.find(i)
            find_i -= n
            st += lower_en[find_i]
        else:
            st += i
    print(st)

    
print('Введите текст')
s = str(input())
print('Введите шаг сдвига')
n = int(input())
print('Если текст на русском, нажмите 1. На английском 0')
lang = int(input())
if lang == 1:
    print('Для шифроки нажмите 1, для дешифровки 0')
    crypt = int(input())
    if crypt == 1:
        rus_encription(n, s)
    else:
        rus_decription(n, s)
elif lang == 0:
    print('Для шифроки нажмите 1, для дешифровки 0')
    crypt = int(input())
    if crypt == 1:
        eng_encription(n, s)
    else:
        eng_decription(n, s)