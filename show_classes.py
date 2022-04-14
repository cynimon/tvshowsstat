import db_func as df
import sql_queries as sqql
import operation_funcs as of
import datetime as dt


class Show:
    def __init__(self, name, episodes, length, start_year, end_year, status, genre):
        self.name = name.title()
        self.episodes = int(episodes)
        self.length = dt.timedelta(minutes=int(length))
        self.start_year = start_year
        self.end_year = end_year
        self.genre = int(genre)
        self.status = status.lower()

    def new_show_corrections(self):
        if self.status == 'д':
            self.status = False
        else:
            self.status = True

    def create_show(self):
        self.new_show_corrections()
        data = (self.name, self.episodes, self.length, self.start_year, self.end_year, self.genre, self.status)
        df.execute_query(of.conn, sqql.insert_new_episodes, data)
