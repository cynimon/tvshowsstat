import user_messages as um
import db_func as df
import show_classes as sc
import sql_queries as sqql

# добавление нового шоу в базу
def add_show():
    new_show = []
    for t in um.create_show:
        new_show.append(um.show_message(t))
    print('Выбрать жанр: ')
    result = df.execute_read_query(conn, 'SELECT * FROM genre;')
    for c in result:
        print(*c)
    new_show.append(um.show_message(''))
    my_show = sc.Show(*new_show)
    my_show.create_show()

# изменение параметров шоу в базе
def get_show(n):
    name_show = []
    for t in n:
        name_show.append(um.show_message(t))
    if n == um.change_eps:
        df.execute_query(conn, sqql.change_eps_amount, (name_show[1], name_show[0]))
    elif n == um.change_show_stat:
        df.execute_query(conn, sqql.change_show_stat, (name_show[1], name_show[0]))

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
            add_show()
        elif x == 2:
            pass
        elif x == 3:
            pass
        elif x == 4:
            pass
    elif choice == 3:
        if x == 1:
            pass
        elif x == 2:
            pass
        elif x == 3:
            pass


def hello():
    global conn
    conn = df.connect()
    if conn:
        print('Привет!')