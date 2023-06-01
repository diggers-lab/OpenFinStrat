from Portfolio.portfolio import Portfolio
from Order.order import StockOrder, BondOrder, OptionOrder, OrderType, AssetClass
import datetime

def main():

    portfolio = Portfolio()
    portfolio.add_cash(1000000)  

    order1 = StockOrder(AssetClass.STOCK, OrderType.LONG, 500, 200)
    order1._apply_fees_and_slippage()
    print(f"Price after fees and slippage: {order1.price}")

    order2 = BondOrder(AssetClass.BOND, OrderType.LONG, 1000, 1000)
    order2._apply_fees_and_slippage()
    print(f"Price after fees and slippage: {order2.price}")
    
    bond_order2 = BondOrder(asset_class=AssetClass.BOND, order_type=OrderType.LONG, quantity=200, price=1100)
    bond_order2._apply_fees_and_slippage()


    expiry_date = datetime.date.today() + datetime.timedelta(days=30)
    order3 = OptionOrder(OrderType.LONG, 10, 1.0, '', expiry_date, 200.0, True)
    order3._apply_fees_and_slippage()
    print(f"Price after fees and slippage: {order3.price}")

    portfolio.add_order_to_position(order1)
    portfolio.add_order_to_position(order2)
    portfolio.add_order_to_position(order3)

    print(portfolio.positions)

if __name__ == "__main__":
    main()
