from turtle import clear


def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    dict = {}
    for c in phrase:
        if not c in dict:
            dict[c] = 1
        else:
            dict[c] += 1

    return dict

if __name__ == "__main__":
    import doctest
    doctest.testmod()