'''
Stage 3-4: I'm so lite
Description
It's very upsetting when the data about registered users disappears after the program is completed. To avoid this problem, you need to create a database where you will store all the necessary information about the created credit cards. We will use SQLite to create the database.

SQLite is a database engine. It is a software that allows users to interact with a relational database. In SQLite, a database is stored in a single file — a trait that distinguishes it from other database engines. This allows for greater accessibility: copying a database is no more complicated than copying the file that stores the data, and sharing a database implies just sending an email attachment.

You can use the sqlite3 module to manage SQLite database from Python. You don't need to install this module. It is included in the standard library.

To use the module, you must first create a Connection object that represents the database. Here the data will be stored in the example.s3db file:

import sqlite3
conn = sqlite3.connect('example.s3db')
Once you have a Connection, you can create a Cursor object and call its execute() method to perform SQL queries:

cur = conn.cursor()

# Executes some SQL query
cur.execute('SOME SQL QUERY')

# After doing some changes in DB don't forget to commit them!
conn.commit()
To get data returned by SELECT query you can use fetchone(), fetchall() methods:

cur.execute('SOME SELECT QUERY')

# Returns the first row from the response
cur.fetchone()

# Returns all rows from the response
cur.fetchall()
Objectives
In this stage, create a database named card.s3db with a table titled card. It should have the following columns:

id INTEGER
number TEXT
pin TEXT
balance INTEGER DEFAULT 0
Pay attention: your database file should be created when the program starts if it hasn’t yet been created. And all created cards should be stored in the database from now.

Do not forget to commit your DB changes right after executing a query!
Example
The symbol > represents the user input. Notice that it's not a part of the input.

1. Create an account
2. Log into account
0. Exit
>1

Your card has been created
Your card number:
4000003429795087
Your card PIN:
6826

1. Create an account
2. Log into account
0. Exit
>2

Enter your card number:
>4000003429795087
Enter your PIN:
>4444

Wrong card number or PIN!

1. Create an account
2. Log into account
0. Exit
>2

Enter your card number:
>4000003429795087
Enter your PIN:
>6826

You have successfully logged in!

1. Balance
2. Log out
0. Exit
>1

Balance: 0

1. Balance
2. Log out
0. Exit
>2

You have successfully logged out!

1. Create an account
2. Log into account
0. Exit
>0

Bye!
'''

import random
import sqlite3
conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY KEY, number TEXT UNIQUE, pin TEXT, balance INTEGER DEFAULT 0);")
conn.commit()
account = {}


def main():
    while 1:
        n = int(input("1. create an account\n" + "2. Log into account\n" + "0. Exit\n"))
        if n == 1:
            createaccount()
        elif n == 2:
            r = logintoaccount()
            if r == 2:
                break
        elif n == 0:
            print("Bye!")
            break


def luhh(cardnumber):
    l = list(cardnumber)
    s = int(l[-1])
    for i in range(0, 15):
        if i % 2 == 0:
            if int(l[i]) * 2 > 9:
                s = s + (int(l[i]) * 2) - 9
            else:
                s += int(l[i]) * 2
        else:
            s += int(l[i])
    if s % 10 == 0:
        return True
    else:
        return False


def createaccount():
    while True:
        inputpin = random.randint(1000, 10000)
        y = random.randint(10 ** 9, 10 ** 10)
        cardnumber = str(400000) + str(y)
        if luhh(cardnumber):
            break

    print("Your card has been created")
    print("Your card number")
    print(cardnumber)
    print("Your card pin")
    print(inputpin)
    cur.execute("INSERT INTO card(number, pin, balance) VALUES (?,?,?);",(cardnumber, inputpin, 0))
    conn.commit()
    account[cardnumber] = inputpin


def logintoaccount():
    x1 = 1
    while x1 != 0:
        cardnumber = input("Enter your card number:")
        pin = input("Enter your PIN")
        if len(cardnumber) == 16:
            old_pin = cur.execute(f"SELECT pin FROM card WHERE number = {cardnumber} And pin = {pin};").fetchone()
            if type(old_pin) == type(None):
                print("Wrong card number or PIN!")
                return 0
            if  len(old_pin) == 1 and old_pin[0] == pin:
                print("You successfully logged in!")
                while 1:
                    print("1. Balance\n" + "2. Log out\n" + "0. Exit\n")
                    n1 = int(input())
                    if n1 == 1:
                        print("Balance: 0")
                        return 0
                    elif n1 == 2:
                        print("You have successfully logged out!")
                        return 0
                    elif n1 == 0:
                        print("Bye!")
                        return 2
            else:
                print("Wrong card number or PIN!")
                return 0
        else:
            print("Wrong card number or PIN!")
            return 0


main()
