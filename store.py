class Store:
    """
    A class used to hold all the products and allow the user to make a
    purchase of multiple products at once.

    Attributes
    ----------
    list_of_products : list
        list of all the products
    """

    def __init__(self, list_of_products):
        """
        Constructs a Store object.
        Creates the instance variables.

        Parameters
        ----------
        list_of_products : list
            list of all the products with class Product
        """
        self.list_of_products = list_of_products

    def add_product(self, product):
        """
        Adds a product to the list_of_products.

        Parameters
        ----------
        product: str
        """
        self.list_of_products.append(product)

    def remove_product(self, product):
        """
        Removes a product from the list_of_products.

        Parameters
        ----------
        product: str
        """
        self.list_of_products.remove(product)

    def get_total_quantity(self):
        """
        Returns how many items are in the store in total.
        """
        return sum(product.quantity for product in self.list_of_products if product.is_active())

    def get_all_products(self):
        """
        Returns a list of all products in the store that are active.
        """
        active_products = []
        for product in self.list_of_products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        """
        Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order.

        Parameters
        ----------
        shopping_list: list
            tuples with 2 items: Product (Product class) and quantity (int).
        """
        total_price = 0
        for item in shopping_list:
            product, quantity = item
            total_price += product.buy(quantity)
        return total_price

    def __contains__(self, product):
        """
        Returns a True if the product exists in store and False in other
        situation.
        """
        return product in self.list_of_products

    def __add__(self, other_store):
        """
        It merges the products of two stores into a new store. The products should
        be exactly the same to be included as one product in the new store, and
        only in that case the product quantity would be added for this product.
        """
        new_store = Store([])
        other_store_products = other_store.list_of_products.copy()
        for product in self.list_of_products:
            if product in other_store_products:
                index = other_store_products.index(product)
                other_store_product = other_store_products[index]
                new_product_quantity = product.quantity + other_store_product.quantity
                merged_product = product.copy()
                merged_product.quantity = new_product_quantity
                new_store.add_product(merged_product)
                other_store_products.pop(index)
            else:
                new_store.add_product(product.copy())
        if other_store_products:
            for product in other_store_products:
                new_store.add_product(product.copy())
        return new_store
