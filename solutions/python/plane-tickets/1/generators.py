"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    letters=["A","B","C","D"]
    for seat in range(number):
        yield letters[seat % 4]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    seat_letters = generate_seat_letters(number)
    count = 0
    row = 1

    while count < number:
        if row == 13:
            row += 1
            continue

        for i in range(4):  # 4 seats per row
            if count >= number:
                break
            letter = next(seat_letters)
            yield f"{row}{letter}"
            count += 1
        row += 1
    

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    seat=generate_seats(len(passengers))
    pass_dic=dict()
    for person in passengers:
        seat_no=next(seat)
        pass_dic[person]=seat_no
    return pass_dic
        
        

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for index,seat in enumerate(seat_numbers):
        ticket =seat_numbers[index]+flight_id
        if len(ticket)==12:
            yield ticket
        else:
            ticket=ticket+'0'*(12-len(ticket))
            yield ticket
            
