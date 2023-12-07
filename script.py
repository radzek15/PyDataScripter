import argparse

from recruitementtask.Database import Database

db = Database("my_sqlite.db")
ap = argparse.ArgumentParser()


def main():
    ap.add_argument("command", help="create SQLite database")
    ap.add_argument("--login", required=True, help="email/phone number")
    ap.add_argument("--password", required=True, help="password")

    args = ap.parse_args()

    login = args.login
    password = args.password

    print(args)
    if db.check_credentials(login, password):
        if args.command == "create_database":
            db.create_database()
        else:
            print(f"Invalid command: {args.command}")
    else:
        print("Login and/or password are incorrect. Please try again")


if __name__ == "__main__":
    main()
