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
    promotion: Promotion class
        the type of promotion that would be applied to the final price
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
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.promotion = None
        self.active = True
        if self.quantity == 0:
            self.deactivate()

    @property
    def name(self):
        """
       Returns the name of the product.
       """
        return self._name

    @name.setter
    def name(self, new_name):
        """
        Sets name. If new name is empty it raises a ValueError.

        Parameters
        ----------
        new_name : str
            the name of the product

        Raises
        ----------
        ValueError
            If new name is empty
        """
        if new_name == "":
            raise ValueError("Invalid name, name should not be empty!")
        self._name = new_name

    @property
    def price(self):
        """
        Returns the price of the product.
        """
        return self._price

    @price.setter
    def price(self, value):
        """
        Sets price. If price is negative raises a ValueError.

        Parameters
        ----------
        value : int
            the price of the product

        Raises
        ----------
        ValueError
            If value is negative
        """
        if value < 0:
            raise ValueError("Invalid value, negative values are not allowed!")
        self._price = value

    @property
    def quantity(self):
        """
        Returns quantity of the product.
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets quantity. If quantity reaches 0, deactivates the product.

        Parameters
        ----------
        quantity : int
            the number of available products
        Raises
        ----------
        ValueError
            If negative quantity
        """
        if quantity < 0:
            raise ValueError("Invalid value, negative values are not allowed!")
        self._quantity = quantity
        if self._quantity == 0:
            self.deactivate()

    @property
    def promotion(self):
        """
        Returns promotion of the product.
        """
        if self._promotion:
            return self._promotion
        return None

    @promotion.setter
    def promotion(self, promotion):
        """
        Sets promotion.

        Parameters
        ----------
        promotion : class Promotion
            the number of available products
        """
        self._promotion = promotion

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

    def __str__(self):
        """
        Returns a string that represents the product
        """
        promotion_name = self.promotion.name if self.promotion else "None"
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}, Promotion: {promotion_name}"

    def buy(self, purchase_quantity):
        """
        Buys a given quantity of the product.
        Returns the total price (float) of the purchase, if the product is
            affected by a promotion, the promotion is discounted from the
            final price
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
        new_quantity = self.quantity - purchase_quantity
        if new_quantity < 0:
            raise ValueError("Error while making order! Quantity larger than what exists.")
        self.quantity = new_quantity
        if self.promotion:
            return self.promotion.apply_promotion(self, purchase_quantity)
        return purchase_quantity * self.price

    def __lt__(self, other):
        """
        Returns True if the price of the product is less than the price
        of the other product and False in other situation.
        """
        return self.price < other.price

    def __gt__(self, other):
        """
        Returns True if the price of the product is greater than the price
        of the other product and False in other situation.
        """
        return self.price > other.price

    def __eq__(self, other):
        """
        Returns True if the Product is exactly the same as the other product.
        (same attributes)
        """
        if not isinstance(other, Product):
            return NotImplemented
        return (
                self.name == other.name
                and self.price == other.price
                and self.promotion == other.promotion
                and type(self) is type(other)
            )

    def copy(self):
        """
        It returns a copy of the product
        """
        new_product = Product(self.name, self.price, self.quantity)
        new_product.promotion = self.promotion
        return new_product


class NonStockedProduct(Product):
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

    def __str__(self):
        """
        Returns a string that represents the product
        """
        promotion_name = self.promotion.name if self.promotion else "None"
        return f"{self.name}, Price: ${self.price}, Quantity: Unlimited, Promotion: {promotion_name}"

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
        if self.promotion:
            return self.promotion.apply_promotion(self, purchase_quantity)
        return purchase_quantity * self.price

    def copy(self):
        """
        It returns a copy of the product
        """
        new_product = NonStockedProduct(self.name, self.price)
        new_product.promotion = self.promotion
        return new_product


class LimitedProduct(Product):
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

    def __str__(self):
        """
        Returns a string that represents the product
        """
        promotion_name = self.promotion.name if self.promotion else "None"
        return f"{self.name}, Price: ${self.price}, Limited to {self.maximum} per order!, Promotion: {promotion_name}"

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

    def __eq__(self, other):
        """
        Returns True if the Product is exactly the same as the other product.
        (same attributes)
        """
        if super().__eq__(other):
            return self.maximum == other.maximum
        return False

    def copy(self):
        """
        It returns a copy of the product
        """
        new_product = LimitedProduct(
            self.name,
            self.price,
            self.quantity,
            self.maximum
        )
        new_product.promotion = self.promotion
        return new_product
