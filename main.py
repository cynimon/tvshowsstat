import user_messages as um
import operation_funcs as of


def main():
    of.hello()
    choice = int(um.show_message())
    of.welcome_manager(choice)
    choice = input('Продолжить работу? д/н ').lower()
    if choice == 'д':
        pass # рестарт программы через sys
    else:
        pass # exit программы через sys отключение от бд


if __name__ == '__main__':
    main()
