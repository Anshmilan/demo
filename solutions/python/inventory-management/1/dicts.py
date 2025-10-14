"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    """new_dict=dict()
    for it in items:
        counter=items.count(it)
        new_dict[it]=counter
    return new_dict"""
        
    inventory = {}
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    new_list=[]
    for key,value in inventory.items():
        i=0
        while i<value:
            new_list.append(key)
            i=i+1
    new_list_full=new_list + items
    return create_inventory(new_list_full)
    
            


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
#inventory={"coal":3, "diamond":1, "iron":5}
    """items_dict=create_inventory(items)#{"diamond":1,"coal":1,"iron"=2}
    new_dict=dict()
    for key,value in inventory.items():
        for key1,value1 in items_dict.items():
            if key1 == key and value1<=value:
                new_val=value-value1
                new_dict[key1]=new_val
            elif key not in items_dict:
                new_dict[key]=value
            elif  value1>value:
                new_dict[key]=0
    return new_dict"""

    for item in items:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
    return inventory
    


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    new_dict=dict()
    for key,value in inventory.items():
        if key!=item:
            new_dict[key]=value
    return new_dict
            


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    new_tup=tuple()
    for key,value in inventory.items():
        if value>0:
            new_tup=new_tup + ((key,value),)
    return list(new_tup)
        

