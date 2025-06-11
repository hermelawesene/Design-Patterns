from abc import ABC, abstractmethod
from typing import List

# Subject interface
class OrderSystem(ABC):
    @abstractmethod
    def add_observer(self, observer) -> None:
        pass

    @abstractmethod
    def remove_observer(self, observer) -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass

# Observer interface
class OrderObserver(ABC):
    @abstractmethod
    def update(self, order: str) -> None:
        pass

# Concrete subject
class RestaurantOrderSystem(OrderSystem):
    def __init__(self):
        self._observers: List[OrderObserver] = []
        self._latest_order: str = ""

    def add_observer(self, observer: OrderObserver) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: OrderObserver) -> None:
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self._latest_order)

    def place_order(self, order: str) -> None:
        """Places a new order and notifies observers."""
        self._latest_order = order
        self.notify_observers()

# Concrete observers
class Kitchen(OrderObserver):
    def update(self, order: str) -> None:
        print(f"Kitchen received order: Prepare {order}")

class Cashier(OrderObserver):
    def update(self, order: str) -> None:
        print(f"Cashier received order: Charge for {order}")

class CustomerDisplay(OrderObserver):
    def update(self, order: str) -> None:
        print(f"Customer Display updated: Order {order} received")

# Client code with user input
def main():
    # Create order system and observers
    order_system = RestaurantOrderSystem()
    kitchen = Kitchen()
    cashier = Cashier()
    display = CustomerDisplay()

    # Subscribe observers
    order_system.add_observer(kitchen)
    order_system.add_observer(cashier)
    order_system.add_observer(display)

    print("Welcome to the Burger Restaurant Order System!")
    while True:
        try:
            order = input("Enter burger order (e.g., Cheeseburger, or 'quit' to exit): ").strip()
            if order.lower() == "quit":
                print("Order system shutting down!")
                break
            order_system.place_order(order)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()