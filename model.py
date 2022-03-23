import os

from sqlite3 import connect, Error


class User:
    def __init__(self, user):
        self.user = user
        self.conn = self.cursor = None

    def connect(self):
        try:
            self.conn = connect('/Users/user/Documents/Python/Personal/Flask retro/flask_db.sql', check_same_thread=False)
            self.cursor = self.conn.cursor()
            return 'ok'
        except Error as err:
            return err

    def close_conn(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def get_fav_color(self):
        sql = f"""SELECT fav_color FROM users where username = '{self.user}' ORDER BY id DESC """
        try:
            single_connect = self.connect()
            if single_connect == 'ok':
                self.cursor.execute(sql)
                color = self.cursor.fetchone()[0]
                return f"User: {self.user}'s Favorite color is {color}"
            else:
                return single_connect
        except (Error, Exception) as err:
            return print(err)
        finally:
            self.close_conn()


if __name__ == '__main__':
    profile = User('karm')
    profile.get_fav_color()
