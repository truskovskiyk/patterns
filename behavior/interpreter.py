from abc import ABCMeta, abstractmethod

class Goods(metaclass=ABCMeta):

    @abstractmethod
    def interpret(self, context):
        pass

class GoodsPackage(Goods):

    def __init__(self, goods_inside):
        self.goods_inside = goods_inside

    def interpret(self, context):
        total_sum = 0.0
        for goods in self.goods_inside:
            total_sum += goods.interpret(context)
        return total_sum

class TV(Goods):
    def interpret(self, context):
        price = context['TV']
        print("TV: {}".format(price))
        return price

class Bed(Goods):
    def interpret(self, context):
        price = context['Bed']
        print("Bed: {}".format(price))
        return price


if __name__ == '__main__':
    CONTEXT = {
        "TV": 100,
        "Bed": 50
    }

    box1 = GoodsPackage([TV(), Bed(), Bed()])
    box2 = GoodsPackage([TV(), TV(), TV()])
    tv1 = TV()
    tv2 = TV()
    bed1 = Bed()

    track = GoodsPackage([box1, box2, tv1, tv2, bed1])
    print(track.interpret(CONTEXT))
