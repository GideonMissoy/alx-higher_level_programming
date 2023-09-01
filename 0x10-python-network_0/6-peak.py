#!/ur/bin/python3
"""
Function finds a peak in a list of unsorted integers.
"""

def find_peak(list_of_integers):
    """finds the peak in a list of ints."""
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    p = int(length / 2)
    li = list_of_integers

    if p - 1 < 0 and p + 1 >= length:
        return li[p]
    elif p - 1 < 0:
        return li[p] if li[p] > li[p + 1] else li[p + 1]
    elif p + 1 >= length:
        return li[p] if li[p] > li[p - 1] else li[p - 1]

    if li[p - 1] < li[p] > li[p + 1]:
        return li[p]

    if li[p + 1] > li[p - 1]:
        return find_peak(li[p:])
    return find_peak(li[:p])
