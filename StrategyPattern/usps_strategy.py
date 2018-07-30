from strategy_abc import AbsStrategy

class USPSStrategy(AbsStrategy):
    ''' concrete implementation of hte ABC '''
    def calculate(self, order):
        return 5.00