
# GST Calculator with Python and MySQL
A Simple GST Calculator system made with Python and MySQL Database.
The Code uses PyMySQL Python Library to function. This code has a very simple syntax which makes it easy to understand and beginner friendly.


## Install the required Libraries.

Clone the project

```
pip install pymysql
```
or
```
python -m pip install pymysql
```

## Initialize the database
- Create the Database:
  
  ```
  CREATE DATABASE GSTCALC;
  USE GSTCALC;
  ```
- Create table and alter it:
- Table will be automatically created when running the script for first time.
  
  ```
  ALTER TABLE transactions
  ADD COLUMN vendor_address VARCHAR(255) NOT NULL AFTER vendor_name;
  ```

## Authors

- [@sidharth_everett](https://github.com/Cyber-Zypher)
