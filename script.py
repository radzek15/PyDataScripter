import sys

from recruitementtask.Database import Database

db = Database("my_sqlite.db")
columns = [
    "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE",
    "firstname TEXT NOT NULL",
    "telephone_number INTEGER NOT NULL UNIQUE CHECK(length(telephone_number) = 9)",
    "email TEXT NOT NULL UNIQUE",
    "password TEXT NOT NULL",
    'role TEXT NOT NULL CHECK(role IN ("admin", "user"))',
    'created_at TEXT NOT NULL CHECK(created_at LIKE "____-__-__ __:__:__")',
    "children TEXT",
]

cols_for_insert = [columns[columns.index(i)].split()[0] for i in columns]


def main():
    command = sys.argv[1]

    if command == "create_database":
        db.create_database()
        db.create_table("users", columns)
    else:
        print(f"Invalid command: {command}")


if __name__ == "__main__":
    main()
