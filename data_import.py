import sqlite3

import pandas as pd

from recruitementtask.EntryValidator import EntryValidator


def main():
    df1_csv = pd.read_csv("recruitement-task-backend-internship-main-data/data/a/b/users_1.csv", sep=";")
    df2_csv = pd.read_csv("recruitement-task-backend-internship-main-data/data/a/c/users_2.csv", sep=";")
    # df_json = pd.read_json("recruitement-task-backend-internship-main-data/data/a/users.json")

    # validate email
    df1_csv = EntryValidator.validate_email(df1_csv)
    df2_csv = EntryValidator.validate_email(df2_csv)

    # Remove rows with empty phone numbers
    df1_csv = EntryValidator.exclude_null(df1_csv, "telephone_number")
    df2_csv = EntryValidator.exclude_null(df2_csv, "telephone_number")

    # Remove duplicates(email, phone)
    df1_csv = EntryValidator.remove_duplicates(df1_csv, "email")
    df1_csv = EntryValidator.remove_duplicates(df1_csv, "telephone_number")
    df2_csv = EntryValidator.remove_duplicates(df2_csv, "email")
    df2_csv = EntryValidator.remove_duplicates(df2_csv, "telephone_number")

    # Standardize phone
    df1_csv = EntryValidator.standardize_phone_number(df1_csv)
    df2_csv = EntryValidator.standardize_phone_number(df2_csv)

    # Export data to SQLite db
    conn = sqlite3.connect("my_sqlite.db")
    df1_csv.to_sql("users1_csv", conn, if_exists="replace")
    df2_csv.to_sql("users2_csv", conn, if_exists="replace")


if __name__ == "__main__":
    main()
