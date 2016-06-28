import copy
from datetime import datetime
from collections import namedtuple

Priority = namedtuple('Priority', 'high, low, medium')
APPPriority = Priority('high', 'low', 'medium')


class CalendarPrototype(object):

    def clone_all(self):
        return copy.deepcopy(self)

class CalendarEvent(CalendarPrototype):

    def __init__(self):
        self.attendees = []
        self.priority = None
        self.start_date_and_time = None

    def __str__(self):
        msg = "hello, I'm calendar event: %s" % (self.__dict__)
        return msg

def get_existing_event():
    beer_party = CalendarEvent()
    beer_party.attendees = [{'name': 'name1'},
                            {'name': 'name2'}]
    beer_party.start_date_and_time = datetime(year=2016,
                                              month=6,
                                              day=29,
                                              hour=9,
                                              minute=30)
    beer_party.priority = APPPriority.high
    return beer_party

if __name__ == '__main__':
    some_event = get_existing_event()
    print(some_event)

    new_events = some_event.clone_all()
    new_events.attendees.append({'name': 'name3'})
    new_events.start_date_and_time = datetime(year=2016,
                                              month=6,
                                              day=29,
                                              hour=16,
                                              minute=30)
    print(new_events)
    print(some_event)
