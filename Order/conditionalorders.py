from order import Order, AssetClass, OrderType

class LimitOrder(Order):

    def __init__(self, asset_name: str, asset_class: AssetClass, order_type: OrderType, 
                 quantity: int, price: float, limit_price: float):
        super().__init__(asset_name, asset_class, order_type, quantity, price)
        self.limit_price = limit_price

    #en pratique on récupère le prix de marché via le data provider des données historiques
    def _check_execution(self, market_price: float):
        if self.order_type == OrderType.LONG and market_price <= self.limit_price:
            return True
        elif self.order_type == OrderType.SHORT and market_price >= self.limit_price:
            return True
        else:
            return False


class StopOrder(Order):

    def __init__(self, asset_name: str, asset_class: AssetClass, order_type: OrderType, 
                 quantity: int, price: float, stop_price: float):
        super().__init__(asset_name, asset_class, order_type, quantity, price)
        self.stop_price = stop_price

    def _check_execution(self, market_price: float):
        if self.order_type == OrderType.LONG and market_price >= self.stop_price:
            return True
        elif self.order_type == OrderType.SHORT and market_price <= self.stop_price:
            return True
        else:
            return False
