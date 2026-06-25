from abc import ABC, abstractmethod


class Promotion (ABC):
    """
    A class used to represent a basis promotion

    Attributes
    ----------
    name : str
        the name of the promotion
    """
    def __init__(self, name):
        """
        Constructs a promotion object.

        Parameters
        ----------
        name: str
            the name of the promotion
        """
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """
        Returns the price after the promotion.
        """


class PercentDiscount (Promotion):
    """
    A child class from Promotion. Percentage discount promotion.

    Attributes
    ----------
    name: str
        the name of the promotion
    percent: int
        percentage discount
    """
    def __init__(self, name, percent):
        """
        Constructs a PercentDiscount object.

        Parameters
        ----------
        name: str
            the name of the promotion
        percent: int
            percentage discount
        """
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        """
        Returns the price after the percent discount is applied.
        """
        return quantity * product.price * (1 - self.percent / 100)


class SecondHalfPrice (Promotion):
    """
    A child class from Promotion. Each second product costs half price.

    Attributes
    ----------
    name: str
        the name of the promotion
    """

    def apply_promotion(self, product, quantity):
        """
        A discount of half price is applied to each second product.
        Returns the price after the percent discount is applied.
        """
        quantity_half_price = quantity // 2
        return (quantity - quantity_half_price) * product.price + quantity_half_price * product.price / 2


class ThirdOneFree(Promotion):
    """
   A child class from Promotion. Each third product is not taken into account
   for calculating the final price.

   Attributes
   ----------
   name: str
       the name of the promotion
   """

    def apply_promotion(self, product, quantity):
        """
        Third products are not taken into account to calculate the final price.
        Returns the price after the discount is applied.
        """
        quantity_third_product = quantity // 3
        return (quantity - quantity_third_product) * product.price
