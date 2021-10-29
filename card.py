import sqlite3
from seat import Seat


class Card:
    database = "banking.db"

    def __init__(self, type, number, cvc, holder, price):
        self.price = price
        self.type = type
        self.number = number
        self.cvc = cvc
        self.holder = holder

    def validate(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
            SELECT type,number,cvc,holder FROM Card WHERE "type"=?
        """, [self.type])
        card_details = cursor.fetchall()
        connection.close()
        cardtype = card_details[0][0]
        cardnumber = card_details[0][1]
        cardcvc = card_details[0][2]
        cardholder = card_details[0][3]
        if self.number == cardnumber and self.cvc == cardcvc and self.holder == cardholder:
            return True
        else:
            return False

    def _balance(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
                      SELECT balance FROM Card WHERE "type"=?
                  """, [self.type])
        balance = cursor.fetchall()
        connection.close()
        return float(balance[0][0])

    def balance_available(self):

        balance_parsed = self._balance()
        if balance_parsed - self.price > 0:
            return True
        else:
            return False

    def charge_card(self):
        charge_amount = self._balance() - self.price
        connection = sqlite3.connect(self.database)
        connection.execute("""       
                                UPDATE "Card" SET "balance" = ? WHERE "type" = ?
                                        """, [charge_amount, self.type])
        connection.commit()
        connection.close()


if __name__ == "__main__":

    card = Card(type="visa".capitalize(), number=1234567, cvc=133, holder="John Smith", price=5000.0)
    if card.validate():
        if card.balance_available():
            card.charge_card()
        else:
            print("Not enough money!")
    else:
        print("One of card details entered are invalid")
