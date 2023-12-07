import argparse

from recruitementtask.Database import Database
from recruitementtask.Query import Query

db = Database("my_sqlite.db")
ap = argparse.ArgumentParser()
TABLE = "users1_csv"
query = Query("my_sqlite.db")


def main():
    ap.add_argument("command", help="create SQLite database")
    ap.add_argument("--login", required=True, help="email/phone number")
    ap.add_argument("--password", required=True, help="password")

    args = ap.parse_args()
    login = args.login
    password = args.password
    command = args.command

    commands = {
        "create_database": db.create_database,
        "print-all-accounts": lambda: print(query.get_all_accounts(TABLE)),
        "print-oldest-account": lambda: print(query.get_oldest_account(TABLE)),
    }

    print(args)
    if query.check_credentials("users1_csv", login, password):
        if command in commands:
            commands[command]()
        else:
            print(f"Invalid command: {args.command}")
    else:
        print("Invalid Login")


if __name__ == "__main__":
    main()
