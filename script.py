import argparse

from recruitementtask.Database import Database
from recruitementtask.Query import Query

DATABASE = "my_sqlite.db"
TABLE = "users1_csv"

db = Database(DATABASE)
ap = argparse.ArgumentParser()
query = Query(db.db_name, TABLE)


def main():
    commands = {
        "create_database": db.create_database(),
        "print-all-accounts": lambda: print(query.get_all_accounts()),
        "print-oldest-account": lambda: print(query.get_oldest_account()),
        "print-children": lambda: [
            print(f"{child['name']}, {child['age']}") for child in query.get_children_by_user(password)
        ],
        "group-by-age": lambda: [print(f"age:{k},\tcount:{v}") for k, v in query.count_children_by_age()],
    }

    ap.add_argument("command", choices=commands.keys(), help="\n".join([f"{cmd}:" for cmd in commands.keys()]))
    ap.add_argument("--login", help="email/phone number")
    ap.add_argument("--password", help="password")

    args = ap.parse_args()
    login = args.login
    password = args.password
    command = args.command

    print(args)
    if command == "create_database":
        db.create_database()
    elif query.check_credentials(login, password):
        if command in commands:
            commands[command]()
        else:
            print(f"Invalid command: {args.command}")
    else:
        print("Invalid Login")


if __name__ == "__main__":
    main()
