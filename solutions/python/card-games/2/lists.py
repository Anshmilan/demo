"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    round_num=list((number,number+1,number+2))
    return round_num


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    if number in rounds:
        return True
    return False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    total=0
    list_len=len(hand)
    for i_el in hand:
        total=total+i_el
    return total/list_len


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    actual_avg=card_average(hand)
    list_len=len(hand)
    index_med=int((list_len-1)/2)
    med_avg=hand[index_med]
    other_avg=(hand[0]+hand[list_len-1])/2
    if med_avg==actual_avg or other_avg==actual_avg:
        return True
    return False


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    k,x=0,0
    count1,count2=0,0
    for index,i in enumerate(hand):
        if index%2==0:
            k=k+i
            count1=count1+1
        else:
            x=x+i
            count2=count2+1
    even_index=k/count1
    odd_index=x/count2
    if even_index==odd_index:
        return True
    return False
            


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[len(hand)-1]==11:
        double=hand[len(hand)-1] * 2
        hand.pop()
        hand.append(double)
        return hand
    else:
        return hand
    
