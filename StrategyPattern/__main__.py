from order import Order
from shipping_cost import ShippingCost
from fedex_strategy import FedExStrategy
from ups_strategy import UPSStrategy
from usps_strategy import USPSStrategy

# test the methods
order = Order()
strategy = FedExStrategy()  #we are using a concrete strategy object
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 3.0

order = Order()
strategy = UPSStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 4.0

order = Order()
strategy = USPSStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 5.0

print('Tests passed')