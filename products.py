class Product:
    """
    A class used to represent a product

    Attributes
    ----------
    name : str
        the name of the product
    price : float
        the price of the product
    quantity : int
        the number of available products
    active: bool
        indicates if the product is active or not
    """
    def __init__(self, name, price, quantity):
        """
        Constructs a product object.
        Creates the instance variables (active is set to True if quantity > 0).

        Parameters
        ----------
        name: str
            the name of the product
        price: float
            the number of available products
        quantity : int
            the number of available products

        Raises
        ----------
        ValueError
            If something is invalid (empty name / negative price or quantity)
        """
        if name == "":
            raise ValueError("Invalid name, name should not be empty!")
        if price < 0 or quantity < 0:
            raise ValueError("Invalid value, negative values are not allowed!")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        if self.quantity == 0:
            self.deactivate()

    def get_quantity(self):
        """
        Returns quantity of the product.
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Sets quantity. If quantity reaches 0, deactivates the product.

        Parameters
        ----------
        quantity : int
            the number of available products
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """
        Returns value of parameter active of the product.
        """
        return self.active

    def activate(self):
        """
        Activates the product, sets the parameter active to True.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivates the product, sets the parameter active to False.
        """
        self.active = False

    def show(self):
        """
        Prints a string that represents the product
        """
        print(f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}")

    def buy(self, purchase_quantity):
        """
        Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.

        Parameters
        ----------
        purchase_quantity : int
            the number of products that are being purchased

        Raises
        ----------
        ValueError
            If the quantity of the product after buying is going to be negative.
        """

        if purchase_quantity <= 0:
            raise ValueError("The quantity should be a positive amount.")
        if not self.active:
            raise ValueError("The product is not available.")
        purchase_price = purchase_quantity * self.price
        new_quantity = self.quantity - purchase_quantity
        if new_quantity < 0:
            raise ValueError("Error while making order! Quantity larger than what exists.")
        self.set_quantity(new_quantity)
        return purchase_price


class NonStockedProduct (Product):
    """
    A child class from the class Product.
    It is used to represent a product that has unlimited availability.
    (not physical product)

    Attributes
    ----------
    quantity : 0
        not needed to keep track of the quantity
    active: bool
        Initially active.
    """
    def __init__(self, name, price):
        """
        Constructs a NonStockedProduct object.
        Creates the instance variables (active is set to True).
        Quantity is set to zero.
        Parameters
        ----------
        name : str
            The name of the product.
        price : float
            The price of the product.
        """
        super().__init__(name, price, quantity=0)
        self.activate()

    def show(self):
        """
        Prints a string that represents the product
        """
        print(f"{self.name}, Price: ${self.price}, Quantity: Unlimited")

    def buy(self, purchase_quantity):
        """
        Purchases the specified quantity of the product.

        Since this product is not stock-limited, its quantity is
        not reduced after purchase.
        """
        if purchase_quantity <= 0:
            raise ValueError("The quantity should be a positive amount.")
        if not self.active:
            raise ValueError("The product is not available.")
        purchase_price = purchase_quantity * self.price
        return purchase_price


class LimitedProduct (Product):
    """
    A child class from the class Product.
    It is used to represent a product that can only be purchased a maximum
        number of times in an order

    Attributes
    ----------
    maximum : int
        The maximum number of units that can be purchased per order.
    """
    def __init__(self, name, price, quantity, maximum):
        """
        Constructs a LimitedProduct object.

        Parameters
        ----------
        name: str
            the name of the product
        price: float
            the number of available products
        quantity : int
            the number of available products
        maximum : int
            The maximum number of units allowed per order.
        """
        super().__init__(name, price, quantity)
        self.maximum = maximum
        if maximum <= 0:
            raise ValueError("Maximum must be positive.")

    def show(self):
        """
        Prints a string that represents the product
        """
        print(f"{self.name}, Price: ${self.price}, Limited to 1 per order!")

    def buy(self, purchase_quantity):
        """
        Purchases the specified quantity of the product.

        Raises
        ------
        ValueError
            If the requested quantity exceeds the maximum allowed
            per order.
        """
        if purchase_quantity > self.maximum:
            raise ValueError(f"Only {self.maximum} is allowed from this product: {self.name}!")
        return super().buy(purchase_quantity)
