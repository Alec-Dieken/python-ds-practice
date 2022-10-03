def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swapped = ''
    for c in phrase:
        if c == to_swap.upper():
            swapped += c.lower()
        elif c == to_swap.lower():
            swapped += c.upper()
        else:
            swapped += c
    return swapped


if __name__ == "__main__":
    import doctest
    doctest.testmod()
