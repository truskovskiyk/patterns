class WeirdCafeVisitor(object):

    def __init__(self, cafe_visitor=None):
        self.cafe_visitor = cafe_visitor

    def handle_food(self, food):
        print("just pass")
        if self.cafe_visitor is not None:
            self.cafe_visitor.handle_food(food)

class BestFriend(WeirdCafeVisitor):
    def __init__(self, cafe_visitor):
        super(BestFriend, self).__init__(cafe_visitor)
        self.coffe_cintain_food = []

    def handle_food(self, food):
        print("I take some coffe and meat")
        test_food = food[0]
        if test_food == 'coffe' or test_food == 'meat':
            self.coffe_cintain_food.append(food.pop())
            print(self.coffe_cintain_food)
            return
        self.cafe_visitor.handle_food(food)

class GirlFriend(WeirdCafeVisitor):
    def __init__(self, cafe_visitor):
        super(GirlFriend, self).__init__(cafe_visitor)
        self.some_food_for_girls = []

    def handle_food(self, food):
        print("I take some girls food")
        test_food = food[0]
        if test_food == 'girls food':
            self.some_food_for_girls.append(test_food)
            print(self.some_food_for_girls)
            return
        self.cafe_visitor.handle_food(food)

if __name__ == '__main__':
    some_company = BestFriend(GirlFriend(WeirdCafeVisitor()))
    food = ['food1', 'food2']
    food = ['girls food', 'food2']
    some_company.handle_food(food)
