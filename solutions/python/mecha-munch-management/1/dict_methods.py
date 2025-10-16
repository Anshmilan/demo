"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    for item in items_to_add:
        if item in current_cart:
            current_cart[item]=current_cart[item]+1
        else:
            current_cart[item]=1
    return current_cart
        


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    new_dict=dict()
    for item in notes:
        new_dict[item]=1
    return new_dict
        


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
     ideas={'Banana Bread' : {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
     'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1}}
     recipe_updates=(('Banana Bread', {'Banana': 4,  'Walnuts': 2, 'Flour': 1, 'Butter': 1, 'Milk': 2, 'Eggs': 3}),)
    """
    for recipe in recipe_updates:
        rec=recipe[0]
        if recipe[0] in ideas:
            ideas[rec]=recipe[1]
        else:
            ideas[rec]=recipe[1]
    return ideas
    
def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    sorted_items=dict(sorted(cart.items()))
    return sorted_items


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    cart={'Banana': 3, 'Apple': 2, 'Orange': 1, 'Milk': 2}
    aisle_mapping={'Banana': ['Aisle 5', False], 'Apple': ['Aisle 4', False], 'Orange': ['Aisle 4', False], 'Milk': ['Aisle 2', True]}
    """
    value=list()
    for key,item in cart.items():
        if key in aisle_mapping:
            value=aisle_mapping[key]
            value.insert(0,item)
            cart[key]=value
            
    sorted_dict = dict(sorted(cart.items(), key=lambda item: item[0], reverse=True))
    return sorted_dict
    


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    fulfillment_cart={'Orange': [1, 'Aisle 4', False], 'Milk': [2, 'Aisle 2', True], 'Banana': [3, 'Aisle 5', False], 'Apple': [2, 'Aisle 4', False]}
    store_inventory={'Banana': [15, 'Aisle 5', False], 'Apple': [12, 'Aisle 4', False], 'Orange': [1, 'Aisle 4', False], 'Milk': [4, 'Aisle 2', True]}
    """

    valuecart_list=list()
    valuestore_list=list()
    for key,item in fulfillment_cart.items():
        if key in store_inventory:
            valuecart_list=fulfillment_cart[key]
            valuestore_list=store_inventory[key]
            if valuestore_list[0]>valuecart_list[0]:
                valuestore_list[0]=(valuestore_list[0]-valuecart_list[0])
                store_inventory[key]=valuestore_list
            else:
                valuestore_list[0]='Out of Stock'
                store_inventory[key]=valuestore_list

    return store_inventory
                
                
            
