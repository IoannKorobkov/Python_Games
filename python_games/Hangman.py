import random
# ИГРА В УГАДАЙ СЛОВО с 5-ю ПОПЫТКМАМИ
word_list = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна']
# функция, генерирующая слово
def get_word(word_list):
    ind_word_list = random.randrange(len(word_list))
    word = word_list[ind_word_list]
    return word
# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                                # голова и торс
                '''
                   --------
                   |      |
                   |      Oj
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]
def play(word):
    print("Давай сыграем в угадайку слов")
    tries = 6
    display_hangman(tries)
    l = len(word)
    hidden_word = '_ ' * l
    print(hidden_word)
    guessed = str()
    answer = ['_' for _ in range(l)]
    
    while True:
        print('Введите букву или слово целиком')
        input_word = str(input())
        input_word = input_word.lower()
        
        for i in input_word:
            if i not in 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя':
                print('Ошибка ввода! Попробуйте еще раз')
            elif i in 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя':
                    if i in guessed:
                        print('Уже было!')
                    else:  
                        if i in word:
                            guessed += i
                            print('Эта буква есть в загаданном слове')    
                            for j in range(l):
                                if  word[j] ==i:
                                    answer = answer[:j] +[i]  + answer[j+1:]
                                    a =''.join(answer)
                            print(*answer)

                            if a == word:
                                print('Поздравляем, вы угадали слово! Вы победили!')
                                break
                        elif i not in word:
                            tries -= 1
                            print('Такой буквы нет в загаданном слове')
                            print(display_hangman(tries))
                            if tries == 0:
                                print('Вы проиграли, загаданное слово', word)
                                break  
word = get_word(word_list)                
play(word)