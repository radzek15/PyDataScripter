import sqlite3


class Database:
    def __init__(self, db_name):
        self.db_name = db_name

    def create_database(self):
        db = None
        try:
            db = sqlite3.connect(self.db_name)
            print(f"database: {self.db_name} created successfully.")
        except sqlite3.Error as e:
            print(e)
        finally:
            if db:
                db.close()

    def create_table(self, table_name, columns):
        conn = sqlite3.connect(self.db_name)
        try:
            c = conn.cursor()
            columns_str = ", ".join(columns)
            c.execute(f"CREATE TABLE {table_name} ({columns_str})")
            print(f"Table {table_name} created successfully.")
        except sqlite3.Error as e:
            print(e)
        finally:
            if conn:
                conn.commit()
                conn.close()

    def insert_row(self, table_name, columns, values):
        conn = sqlite3.connect(self.db_name)
        try:
            c = conn.cursor()
            columns_str = ", ".join(columns)
            c.execute(f"INSERT INTO {table_name}({columns_str}) VALUES ({values})")
            print("row inserted successfully")
        except sqlite3.Error as e:
            print(e)
        finally:
            if conn:
                conn.commit()
                conn.close()

    def check_credentials(self, login, password):
        conn = sqlite3.connect(self.db_name)
        try:
            c = conn.cursor()
            c.execute(
                "SELECT * FROM users1_csv WHERE (email = ? OR telephone_number = ?) AND password = ?",
                (login, login, password),
            )
            credentials = c.fetchone()
            return True if credentials else False
        except sqlite3.Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

    def __str__(self):
        return self.db_name
