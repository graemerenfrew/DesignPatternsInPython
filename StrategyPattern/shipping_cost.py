class ShippingCost(object):
    def __init__(self, strategy):
        '''
        :param strategy:
        Take in a strategy in the constructor and saves it for later
        '''
        self._strategy = strategy

    def shipping_cost(self, order):
        '''
        :param order:
        :return:
        Use the reference, and executes its calculate method
        '''
        return self._strategy.calculate(order)