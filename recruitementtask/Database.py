import sqlite3
from typing import Union

import pandas as pd

from recruitementtask.DataTransformer import DataTransformer
from recruitementtask.EntryValidator import EntryValidator


class Database:
    def __init__(self, db_name: str):
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

    def create_table(self, table_name: str, columns: list[Union[str, int]]) -> None:
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

    def insert_row(self, table_name: str, columns: list[Union[str, int]], values: list[Union[str, int]]) -> None:
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

    @staticmethod
    def import_data():
        df1_csv = pd.read_csv("recruitement-task-backend-internship-main-data/data/a/b/users_1.csv", sep=";")
        df2_csv = pd.read_csv("recruitement-task-backend-internship-main-data/data/a/c/users_2.csv", sep=";")
        df_json = pd.read_json("recruitement-task-backend-internship-main-data/data/a/users.json")
        df1_xml = DataTransformer.transform_xml_to_json(
            "recruitement-task-backend-internship-main-data/data/a/b/users_1.xml"
        )
        df2_xml = DataTransformer.transform_xml_to_json(
            "recruitement-task-backend-internship-main-data/data/users_2.xml"
        )

        # validate email
        df1_csv = EntryValidator.validate_email(df1_csv)
        df2_csv = EntryValidator.validate_email(df2_csv)
        df_json = EntryValidator.validate_email(df_json)
        df1_xml = EntryValidator.validate_email(df1_xml)
        df2_xml = EntryValidator.validate_email(df2_xml)

        # Remove rows with empty phone numbers
        df1_csv = EntryValidator.exclude_null(df1_csv, "telephone_number")
        df2_csv = EntryValidator.exclude_null(df2_csv, "telephone_number")
        df_json = EntryValidator.exclude_null(df_json, "telephone_number")
        df1_xml = EntryValidator.exclude_null(df1_xml, "telephone_number")
        df2_xml = EntryValidator.exclude_null(df2_xml, "telephone_number")

        # Remove duplicates(email, phone)
        df1_csv = EntryValidator.remove_duplicates(df1_csv, "email")
        df1_csv = EntryValidator.remove_duplicates(df1_csv, "telephone_number")
        df2_csv = EntryValidator.remove_duplicates(df2_csv, "email")
        df2_csv = EntryValidator.remove_duplicates(df2_csv, "telephone_number")
        df_json = EntryValidator.remove_duplicates(df_json, "email")
        df_json = EntryValidator.remove_duplicates(df_json, "telephone_number")
        df1_xml = EntryValidator.remove_duplicates(df1_xml, "email")
        df1_xml = EntryValidator.remove_duplicates(df1_xml, "telephone_number")
        df2_xml = EntryValidator.remove_duplicates(df2_xml, "email")
        df2_xml = EntryValidator.remove_duplicates(df2_xml, "telephone_number")

        # Standardize phone
        df1_csv = EntryValidator.standardize_phone_number(df1_csv)
        df2_csv = EntryValidator.standardize_phone_number(df2_csv)
        df_json = EntryValidator.standardize_phone_number(df_json)
        df1_xml = EntryValidator.standardize_phone_number(df1_xml)
        df2_xml = EntryValidator.standardize_phone_number(df2_xml)

        # Transform children column to json format
        df1_csv = DataTransformer.transform_children_csv(df1_csv)
        df2_csv = DataTransformer.transform_children_csv(df2_csv)

        # Serialize children column
        df1_csv = DataTransformer.json_serializer(df1_csv)
        df2_csv = DataTransformer.json_serializer(df2_csv)
        df_json = DataTransformer.json_serializer(df_json)
        df1_xml = DataTransformer.json_serializer(df1_xml)
        df2_xml = DataTransformer.json_serializer(df2_xml)

        # Export data to SQLite db
        try:
            conn = sqlite3.connect("my_sqlite.db")
            df1_csv.to_sql("users1_csv", conn, if_exists="replace")
            df2_csv.to_sql("users2_csv", conn, if_exists="replace")
            df_json.to_sql("users_json", conn, if_exists="replace")
            df1_xml.to_sql("users1_xml", conn, if_exists="replace")
            df2_xml.to_sql("users2_xml", conn, if_exists="replace")
            print("Data imported properly")
        except sqlite3.Error as e:
            print(e)
        finally:
            if conn:
                conn.commit()
                conn.close()

    def __str__(self):
        return self.db_name
