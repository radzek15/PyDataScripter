import sqlite3

import pandas as pd

DATA_PATH = "../recruitement-task-backend-internship-main-data/data/"
conn = sqlite3.connect("../my_sqlite.db")

users_1_csv = pd.read_csv(DATA_PATH + "a/b/users_1.csv")
users_2_csv = pd.read_csv(DATA_PATH + "a/c/users_2.csv")
