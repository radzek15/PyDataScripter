<div align="center">
  <a href="https://github.com/radzek15/Recruitement-task"></a>
  <h1 align="center">Recruitement Task - backend Internship</h1>
  <p align="justify">Python script designed to execute various operations on the given datasets.</p></div>

## Installation:
<div align="justify">

   * Firstly clone the repo:
     * `git clone https://github.com/radzek15/Recruitement-task`
   * Initialize virtual environment and install dependencies:
     * `poetry install && poetry shell`

## Usage:
   * For every command login and password is required:
     - Login: Either email or telephone number
     - Password: password
     - `python script.py <command> --login <login> --password <password>`
   * Create Database: `python script.py create_database`
   * import any data you would like to database `python data_import.py`
     * data will be validated before export according to task requirements but this process can be easily modified

## Tech Stack:
   * Python3
   * pandas
   * Poetry
   * Pre-commit

</div>
