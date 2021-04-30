import random
import sqlite3

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY KEY, number TEXT UNIQUE, pin TEXT, balance INTEGER DEFAULT 0);")
conn.commit()


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
    cur.execute("INSERT INTO card(number, pin, balance) VALUES (?,?,?);", (cardnumber, inputpin, 0))
    conn.commit()


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
            if len(old_pin) == 1 and old_pin[0] == pin:
                print("You successfully logged in!")
                while 1:
                    print("1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit\n")
                    n1 = int(input())
                    if n1 == 1:
                        balance = cur.execute(f"SELECT balance From card WHERE number = {cardnumber};").fetchone()
                        print("Balance: ", balance[0])
                    elif n1 == 2:
                        print("Enter income:")
                        income = int(input())
                        balance = cur.execute(f"SELECT balance From card WHERE number = {cardnumber};").fetchone()
                        cur.execute(f"UPDATE card SET balance = {income + balance[0]} WHERE number = {cardnumber}")
                        conn.commit()
                        print("Income was added!")
                    elif n1 == 3:
                        print("Transfer\nEnter card number:")
                        cardnumber_to_transfer = input("Enter your card number:")
                        cardnumber1 = cur.execute(
                            f"SELECT number FROM card WHERE number = {cardnumber_to_transfer};").fetchone()
                        if not luhh(cardnumber_to_transfer):
                            print("Probably you made a mistake in the card number. Please try again!")
                        elif type(cardnumber1) == type(None):
                            print("Such a card does not exist.")
                        elif cardnumber == cardnumber_to_transfer:
                            print("You can't transfer money to the same account!")
                        else:
                            print("Enter how much money you want to transfer:")
                            amount_to_transfer = int(input())
                            acc_balance = cur.execute(
                                f"SELECT balance From card WHERE number = {cardnumber};").fetchone()
                            if acc_balance[0] < amount_to_transfer:
                                print("Not enough money!")
                            else:
                                acc_balance3 = cur.execute(
                                    f"SELECT balance From card WHERE number = {cardnumber_to_transfer};").fetchone()
                                cur.execute(
                                    f"UPDATE card SET balance = {acc_balance[0] - amount_to_transfer} WHERE number = {cardnumber}")
                                cur.execute(
                                    f"UPDATE card SET balance = {amount_to_transfer + acc_balance3[0]} WHERE number = {cardnumber_to_transfer}")
                                conn.commit()
                                print("Success!")

                    elif n1 == 4:
                        cur.execute(f"DELETE FROM card WHERE number = {cardnumber};")
                        conn.commit()
                        print("The account has been closed!")
                        return 0
                    elif n1 == 5:
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
