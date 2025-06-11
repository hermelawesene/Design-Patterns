from abc import ABC, abstractmethod

# Target interface (new system)
class OrderProcessor(ABC):
    @abstractmethod
    def process_order(self, order: str) -> str:
        """Processes a burger order."""
        pass

# Adaptee: Old kitchen system with incompatible interface
class OldKitchenSystem:
    def cook_burger(self, burger_type: str) -> str:
        """Old system for cooking burgers."""
        return f"Cooking {burger_type} in the old kitchen system"

# Adapter: Converts old system to new interface
class KitchenAdapter(OrderProcessor):
    def __init__(self, old_system: OldKitchenSystem):
        self.old_system = old_system

    def process_order(self, order: str) -> str:
        """Adapts old system's method to new interface."""
        return self.old_system.cook_burger(order)

# Concrete new order processor (for comparison)
class NewOrderProcessor(OrderProcessor):
    def process_order(self, order: str) -> str:
        """New system for processing orders."""
        return f"Processing {order} in the new order system"

# Client code with user input
def main():
    # Initialize systems
    old_kitchen = OldKitchenSystem()
    adapter = KitchenAdapter(old_kitchen)
    new_processor = NewOrderProcessor()

    print("Welcome to the Burger Restaurant Order System!")
    while True:
        try:
            order = input("Enter burger order (e.g., Cheeseburger, or 'quit' to exit): ").strip()
            if order.lower() == "quit":
                print("Order system shutting down!")
                break
            # Process with new system
            print(new_processor.process_order(order))
            # Process with old system via adapter
            print(adapter.process_order(order))
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()