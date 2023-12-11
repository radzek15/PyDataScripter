import json
import sqlite3
from typing import Any, Union

from .Database import Database


class Query(Database):
    def __init__(self, db_name: str, table_name: str):
        super().__init__(db_name)
        self.table_name = table_name

    def check_credentials(self, login: str, password: str) -> bool:
        conn = sqlite3.connect(self.db_name)
        try:
            c = conn.cursor()
            c.execute(
                f"SELECT * FROM {self.table_name} WHERE (email = ? OR telephone_number = ?) AND password = ?",
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

    def get_all_accounts(self) -> Any:
        conn = sqlite3.connect(self.db_name)
        try:
            c = conn.cursor()
            c.execute(f"SELECT COUNT(*) FROM {self.table_name}")
            sum_of_accounts = c.fetchall()
            return sum_of_accounts[0][0]
        except sqlite3.Error as e:
            print(e)
            return -1
        finally:
            if conn:
                conn.close()

    def get_oldest_account(self) -> str:
        conn = sqlite3.connect(self.db_name)
        try:
            c = conn.cursor()
            c.execute(f"SELECT firstname, email, created_at FROM {self.table_name} ORDER BY created_at")
            oldest_acc = c.fetchone()
            return f"""name: {oldest_acc[0]}\nemail_address: {oldest_acc[1]}\ncreated_at: {oldest_acc[2]}"""
        except sqlite3.Error as e:
            print(e)
            return ""
        finally:
            if conn:
                conn.close()

    def count_children_by_age(self) -> list[tuple[int, int]]:
        conn = sqlite3.connect(self.db_name)
        try:
            c = conn.cursor()
            c.execute(f"SELECT children FROM {self.table_name} WHERE LENGTH(children) > 2")
            children = c.fetchall()
            age_groups = {}
            for i in range(len(children)):
                for j in json.loads(children[i][0]):
                    age_groups[j["age"]] = age_groups.get(j["age"], 0) + 1
            return sorted(age_groups.items(), key=lambda x: x[0])
        except sqlite3.Error as e:
            print(e)
            return []
        finally:
            if conn:
                conn.close()

    def get_children_by_user(self, login: str) -> list[dict[str, Union[str, int]]]:
        conn = sqlite3.connect(self.db_name)
        try:
            c = conn.cursor()
            c.execute(
                f"SELECT children FROM {self.table_name} WHERE (email = ? OR telephone_number = ?)", (login, login)
            )
            children = c.fetchone()
            return json.loads(children[0])
        except sqlite3.Error as e:
            print(e)
            return []
        finally:
            if conn:
                conn.close()

    def get_similar_children_by_age(self, login: str, table_name) -> set[str]:
        user_children = self.get_children_by_user(login)
        conn = sqlite3.connect(self.db_name)
        try:
            c = conn.cursor()
            c.execute(
                f"SELECT firstname, telephone_number, email, children FROM {table_name} WHERE LENGTH(children) > 2"
            )
            rows = c.fetchall()
            rows = [[p, t, e, json.loads(i)] for p, t, e, i in rows]

            # Finding matching rows excluding the user
            data = [
                [p, t, c]
                for i in user_children
                for p, t, e, c in rows
                for j in c
                if i["age"] == j["age"] and t != login and e != login
            ]

            # Change elements types with f-string to exclude repetition using set
            formatted_data = {
                f"{item[0]} , {item[1]}: " + "; ".join([f"{child['name']}, {child['age']}" for child in item[2]])
                for item in data
            }
            return formatted_data
        except sqlite3.Error as e:
            print(e)
            return set()
        finally:
            if conn:
                conn.close()

    def __str__(self):
        return f"Database {self.db_name} query for {self.table_name}"
