from order import Order
from shipping_cost import ShippingCost
#from fedex_strategy import FedExStrategy
#from ups_strategy import UPSStrategy
#from usps_strategy import USPSStrategy


'''
For our variation on the strategy pattern, we'll use lambda functions and functions
so we can see other ways to use the pattern
'''
def fedex_strategy(order):
    return 3.0

ups_strategy = lambda order: 4.0

order = Order()

# test the methods
strategy = fedex_strategy
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 3.0

cost_calculator = ShippingCost(ups_strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 4.0

cost_calculator = ShippingCost(lambda order: 5.0)
cost = cost_calculator.shipping_cost(order)
assert cost == 5.0

print('Tests passed')