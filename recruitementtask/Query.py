import sqlite3

from .Database import Database


class Query(Database):
    def check_credentials(self, table_name: str, login: str, password: str) -> bool:
        conn = sqlite3.connect(self.db_name)
        try:
            c = conn.cursor()
            c.execute(
                f"SELECT * FROM {table_name} WHERE (email = ? OR telephone_number = ?) AND password = ?",
                (login, login, password),
            )
            credentials = c.fetchone()
            return True if credentials else False
        except sqlite3.Error as e:
            print(e)
            return False
        finally:
            if conn:
                conn.close()

    def get_all_accounts(self, table_name: str) -> int:
        conn = sqlite3.connect(self.db_name)
        try:
            c = conn.cursor()
            c.execute(f"SELECT COUNT(*) FROM {table_name}")
            sum_of_accounts = c.fetchall()
            return sum_of_accounts[0][0]
        except sqlite3.Error as e:
            print(e)
            return -1
        finally:
            if conn:
                conn.close()

    def get_oldest_account(self, table_name: str) -> str:
        conn = sqlite3.connect(self.db_name)
        try:
            c = conn.cursor()
            c.execute(f"SELECT firstname, email, created_at FROM {table_name} ORDER BY created_at")
            oldest_acc = c.fetchone()
            return f"""name: {oldest_acc[0]}\nemail_address: {oldest_acc[1]}\ncreated_at: {oldest_acc[2]}"""
        except sqlite3.Error as e:
            print(e)
            return ""
        finally:
            if conn:
                conn.close()

    def get_childrens(self, table_name: str):
        pass

    def __str__(self):
        return f"Database {self.db_name} query"
