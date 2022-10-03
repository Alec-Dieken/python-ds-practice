def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """

    total = 0

    for c in word:
        if c.lower() == letter:
            total += 1

    return total

if __name__ == "__main__":
    import doctest
    doctest.testmod()