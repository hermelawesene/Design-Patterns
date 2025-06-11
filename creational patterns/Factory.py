from abc import ABC, abstractmethod

# Product interface
class Burger(ABC):
    @abstractmethod
    def prepare(self) -> str:
        """Returns a description of preparing the burger."""
        pass

# Concrete products
class Cheeseburger(Burger):
    def prepare(self) -> str:
        return "Preparing a Cheeseburger: bun, beef patty, cheese, lettuce, tomato"

class VeggieBurger(Burger):
    def prepare(self) -> str:
        return "Preparing a Veggie Burger: bun, veggie patty, lettuce, tomato, avocado"

# Creator factory interface
class BurgerFactory(ABC):
    @abstractmethod
    def create_burger(self) -> Burger:
        """Factory method to create a burger."""
        pass

    def serve_burger(self) -> str:
        """Uses the factory method to prepare and serve a burger."""
        burger = self.create_burger()
        return f"Order up! {burger.prepare()}"

# Concrete factories
class CheeseburgerFactory(BurgerFactory):
    def create_burger(self) -> Burger:
        return Cheeseburger()

class VeggieBurgerFactory(BurgerFactory):
    def create_burger(self) -> Burger:
        return VeggieBurger()

# Restaurant class to handle user orders
class Restaurant:
    # Map user input to factory classes
    FACTORY_MAP = {
        "CHEESE": CheeseburgerFactory,
        "VEGGIE": VeggieBurgerFactory
    }

    def order_burger(self, request: str) -> str:
        """Orders a burger using the appropriate factory based on user input."""
        request = request.upper()
        factory_class = self.FACTORY_MAP.get(request)
        if not factory_class:
            raise ValueError(f"Sorry, we don't have '{request}' on the menu!")
        
        factory = factory_class()
        return factory.serve_burger()

# Client code with user input
def main():
    restaurant = Restaurant()
    
    print("Welcome to the Burger Restaurant!")
    print("Available burgers: CHEESE, VEGGIE")
    while True:
        try:
            request = input("What burger would you like to order? (or 'quit' to exit): ").strip()
            if request.lower() == "quit":
                print("Thank you for visiting!")
                break
            result = restaurant.order_burger(request)
            print(result)
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()