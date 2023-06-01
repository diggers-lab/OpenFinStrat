from abc import ABC, abstractmethod
from enum import Enum
import datetime


class OrderType(Enum):
    LONG = 1
    SHORT = 2


class AssetClass(Enum):
    BOND = 1
    OPTION = 2
    FUTURE = 3
    STOCK = 4


class Order(ABC):

    fee_rate = 0.01
    slippage_rate = 0.005
    margin_rate = 0.5
    

    def __init__(self, asset_class: AssetClass, order_type: OrderType, quantity: int, price: float):
        self.asset_class = asset_class
        self.order_type = order_type
        self.quantity = quantity
        self.price = price

    @abstractmethod
    def add_order_to_portfolio(self, portfolio):
        pass

    def _check_cash(self, portfolio):
        transaction_cost = self._calculate_transaction_cost()
        margin_requirement = self._calculate_margin_requirement()

        if self.order_type == OrderType.LONG:
            return portfolio.cash >= transaction_cost
        elif self.order_type == OrderType.SHORT:
            return portfolio.cash >= transaction_cost + margin_requirement

    def _calculate_transaction_cost(self):
        return self.quantity * self.price * self.fee_rate

    def _calculate_margin_requirement(self):
        if self.order_type == OrderType.SHORT:
            return self.quantity * self.price * self.margin_rate
        else:
            return 0

    def _apply_fees_and_slippage(self):
        self.price = self.price * (1 - self.fee_rate)

        if self.order_type == OrderType.LONG:
            self.price = self.price * (1 + self.slippage_rate)
        else:
            self.price = self.price * (1 - self.slippage_rate)

     #en admettant que l'on ait un data provider fonctionnel
     #def update_price(self, data_provider):
      #  self.price = data_provider.get_price(args)


class BondOrder(Order):

    def add_order_to_portfolio(self, portfolio):
        if self._check_cash(portfolio):
            self._apply_fees_and_slippage()
            portfolio.add_order_to_position(self)
        else:
            print("Not enough cash to proceed order")

class OptionOrder(Order):

    def __init__(self, order_type: OrderType, quantity: int, price: float, 
                 underlying: str, expiry: datetime.date, strike: float, is_call: bool):
        super().__init__(AssetClass.OPTION, order_type, quantity, price)
        self.underlying = underlying
        self.expiry = expiry
        self.strike = strike
        self.is_call = is_call

    def add_order_to_portfolio(self, portfolio):
        if self._check_cash(portfolio):
            self._apply_fees_and_slippage()
            portfolio.add_order_to_position(self)
        else:
            print("Not enough cash to proceed order")



class FutureOrder(Order):

    def __init__(self, order_type: OrderType, quantity: int, price: float, 
                 underlying: str, expiry: datetime.date, strike: float, is_call: bool):
        super().__init__(AssetClass.OPTION, order_type, quantity, price)
        self.underlying = underlying
        self.expiry = expiry

    def add_order_to_portfolio(self, portfolio):
        if self._check_cash(portfolio):
            self._apply_fees_and_slippage()
            portfolio.add_order_to_position(self)
        else:
            print("Not enough cash to proceed order")

class StockOrder(Order):

    def add_order_to_portfolio(self, portfolio):
        if self._check_cash(portfolio):
            self._apply_fees_and_slippage()
            portfolio.add_order_to_position(self)
        else:
            print("Not enough cash to proceed order")
