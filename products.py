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
        Creates the instance variables (active is set to True).

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
        else:
            self.quantity = quantity
            if self.quantity == 0:
                self.active = False

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
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        """
        Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.

        Parameters
        ----------
        quantity : int
            the number of available products

        Raises
        ----------
        ValueError
            If the quantity of the product after buying is going to be negative.
        """

        if quantity < 0:
            raise ValueError("The quantity should be a positiv amount.")
        if not self.active:
            raise ValueError("The product is not available.")
        purchase_price = quantity * self.price
        new_quantity = self.quantity - quantity
        if new_quantity < 0:
            raise ValueError("Error while making order! Quantity larger than what exists.")
        self.set_quantity(new_quantity)
        return purchase_price
