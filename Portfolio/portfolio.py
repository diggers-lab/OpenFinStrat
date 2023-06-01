class Portfolio:

    def __init__(self):
        self.positions = {} 
        self.cash = 0  

    def add_order_to_position(self, order):
        if (order.asset_class, order.order_type) in self.positions:
            self.positions[(order.asset_class, order.order_type)].append(order)
        else:
            self.positions[(order.asset_class, order.order_type)] = [order]

        self.cash -= order.price * order.quantity

    def add_cash(self, amount):
        self.cash += amount
