import sqlite3


class Seat:
    database = "cinema.db"

    def __init__(self, seat_id):
        self.seat_id = seat_id

    def price(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""       
        SELECT price FROM Seat WHERE "seat_id" = ?
                """, [self.seat_id])
        pricelist = cursor.fetchall()
        result = float(pricelist[0][0])
        connection.close()
        return result

    def is_free(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""       
                SELECT taken FROM Seat WHERE "seat_id" = ?
                        """, [self.seat_id])
        free = cursor.fetchall()
        connection.close()
        result = float(free[0][0])
        if result == 0:
            return True
        else:
            return "Seat is already Booked, please try another seat"

    def occupy(self):
        connection = sqlite3.connect(self.database)
        connection.execute("""       
                        UPDATE "Seat" SET "taken" = 1 WHERE "seat_id" = ?
                                """, [self.seat_id])
        connection.commit()
        connection.close()


# seat = Seat(seat_id="A3")
# print(seat.price(), seat.is_free())
# if seat.is_free():
#     seat.occupy()
# else:
#     print("Sorry the Seat is unavailable or Occupied")