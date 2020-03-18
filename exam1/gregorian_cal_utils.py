def is_leap_year(year: int) -> bool:
    """
    Given a year, this function returns a boolean indicating whether or not it is a leap year.

    :param year: an integer indicating a year.
    :return: A boolean indicating whether or not the year parameter is a leap year.
    """
    if ((((year % 4) == 0) or ((year%400) ==0)) and ((year%100) != 0)):
        return True
    else:
        return False
