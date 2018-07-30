from strategy_abc import AbsStrategy

class UPSStrategy(AbsStrategy):
    ''' concrete implementation of hte ABC '''
    def calculate(self, order):
        return 4.00