<div align="center">
  <a href="https://github.com/radzek15/Recruitement-task"></a>
  <h1 align="center">Recruitement Task - backend Internship</h1>
  <p align="justify">Python script designed to execute various operations on the given datasets.</p></div>

## Features:

| Feature              | Description                                                                                                                                                                                                                                                                                                                     |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Easy usage           | <p align="justify">The script is designed for easy usage, employing the argparse library to provide a user-friendly command-line interface. This allows users to interact with the script and its functionalities using intuitive commands and options.</p>                                                                     |
| SQLite Database      | <p align="justify">The script facilitates various operations on a SQLite database, leveraging the sqlite3 library. It enables users to create, import data into, and perform other database operations using the powerful capabilities of SQLite.</p>                                                                           |
| Data Export          | <p align="justify">Data export functionality is seamlessly integrated into the script, utilizing the Pandas library. This allows for easy reformatting and exporting of data, providing users with the flexibility to manipulate and export data in various formats as per their requirements.</p>                              |
| OOP and PEP8         | <p align="justify">The script is developed following Object-Oriented Programming (OOP) principles, promoting modularity, reusability, and maintainability of code. Additionally, the script adheres to the PEP8 coding style guidelines, ensuring clean, readable, and consistent code that is in line with best practices.</p> |
| Tests and validation | <p align="justify"></p>                                                                                                                                                                                                                                                                                                         |

## Installation:


   * Firstly clone the repo:
     * `git clone https://github.com/radzek15/Recruitement-task`
   * Initialize virtual environment and install dependencies:
     * `poetry install && poetry shell`

## Usage:
   * For every command login and password is required:
     - Login: Either email or telephone number
     - Password: password
     - `python script.py <command> --login <login> --password <password>`
       - **Notice** Remember about escape symbol "\\" when typing special characters in email/password
   * Create Database: `python script.py create_database`
     ![create-db.png](static%2Fcreate-db.png)
   * import data to database `python script.py import-data`
     * data will be validated before export according to task requirements but this process can be easily modified
     ![import-data.png](static%2Fimport-data.png)
   * Print All Accounts: `python script.py print-all-accounts`
     ![print_accounts.png](static%2Fprint_accounts.png)
   * Print Oldest Account: `python script.py print-oldest-account`
     ![print-oldest.png](static%2Fprint-oldest.png)
   * Print Children: `python script.py print-children`
     ![print-children.png](static%2Fprint-children.png)
   * Group Children by Age: `python script.py group-by-age`
     ![group-age.png](static%2Fgroup-age.png)
   * Find users with Children of the same age: `python script.py find-similar-children-by-age`
     ![find-similar.png](static%2Ffind-similar.png)

## Tech Stack:
   * Python3
   * Pandas
   * SQLite
   * Poetry
   * Pre-commit

## Author:
   * **Radomir Piątkowski**
