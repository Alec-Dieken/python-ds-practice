def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    count = {}
    for n in nums:
        if count.get(n):
            count[n] += 1
        else:
            count[n] = 1
    
    maxK = max(count.values())
    for k in count:
        if count[k] == maxK:
            return k


if __name__ == "__main__":
    import doctest
    doctest.testmod()