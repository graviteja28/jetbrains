'''
Stage 2-4: Luhn algorithm
Description
In this stage, we will find out what the purpose of the checksum is and what the Luhn algorithm is used for.

The main purpose of the check digit is to verify that the card number is valid. Say you're buying something online, and you type in your credit card number incorrectly by accidentally swapping two digits, which is one of the most common errors. When the website looks at the number you've entered and applies the Luhn algorithm to the first 15 digits, the result won't match the 16th digit on the number you entered. The computer knows the number is invalid, and it knows the number will be rejected if it tries to submit the purchase for approval, so you're asked to re-enter the number. Another purpose of the check digit is to catch clumsy attempts to create fake credit card numbers. Those who are familiar with the Luhn algorithm, however, could get past this particular security measure.

Luhn Algorithm in action

The Luhn algorithm is used to validate a credit card number or other identifying numbers, such as Social Security. The Luhn algorithm, also called the Luhn formula or modulus 10, checks the sum of the digits in the card number and checks whether the sum matches the expected result or if there is an error in the number sequence. After working through the algorithm, if the total modulus 10 equals zero, then the number is valid according to the Luhn method.

While the algorithm can be used to verify other identification numbers, it is usually associated with credit card verification. The algorithm works for all major credit cards.

Here is how it works for a credit card with the number 4000008449433403:



If the received number is divisible by 10 with the remainder equal to zero, then this number is valid; otherwise, the card number is not valid. When registering in your banking system, you should generate cards with numbers that are checked by the Luhn algorithm. You know how to check the card for validity. But how do you generate a card number so that it passes the validation test? It's very simple!

First, we need to generate an Account Identifier, which is unique to each card. Then we need to assign the Account Identifier to our BIN (Bank Identification Number). As a result, we get a 15-digit number 400000844943340, so we only have to generate the last digit, which is a checksum.

To find the checksum, it is necessary to find the control number for 400000844943340 by the Luhn algorithm. It equals 57 (from the example above). The final check digit of the generated map is 57+X, where X is checksum. In order for the final card number to pass the validity check, the check number must be a multiple of 10, so 57+X must be a multiple of 10. The only number that satisfies this condition is 3.

Therefore, the checksum is 3. So the total number of the generated card is 4000008449433403. The received card is checked by the Luhn algorithm.

You need to change the credit card generation algorithm so that they pass the Luhn algorithm.

Objectives
You should allow customers to create a new account in our banking system.

Once the program starts you should print the menu:

1. Create an account
2. Log into the account
0. Exit

If the customer chooses ‘Create an account’, you should generate a new card number that satisfies all the conditions described above. Then you should generate a PIN code that belongs to the generated card number. PIN is a sequence of 4 digits; it should be generated in the range from 0000 to 9999.

If the customer chooses ‘Log into account’, you should ask to enter card information.

After the information has been entered correctly, you should allow the user to check the account balance; after creating the account, the balance should be 0. It should also be possible to log out of the account and exit the program.

Example
The symbol > represents the user input. Notice that it's not a part of the input.

1. Create an account
2. Log into account
0. Exit
>1

Your card has been created
Your card number:
4000004938320896
Your card PIN:
6826

1. Create an account
2. Log into account
0. Exit
>2

Enter your card number:
>4000004938320896
Enter your PIN:
>4444

Wrong card number or PIN!

1. Create an account
2. Log into account
0. Exit
>2

Enter your card number:
>4000004938320896
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
