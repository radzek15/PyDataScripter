import argparse

from recruitementtask.Database import Database
from recruitementtask.Query import Query

DATABASE = "my_sqlite.db"
TABLE = "users1_csv"

db = Database(DATABASE)
ap = argparse.ArgumentParser()
query = Query(db.db_name)


def main():
    ap.add_argument("command", help="create SQLite database")
    ap.add_argument("--login", help="email/phone number")
    ap.add_argument("--password", help="password")

    args = ap.parse_args()
    login = args.login
    password = args.password
    command = args.command

    commands = {
        "print-all-accounts": lambda: print(query.get_all_accounts(TABLE)),
        "print-oldest-account": lambda: print(query.get_oldest_account(TABLE)),
        "print-children": lambda: [
            print(f"{child['name']}, {child['age']}") for child in query.get_children_by_user(TABLE, password)
        ],
    }

    print(args)
    if command == "create_database":
        db.create_database()
    elif query.check_credentials("users1_csv", login, password):
        if command in commands:
            commands[command]()
        else:
            print(f"Invalid command: {args.command}")
    else:
        print("Invalid Login")


if __name__ == "__main__":
    main()
