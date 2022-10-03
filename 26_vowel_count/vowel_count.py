def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    tracker = {}
    vowels = set('aeiou')
    for c in phrase.lower():
        if c in vowels:
            tracker[c] = tracker.get(c, 0) + 1 

    return tracker


if __name__ == "__main__":
    import doctest
    doctest.testmod()
