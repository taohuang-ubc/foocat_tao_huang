import statistics

def get_mean(l):
    """
    Concatenates two pandas categoricals.

    Parameters
    ----------
    l : list
      A list of numbers.

    Returns
    -------
    float
      The result.

    Examples
    --------
    >>> from foocat_tao_huang import foocat_tao_huang
    >>> a = [1,2,3]
    >>> foocat.get_mean(a)
    2.0
    """
    return sum(l) / len(l)
