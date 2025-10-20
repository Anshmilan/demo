"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from `dish_ingredients`.

    :param dish_name: str - containing the dish name.
    :param dish_ingredients: list - dish ingredients.
    :return: tuple - containing (dish_name, ingredient set).

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    """

    dish_ing=set(dish_ingredients)
    fin=[]
    fin.append(dish_name)
    fin.append(dish_ing)
    return tuple(fin)
    


def check_drinks(drink_name, drink_ingredients):
    """Append "Cocktail" (alcohol)  or "Mocktail" (no alcohol) to `drink_name`, based on `drink_ingredients`.

    :param drink_name: str - name of the drink.
    :param drink_ingredients: list - ingredients in the drink.
    :return: str - drink_name appended with "Mocktail" or "Cocktail".

    The function should return the name of the drink followed by "Mocktail" (non-alcoholic) and drink
    name followed by "Cocktail" (includes alcohol).

    """
    drink_ingredients_set=set(drink_ingredients)
    alcohol_set=ALCOHOLS
    item=drink_ingredients_set.isdisjoint(alcohol_set)
    if item is True:
        key='Mocktail'
    else:
        key='Cocktail'
    return drink_name+' '+key
    


def categorize_dish(dish_name, dish_ingredients):
    """Categorize `dish_name` based on `dish_ingredients`.

    :param dish_name: str - dish to be categorized.
    :param dish_ingredients: set - ingredients for the dish.
    :return: str - the dish name appended with ": <CATEGORY>".

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    `<CATEGORY>` can be any one of  (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    All dishes will "fit" into one of the categories imported from `sets_categories_data.py`

    """

    Vegan_n=dish_ingredients.issubset(VEGAN)
    Vegetarian_n=dish_ingredients.issubset(VEGETARIAN)
    Paleo_n=dish_ingredients.issubset(PALEO)
    Keto_n=dish_ingredients.issubset(KETO)
    Omnivore_n=dish_ingredients.issubset(OMNIVORE)

    if Vegan_n is True:
        key='VEGAN'
    elif Vegetarian_n is True:
        key='VEGETARIAN'
    elif Paleo_n is True:
        key='PALEO'
    elif Keto_n is True:
        key='KETO'
    elif Omnivore_n is True:
        key='OMNIVORE'

    return dish_name+':'+' '+key
        


def tag_special_ingredients(dish):
    """Compare `dish` ingredients to `SPECIAL_INGREDIENTS`.

    :param dish: tuple - of (dish name, list of dish ingredients).
    :return: tuple - containing (dish name, dish special ingredients).

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `sets_categories_data.py`.
    """

    ing_set=set(dish[1])
    resp=ing_set.intersection(SPECIAL_INGREDIENTS)
    ing_list=[]
    ing_list.append(resp)
    ing_list.insert(0,dish[0])
    return tuple(ing_list)


def compile_ingredients(dishes):
    """Create a master list of ingredients.

    :param dishes: list - of dish ingredient sets.
    :return: set - of ingredients compiled from `dishes`.

    This function should return a `set` of all ingredients from all listed dishes.
    """
    item1=set()
    for item in dishes:
        item1=item1|item
    return item1


def separate_appetizers(dishes, appetizers):
    """Determine which `dishes` are designated `appetizers` and remove them.

    :param dishes: list - of dish names.
    :param appetizers: list - of appetizer names.
    :return: list - of dish names that do not appear on appetizer list.

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """

    dishes_set=set(dishes)
    appetizers_set=set(appetizers)
    fin= dishes_set ^ appetizers_set
    return list(fin)


def singleton_ingredients(dishes, intersection):
    """Determine which `dishes` have a singleton ingredient (an ingredient that only appears once across dishes).

    :param dishes: list - of ingredient sets.
    :param intersection: constant - can be one of `<CATEGORY>_INTERSECTIONS` constants imported from `sets_categories_data.py`.
    :return: set - containing singleton ingredients.

    Each dish is represented by a `set` of its ingredients.

    Each `<CATEGORY>_INTERSECTIONS` is an `intersection` of all dishes in the category. `<CATEGORY>` can be any one of:
        (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).

    The function should return a `set` of ingredients that only appear in a single dish.
    """
    intersection_fin=set()
    diff_fin=set()
    for item in dishes:
        intersections_1=item & intersection
        intersection_fin=intersection_fin|intersections_1
        diff_2=item ^ intersection
        diff_fin=diff_fin^diff_2
    return diff_fin-intersection_fin
        
        
