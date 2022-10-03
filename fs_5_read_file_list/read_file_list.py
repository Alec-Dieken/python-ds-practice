def read_file_list(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("C:/Users/ajdie/Desktop/Springboard/Practice/python-ds-practice/fs_5_read_file_list/dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.
    """
    f = open(filename, 'r')
    for line in f:
        line = line.strip()
        print(f"- {line}")
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()