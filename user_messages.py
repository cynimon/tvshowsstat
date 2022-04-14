# welcome

welcome = ('1. Работа с базой сериалов\n'
           '2. Работа с твоими сериалами\n'
           '3. Немножко статистики\n')

opt1 = ('1. Добавить сериал\n'
        '2. Изменить количество эпизодов сериала\n'
        '3. Изменить статус сериала\n')

opt2 = ('1. Добавить сериал в "Буду смотреть"\n'
        '2. Добавить сериал в "Смотрю"\n'
        '3. Изменить статус сериала на "Перестал смотреть"\n'
        '4. Добавить просмотренный эпизод в сериал\n')

opt3 = ('1. Статистика по количеству\n'
        '2. Статистика по времени\n'
        '3. Статистика по жанрам\n')

# пройти по кортежу и каждый раз вызывать штуку
create_show = ('Название сериала', 'Количество эпизодов', 'Длительность эпизода (в минутах)',
               'Год начала', 'Год конца (если не закончен, ставим текущий)', 'Закончен? д/н')
change_eps = ('Название сериала', 'Сколько эпизодов добавить')
change_show_stat = ('Название сериала', 'Сериал закончен? д/н')

name = 'Название сериала'

eps_watched = ('Название сериала', 'Сколько эпизодов просмотрено?')


def show_message(msg=welcome):
    print(msg)
    text = input('Ввод действия (текста): ')
    return text
