import sys
import products
import store
import promotions


def menu():
    """
    Displays the menu options
    """
    print()
    print("   Store Menu:")
    print("   ----------")
    for key, value in MENU_ACTIONS.items():
        _, option, _ = value
        print(f"{key} {option}")


def list_products_store(products_in_store):
    """
    Lists the list of products available in the store.

    Parameters
    ----------
    products_in_store: a class Store object
        a list of class Products objects
    """
    num = 1
    available_products = products_in_store.get_all_products()
    print("------")
    for product in available_products:
        print(f"{num}.", end=" ")
        print(product)
        num += 1
    print("------")


def show_total_amount_store(products_in_store):
    """
    Displays the total amount of items in the store.

    Parameters
    ----------
    products_in_store: a class Store object
        a list of class Products objects
    """

    total_quantity = products_in_store.get_total_quantity()
    print(f"Total of {total_quantity} items in store")


def make_order(products_in_store):
    """
    Asks the user the product and quantity that he/she wants to order. The user
    can choose more than one product. It prints the total price that the order
    costs. The quantity of purchased products is subtracted from the quantity
    in the Store

    Parameters
    ----------
    products_in_store: a class Store object
        a list of class Products objects

    Raises
    ------
    ValueError
        when the user enters a product that does not exist in the list
        when the user enters a product or a quantity that is not a number
    """
    list_products_store(products_in_store)
    user_order = []
    available_products = products_in_store.get_all_products()
    print("When you want to finish order, enter empty text.")
    while True:
        order_product = input("Which product # do you want? ")
        order_amount = input("What amount do you want? ")
        if order_product == "" or order_amount == "":
            break
        try:
            order_product_int = int(order_product)
            order_amount_int = int(order_amount)
            if order_amount_int <= 0:
                raise ValueError("Quantity must be positive")
            if 1 > order_product_int or order_product_int > len(available_products):
                raise ValueError("This product is not available.")
            user_order.append((available_products[order_product_int - 1], order_amount_int))
            print("Product added to list!")
            print()
        except ValueError as e:
            print("Error adding product!", end=" ")
            print(e)
            print()
    if user_order:
        try:
            total_payment = products_in_store.order(user_order)
            print("********")
            print(f"Order made! Total payment: ${total_payment}")
        except ValueError as e:
            print("Error while making order!", end=" ")
            print(e)


def exit_program():
    """
    Exits the program.
    """
    sys.exit()


MENU_ACTIONS = {
    1: (list_products_store, "List all products in store", True),
    2: (show_total_amount_store, "Show total amount in store", True),
    3: (make_order, "Make an order", True),
    4: (exit_program, "Quit", False),
}


def start(products_in_store):
    """
    Starts the program.

    Parameters
    ----------
    products_in_store: a class Store object
        a list of class Products objects

    Raises
    ------
    ValueError
        when the user enters an option of the menu tthat is not a number
    """
    while True:
        while True:
            menu()
            min_key = min(list(MENU_ACTIONS.keys()))
            max_key = max(list(MENU_ACTIONS.keys()))
            try:
                user_choice = int(input("Please choose a number: "))
            except ValueError:
                print("Error with your choice! Try again!")
                continue
            if min_key <= user_choice <= max_key:
                break
        action, _, needs_products = MENU_ACTIONS.get(user_choice)
        if needs_products:
            action(products_in_store)
        else:
            action()


def main():
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]

    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].promotion = second_half_price
    product_list[1].promotion = third_one_free
    product_list[3].promotion = thirty_percent

    """
    ## Test features ##
    
    # setup initial stock of inventory
    mac = products.Product("MacBook Air M2", price=1450, quantity=100)
    bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    pixel = products.LimitedProduct("Google Pixel 7", price=500, quantity=250, maximum=1)

    mac.promotion = second_half_price

    best_buy2 = store.Store([mac, bose])
    #mac.price = -100  # Should give error
    print(mac)  # Should print `MacBook Air M2, Price: $1450 Quantity:100`
    print(mac > bose)  # Should print True
    print(mac in best_buy2)  # Should print True
    print(pixel in best_buy2)  # Should print False
    """
    best_buy = store.Store(product_list)
    """
    print(mac in best_buy)
    
    ## Test combine two stores ##
    combined_store = best_buy + best_buy2
    for product in combined_store.list_of_products:
        print(product)
    """

    start(best_buy)


if __name__ == "__main__":
    main()
