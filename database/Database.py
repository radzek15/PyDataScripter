import sqlite3
from typing import Iterable

import pandas as pd

from database.DataTransformer import DataTransformer
from database.EntryValidator import EntryValidator


class Database:
    def __init__(self, db_path: str, db_name: str):
        self.db_path = db_path
        self.db_name = db_name

    def create_database(self) -> None:
        db = None
        try:
            db = sqlite3.connect(self.db_name)
            print(f"database: {self.db_name} created successfully.")
        except sqlite3.Error as e:
            print(e)
        finally:
            if db:
                db.close()

    def create_table(self, table_name: str, columns: Iterable[str]) -> None:
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

    def insert_row(self, table_name: str, columns: Iterable[str], values: Iterable[str]) -> None:
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

    def import_data(self) -> None:
        df1_csv = pd.read_csv(f"{self.db_path}a/b/users_1.csv", sep=";")
        df2_csv = pd.read_csv(f"{self.db_path}a/c/users_2.csv", sep=";")
        df_json = pd.read_json(f"{self.db_path}a/users.json")
        df1_xml = DataTransformer.transform_xml_to_json(f"{self.db_path}a/b/users_1.xml")
        df2_xml = DataTransformer.transform_xml_to_json(f"{self.db_path}users_2.xml")

        # Transform children column to json format
        df1_csv = DataTransformer.transform_children_csv(df1_csv)
        df2_csv = DataTransformer.transform_children_csv(df2_csv)

        # Serialize children column
        df1_csv = DataTransformer.json_serializer(df1_csv)
        df2_csv = DataTransformer.json_serializer(df2_csv)
        df_json = DataTransformer.json_serializer(df_json)
        df1_xml = DataTransformer.json_serializer(df1_xml)
        df2_xml = DataTransformer.json_serializer(df2_xml)

        # merge dataframes and standardize data type
        merged = pd.concat([df1_csv, df2_csv, df_json, df1_xml, df2_xml])
        merged["created_at"] = merged["created_at"].astype(str)

        # validation
        merged = EntryValidator.validate_email(merged)
        merged = EntryValidator.exclude_null(merged, "telephone_number")
        merged = EntryValidator.standardize_phone_number(merged)

        # Remove duplicates(email, phone)
        merged = EntryValidator.remove_duplicates(merged, "email")
        merged = EntryValidator.remove_duplicates(merged, "telephone_number")

        # reapply index
        merged = merged.reset_index(drop=True)

        # Export data to SQLite db
        try:
            conn = sqlite3.connect("my_sqlite.db")
            merged.to_sql("users", conn, if_exists="replace")
            print("Data imported properly")
        except sqlite3.Error as e:
            print(e)
        finally:
            if conn:
                conn.commit()
                conn.close()

    def __str__(self) -> str:
        return self.db_name
