from database_connection import get_database_connection

def create_int_generator(i_start=0):
    i = i_start
    while True:
        yield i
        i += 1

generator_user_id = create_int_generator()
generator_vinkki_id = create_int_generator()

def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;
    ''')
    cursor.execute('''
        drop table if exists vinkit;
    ''')
    connection.commit()


def create_users_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
        create table users (
            id integer PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        );
    ''')
    connection.commit()


def create_vinkit_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
        create table vinkit (
            id integer PRIMARY KEY,
            name TEXT NOT NULL
        );
    ''')
    connection.commit()


def create_tables(connection):
    create_users_table(connection)
    create_vinkit_table(connection)


def insert_default_data(connection):
    cursor = connection.cursor()
    sql_users = """INSERT INTO users(id, name, password) VALUES (?,?,?)"""
    cursor.execute(
        sql_users, [next(generator_user_id), "user", "passu"])
    sql_vinkit = """INSERT INTO vinkit(id, name) VALUES (?,?)"""
    cursor.execute(
        sql_vinkit, [next(generator_vinkki_id), "kirja1"])
    connection.commit()


def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)
    insert_default_data(connection)


if __name__ == "__main__":
    initialize_database()
