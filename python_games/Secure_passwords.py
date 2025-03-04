import random

def generate_password(length,chars):
    password = []
    for i in range(length):
        password.append(random.choice(chars))
    password = ''.join(password)
    return password

def isitdigit(z):
    while False == z.isdigit():
        print('Нужно ввести цифру')
        z = input()
    else:
        z = int(z)
        return(z)
    
def isitalpha(z):
    while False == z.isalpha():
        print('Нужно ввести "да" или "нет"')
        z = input()
    else:
        return(z)

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = "!#$%&*+-=?@^_."
chars = ''
print('Количество паролей для генерации? ')
que1 = input()
isitdigit(que1)
que1 = int(que1)
print('Длина одного пароля')
length = input()
isitdigit(length)
length = int(length)
print('Включать ли цифры')
que3 = input()
isitalpha(que3) 
if que3.lower() == 'да':
    chars += digits
print('Включать ли прописные буквы')
que4 = input()
isitalpha(que4) 
if que4.lower() == 'да':
    chars += uppercase_letters
print('Включать ли строчные буквы')
que5 = input()
isitalpha(que5) 
if que5.lower() == 'да':
    chars += lowercase_letters
print('Включать ли символы !#$%&*+-=?@^_.')
que6 = input()
isitalpha(que6) 
if que6.lower() == 'да':
    chars += digits
print('Исключать ли неоднозначные символы il1Lo0O')
que7 = input()
isitalpha(que7) 
if que7.lower() == 'да':
    ban ='il1Lo0O'
    chars = [i for i in chars]
    for i in range(len(chars)):
        if chars[i] in ban:
            chars[i] = ' '
chars = [i for i in chars if i != ' ']
chars = ''.join(chars)
while que1 > 0:
    print(generate_password(length,chars))
    que1 -= 1

