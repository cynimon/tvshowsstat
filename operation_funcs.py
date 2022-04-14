import user_messages as um
import db_func as df
import show_classes as sc


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


def welcome_manager(choice):
    options = {1: um.opt1, 2: um.opt2, 3: um.opt3}
    x = int(um.show_message(options[choice]))
    if choice == 1:
        if x == 1:
            add_show()
        elif x == 2:
            pass
        elif x == 3:
            pass
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


def goodbye():
    pass
