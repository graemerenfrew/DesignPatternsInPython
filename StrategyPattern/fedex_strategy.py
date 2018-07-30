from strategy_abc import AbsStrategy

class FedExStrategy(AbsStrategy):
    ''' concrete implementation of hte ABC '''
    def calculate(self, order):
        return 3.00