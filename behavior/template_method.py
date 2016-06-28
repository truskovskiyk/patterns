class MessagesSeacher(object):

    def __init__(self, date_sent, person_name, importance_level):
        self.date_sent = date_sent
        self.person_name = person_name
        self.importance_level = importance_level

    def create_data_criteria(self):
        print("Apply data criteria")

    def create_sent_person_criteria(self):
        print("Apply sent person criteria")

    def create_importance_criteria(self):
        print("Apply importance criteria")

    def search(self):
        self.create_data_criteria()
        self.create_sent_person_criteria()
        self.create_importance_criteria()
        return "Some messages ..."

class ImportantMessagesSercher(MessagesSeacher):

    def __init__(self, date_sent, person_name):
        super(ImportantMessagesSercher, self).__init__(date_sent,
                                                        person_name, 10)
    def create_importance_criteria(self):
        print("This criteria is now important")

class UselessMessagesSercher(MessagesSeacher):
    def __init__(self, date_sent, person_name):
        super(UselessMessagesSercher, self).__init__(date_sent,
                                                    person_name, 0)
    def create_importance_criteria(self):
        print("This criteria is not used")


if __name__ == '__main__':
    im_mess_sear = ImportantMessagesSercher("data", "person_name")
    im_mess_sear.search()

    us_mess_sear = UselessMessagesSercher("data", "person_name")
    us_mess_sear.search()
