import random
# ИГРА МАГИЧЕСКИЙ ШАР КОТОРЫЙ ОТВЕЧАЕТ НА ВОПРОСЫ
answers = ['Бесспорно',	'Мне кажется - да',	'Пока неясно, попробуй снова', 'Даже не думай',
'Предрешено', 'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет',
'Никаких сомнений',	'Хорошие перспективы',	'Лучше не рассказывать', 'По моим данным - нет',
'Определённо да', 'Знаки говорят - да',	'Сейчас нельзя предсказать',	'Перспективы не очень хорошие',
'Можешь быть уверен в этом',	'Да',	'Сконцентрируйся и спроси опять',	'Весьма сомнительно']
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
print('Назовите своё имя')
name = input()
print(f'Привет {name}')
while True:
    print('Какой у вас вопрос?')
    quest = input()
    print(random.choice(answers))
    print('Хотите ли вы задать еще один вопрос, введите "да" или "нет"')
    end = input().lower()
    if end == 'да':
        continue
    else:
        print('Возвращайся если возникнут вопросы!')
        break

