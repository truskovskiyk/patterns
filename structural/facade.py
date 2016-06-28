class SkiRent(object):

    def rent_boots(self, feet_size, skier_lever):
        return 20

    def rent_ski(self, weight, skier_level):
        return 40

    def rent_pole(self, height):
        return 5

class SkiTicket(object):

    def by_one_day_ticket(self):
        return 115

    def by_half_day_ticker(self):
        return 60

class SkiRoom(object):

    def book_room(self, room_quality):
        if room_quality == 3:
            return 250
        elif room_quality == 4:
            return 500
        elif room_quality == 5:
            return 900
        else:
            raise ValueError(
                    "room_quality should be in range [3:5]")

class SkiFacade(object):

    def __init__(self):
        self.ski_rent = SkiRent()
        self.ski_ticket = SkiTicket()
        self.ski_room = SkiRoom()

    def have_good_rest(self, height, weight, feer_size, skier_level,
                        room_quality):

        ski_price = self.ski_rent.rent_ski(weight, skier_level)
        ski_boots_price = self.ski_rent.rent_boots(feer_size, skier_level)
        ski_pole_price = self.ski_rent.rent_pole(height)

        one_day_ticket_price = self.ski_ticket.by_one_day_ticket()

        hotel_price = self.ski_room.book_room(room_quality)

        return (ski_price + ski_boots_price + ski_pole_price +
                    one_day_ticket_price + hotel_price)

if __name__ == '__main__':
    ski_facade = SkiFacade()
    print(ski_facade.have_good_rest(height=185, weight=95, feer_size=43,
                        skier_level=5, room_quality=5))

    print(ski_facade.have_good_rest(height=185, weight=95, feer_size=43,
                        skier_level=5, room_quality=-1))
