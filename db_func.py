import psycopg2


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
    except psycopg2.OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


# исполнение команд
def execute_query(connection, query, data=None):
    connection.rollback()
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query, data)
        print('Успешно!')
    except psycopg2.OperationalError as e:
        print(f"The error '{e}' occurred")


# чтение выборки данных
def execute_read_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except psycopg2.OperationalError as e:
        print(f"The error '{e}' occurred")


def read_query(connection, query):
    result = execute_read_query(connection, query)
    for c in result:
        print(*c)


def connect():
    x = create_connection(
        "myshows", "postgres", "11qa", "127.0.0.1", "5432"
    )
    return x
