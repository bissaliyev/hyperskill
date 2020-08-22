import sqlite3
import random


class BankingSystem:
    def __init__(self):
        self.current_account = None
        self.logged: bool = False

        # init card db
        self.conn = sqlite3.connect('card.s3db')
        self.conn.row_factory = sqlite3.Row
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS card(
                id INTEGER constraint card_pk primary key, 
                number TEXT, 
                pin TEXT, 
                balance INTEGER DEFAULT 0)
            ''')
        self.conn.commit()
        self.cur = self.conn.cursor()

    def clear(self):
        self.logged = False

    def menu(self):
        # print menu
        while True:
            if self.logged and self.current_account is not None:
                print("1. Balance")
                print("2. Add income")
                print("3. Do transfer")
                print("4. Close account")
                print("5. Log out")
            else:
                print("1. Create an account")
                print("2. Log into account")
            print("0. Exit")

            # action
            action = input("")
            if self.logged and self.current_account is not None:
                if action == "1":
                    print("Balance: " + str(self.current_account.get_balance()))
                elif action == "2":
                    self.add_income()
                elif action == "3":
                    self.transfer()
                elif action == "4":
                    self.close_account()
                elif action == "5":
                    self.logout()
                elif action == "0":
                    break
            else:
                if action == "1":
                    self.create_account()
                elif action == "2":
                    self.login()
                else:
                    break

    def create_account(self):
        acc = Account()
        self.cur.execute("INSERT INTO card(number, pin) VALUES(?, ?)", (acc.number, acc.pin))
        self.conn.commit()
        print("Your card has been created")
        print("Your card number:")
        print(acc.number)
        print("Your card PIN:")
        print(acc.pin)

    def login(self):
        number = input("Enter your card number:\n")
        pin = input("Enter your PIN:\n")

        self.cur.execute("SELECT * FROM card WHERE number = ?", (number,))
        data = self.cur.fetchone()
        if data is not None:
            if number == data['number'] and pin == data["pin"]:
                self.current_account = Account(data['number'], data['pin'], data['balance'])
                self.logged = True
                print("You have successfully logged in!")
            else:
                print("Wrong card number or PIN!")
        else:
            print("Wrong card number or PIN!")

    def logout(self):
        self.clear()
        print("You have successfully logged out!")

    def validate_card(self, number):
        r = [int(ch) for ch in str(number)][::-1]
        return (sum(r[0::2]) + sum(sum(divmod(d * 2, 10)) for d in r[1::2])) % 10 == 0

    def add_income(self):
        money = int(input("Enter income:"))
        if self.current_account is not None:
            self.cur.execute("UPDATE card set balance = balance + ? WHERE number = ?",
                             (money, self.current_account.number))
            self.current_account.balance = self.current_account.balance + money
            self.conn.commit()
        print("Income was added!")

    def transfer(self):
        print("Transfer")
        dest_account = input("Enter card number:")
        if not self.validate_card(dest_account):
            print("Probably you made mistake in the card number. Please try again!")
        else:
            self.cur.execute("SELECT * FROM card WHERE number = ?", (dest_account,))
            data = self.cur.fetchone()
            if data is not None:
                money = int(input("Enter how much money you want to transfer:"))
                if self.current_account.balance >= money:
                    self.cur.execute("UPDATE card set balance = balance + ? WHERE number = ?",
                                     (money, dest_account))
                    self.cur.execute("UPDATE card set balance = balance - ? WHERE number = ?",
                                     (money, self.current_account.number))
                    self.current_account.balance = self.current_account.balance - money
                    self.conn.commit()
                    print("Success!")
                else:
                    print("Not enough money!")
            else:
                print("Such a card does not exist.")

    def close_account(self):
        self.cur.execute("DELETE FROM card WHERE number = ?", (self.current_account.number,))
        self.conn.commit()
        self.current_account = None
        self.clear()
        print("The account has been closed!")


class Account:
    def __init__(self, number="", pin="", balance=0):
        if not number:
            self.number = "400000"

            for _ in range(0, 2):
                num = random.randint(0, 99999)  # random number is 143
                num = str(num).zfill(5)  # num is now '0143'
                self.number += num

            r = [int(_) for _ in self.number][:15]
            r = sum(r[1::2]) + sum(sum(divmod(d * 2, 10)) for d in r[0::2])
            checksum = (10 - r % 10) % 10
            self.number = self.number[:15] + str(checksum)

            pin = random.randint(0, 9999)
            pin = str(pin).zfill(4)
            self.pin = pin
        else:
            self.number = number
            self.pin = pin
        self.balance = balance

    def get_balance(self):
        return self.balance

    def add_income(self, money):
        self.balance = self.balance + money


bank = BankingSystem()
bank.menu()
