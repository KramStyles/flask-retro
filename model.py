import os

from sqlite3 import connect, Error as Err, dbapi2


class User:
    def __init__(self, user):
        self.user = user
        self.conn = self.cursor = None

    def connect(self):
        try:
            self.conn = connect('/Users/user/Documents/Python/Personal/Flask retro/flask_db.sql', check_same_thread=False)
            self.cursor = self.conn.cursor()
            return 'ok'
        except Err as err:
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
        except (Err, Exception) as err:
            return print(err)
        finally:
            self.close_conn()

    def get_users(self):
        sql = 'SELECT username from users'
        try:
            conn = self.connect()
            if conn == 'ok':
                self.cursor.execute(sql)
                # Pulls out the names from the tuple and appends them individually to a new list
                return [item[0] for item in self.cursor.fetchall()]
            else:
                return "connection error"
        except (Err, Exception) as err:
            return err
        finally:
            self.close_conn()

    def read(self, table='users', conditions='', what='*'):
        self.connect()
        if conditions:
            conditions = 'where ' + conditions
        sql = f"SELECT {what} FROM {table} {conditions};"
        try:
            result = self.cursor.execute(sql)
            msg = result.fetchall()
        except (Exception) as err:
            msg = err
        finally:
            self.close_conn()
            return msg


    def create(self, data, table='users', columns='', testing=False):
        self.connect()
        if columns:
            columns = f"({columns})"
            values = data
        else:
            values = 'null, '
            values += data

        sql = f"""INSERT INTO {table} {columns} VALUES ({values})"""
        try:
            self.cursor.execute(sql)
            if not testing: self.conn.commit()
            msg = 'ok'
        except (Exception) as err:
            msg = err
        finally:
            self.close_conn()
            return msg

    def delete(self, conditions='', table='users'):
        self.connect()
        if conditions:
            conditions = 'where ' + conditions

        sql = f"DELETE FROM {table} {conditions};"
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            msg = 'ok'
        except Exception as err:
            msg = err
        finally:
            self.close_conn()
            return msg

    def authenticate(self, username, password):
        db_pass = self.read(conditions=f"username='{username}'", what='password')[0][0]
        return password == db_pass

    def check_user_exists(self):
        all_users = self.get_users()
        return self.user in all_users


if __name__ == '__main__':
    profile = User('karm')
    print(profile.get_users())

