from abc import ABCMeta, abstractmethod

class OrderState(metaclass=ABCMeta):
    def __init__(self, order):
        self.order = order

    def add_product(self):
        raise Exception()

    def ship(self):
        raise Exception()

    def cancel(self):
        raise Exception()

class Shipped(OrderState):
    def grand(self):
        self.order.do_grand()
        self.order.set_order_state(Granted(self.order))

    def ship(self):
        self.order.do_shipping()
        self.order.set_order_state(Shipped(self.order))

    def cancel(self):
        self.order.do_cancel()
        self.order.set_order_state(Cancelled(self.order))

class Granted(OrderState):

    def add_product(self):
        self.order.do_add_product()

    def ship(self):
        self.order.do_shipping()
        self.order.set_order_state(Shipped(self.order))

    def cancel(self):
        self.order.do_cancel()
        self.order.set_order_state(Cancelled(self.order))

class NewOrder(OrderState):

    def add_product(self):
        self.order.do_add_product()

    def ship(self):
        self.order.do_shipping()
        self.order.set_order_state(Shipped(self.order))

    def cancel(self):
        self.order.do_cancel()
        self.order.set_order_state(Cancelled(self.order))

class Cancelled(OrderState):

    def cancel(self):
        self.order.do_cancel()
        self.order.set_order_state(Cancelled(self.order))

class Order(object):

    def __init__(self):
        self._state = NewOrder(self)

    def set_order_state(self, state):
        self._state = state

    def write_curent_state(self):
        print(self._state)

    def ship(self):
        self._state.ship()

    def grand(self):
        self._state.grand()

    def do_grand(self):
        print("do_grand")

    def do_shipping(self):
        print('do_shipping')

    def do_cancel(self):
        print('do_cancel')

    def do_add_product(self, product):
        print('do_add_product')


if __name__ == '__main__':
    order = Order()
    order.do_add_product('prod1')
    order.do_add_product('prod2')

    order.write_curent_state()

    order.ship()
    order.write_curent_state()

    order.grand()
    order.write_curent_state()
