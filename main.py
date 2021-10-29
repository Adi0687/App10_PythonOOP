# Title: Cinema Ticket Booking
# Description: An app where a user can book a cinema seat
# if the seat is free and if the user has balance in their card.
# The app generates a PDF ticket if the purchase is successful.
# Objects: User, Seat, Card, Ticket
from card import Card
from seat import Seat


class User:

    def __init__(self, name):
        self.name = name

    def buy(self, seat, card):

        if seat.is_free():
            seat.occupy()
        else:
            print("Sorry the Seat is unavailable or Occupied")

        if card.validate():
            if card.balance_available():
                card.charge_card()
            else:
                print("Not enough money!")
        else:
            print("One of card details entered are invalid")


class Ticket:

    def __init__(self, id, user, price, seat):
        self.id = id
        self.user = user
        self.price = price
        self.seat = seat

    def to_pdf(self, path):
        pass


name = input("Please Type in Your Full Name: ")
seatnumber = input("Whats your Preferred seat Number: ")
cardtype = input("Whats your Card Type (Visa or Mastercard): ")
cardnumber = input("Whats your Card Number: ")
cvcnumber = input("Whats your CVC: ")
cardname = input("Whats the Card Holders Name: ")

user = User(name=name)
seat = Seat(seat_id=seatnumber)
card = Card(type=cardtype, number=cardnumber, cvc=cvcnumber, holder=cardname,price=seat.price())

user.buy(seat=seat, card=card)





