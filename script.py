import sys

from recruitementtask.Database import Database

db = Database("my_sqlite.db")


def main():
    command = sys.argv[1]

    if command == "create_database":
        db.create_database()
    else:
        print(f"Invalid command: {command}")


if __name__ == "__main__":
    main()
