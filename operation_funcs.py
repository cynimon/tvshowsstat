import user_messages as um
import db_func as df
import show_classes as sc
import sql_queries as sqql
import datetime as dt


# добавление нового шоу в базу
def add_show():
    new_show = []
    for t in um.create_show:
        new_show.append(um.show_message(t))
    print('Выбрать жанр: ')
    df.read_query(conn, 'SELECT * FROM genre;')
    new_show.append(um.show_message(''))
    my_show = sc.Show(*new_show)
    my_show.create_show()


# изменение параметров шоу в базе
def get_show(n, choice=1):
    name_show = []
    for t in n:
        name_show.append(um.show_message(t))
    if n == um.change_eps:
        df.execute_query(conn, sqql.change_eps_amount, (name_show[1], name_show[0]))
    elif n == um.change_show_stat:
        df.execute_query(conn, sqql.change_show_stat, (name_show[1], name_show[0]))
    elif n == um.name:
        df.execute_query(conn, sqql.to_will_watch, (name_show[0],))
    elif choice == 2 and n == um.change_eps:
        df.execute_query(conn, sqql.to_watching, (name_show[0], name_show[1], name_show[0]))
    elif choice == 2 and n == um.name:
        df.execute_query(conn, sqql.to_cancelled, (name_show[0],))
    elif n == um.eps_watched:
        df.execute_query(conn, sqql.add_episodes, (name_show[1], name_show[0]))


# автоматическая перестановка статуса на "просмотрен полностью", если серии кончились
def check_completed():
    checking = df.execute_read_query(conn, sqql.completed_check)
    temp = []
    for c in checking:
        if int(c[1]) == int(c[2]):
            temp.append(c[0])
    for t in temp:
        df.execute_query(conn, sqql.to_completed, t)


def stats_amount():
    print('Буду смотреть')
    result = df.execute_read_query(conn, sqql.shows_willwatch)
    for r in result:
        print(*r, end=' | ')
    print('\nСмотрю')
    result = df.execute_read_query(conn, sqql.shows_watching)
    for r in result:
        print(*r, end=' | ')
    print('\nПолностью посмотрел')
    result = df.execute_read_query(conn, sqql.shows_completed)
    for r in result:
        print(*r, end=' | ')
    print('\nПерестал смотреть')
    result = df.execute_read_query(conn, sqql.shows_cancelled)
    for r in result:
        print(*r, end=' | ')
    print()
    df.read_query(conn, sqql.count_all)


def time_amount():
    result = df.execute_read_query(conn, sqql.time_each_show)
    print('Название', 'Насмотрено', 'Осталось', sep=' | ')
    for r in result:
        print(r[0], str(r[1]), str(r[2]), sep=' | ')
    print('Всего насмотрено: ')
    result = df.execute_read_query(conn, sqql.time_spend)
    print(str(result[0][0]))
    print('Всего осталось: ')
    result = df.execute_read_query(conn, sqql.time_left)
    print(str(result[0][0]))


def genre_amount():
    print('Сериалов по жанрам: ')
    df.read_query(conn, sqql.shows_by_genre)


# управление основными функциями приложения
def welcome_manager(choice):
    options = {1: um.opt1, 2: um.opt2, 3: um.opt3}
    x = int(um.show_message(options[choice]))
    if choice == 1:
        if x == 1:
            add_show()
        elif x == 2:
            get_show(um.change_eps)
        elif x == 3:
            get_show(um.change_show_stat)
    elif choice == 2:
        if x == 1:
            print('Выбираем сериал :)')
            df.read_query(conn, sqql.non_activity)
            get_show(um.name)
        elif x == 2:
            print('Выбираем сериал :)')
            df.read_query(conn, sqql.shows_willwatch)
            get_show(um.change_eps, 2)
        elif x == 3:
            print('Выбираем сериал :)')
            df.read_query(conn, sqql.shows_watching)
            get_show(um.name, 2)
        elif x == 4:
            print('Выбираем сериал :)')
            df.read_query(conn, sqql.shows_watching)
            get_show(um.eps_watched)
            check_completed()
    elif choice == 3:
        if x == 1:
            stats_amount()
        elif x == 2:
            time_amount()
        elif x == 3:
            genre_amount()


def hello():
    global conn
    conn = df.connect()
    if conn:
        print('Привет!')
    return conn
