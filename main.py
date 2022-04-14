import user_messages as um
import operation_funcs as of
import sys

def main():
    of.hello()
    choice = int(um.show_message())
    of.welcome_manager(choice)
    conn.close()
    choice = input('Продолжить работу? д/н ').lower()
    if choice == 'д':
        main()
    else:
        sys.exit()


if __name__ == '__main__':
    main()
