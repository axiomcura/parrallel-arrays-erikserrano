"""
Utils.py
Developer: Erik Serrano

utils.py package contains functions that aids in searching and indexing arrays


* linear_search - A function that searches for a specific target from a given
                  array. It will return the index value of target

* binary_search - Searching algorithm that requires an indexed array. (look at
                  index_list). Sorts list and attempts to find target element.
                  return the index position of the target.

* index_list - generates a list of lists where the nested list contains index
               index values for each element.
"""
from typing import Union
from typing import Optional
from typing import List
from typing import Any
from typing import Sequence


def linear_search(target: str, sel_array: List[str]) -> int:
    """Searches target value within given array. If the target is found, an
    ValueError will be raised. If found, it will return the index position
    where the target resides in the provided array.

    Parameters
    ----------
    target : str
        specific value to search within the given array.
    sel_array : list[str]
        selected list of elements that contains data to search.

    Returns
    -------
    int
        index position where the target is located within the array. ValueError
        will be raised if the target cannot be found.

    Raises
    ------
    ValueError
        raised if the target cannot be found within the provided array
    RuntimeError
        raised if empty list was provided
    TypeError
        raised if a non sequences objects are passed (tuples or lists only)

    Example
    -------
    >>> header = ["hello", "world", ":)"]
    >>> indx_pos = linear_search(target="world", sel_array=header)
    >>> print(indx_pos)
    1
    """
    # type checking
    if not isinstance(sel_array, Sequence):
        raise TypeError("Only tuples or lists are supported")
    if len(sel_array) == 0:
        raise RuntimeError("Empty list porivded")

    for idx, field in enumerate(sel_array):
        if target == field:
            return idx
    raise ValueError


def binary_search(
    target: str, indexed_sel_array: List[List[Union[str, int]]]
) -> int:
    """Conducted a binary search on a provided indexed array. The indexed array
    should be a list of lists were the nested list contains string and an
    integer that represents the position where the string entry resides in.

    Parameters
    ----------
    target : str
        target name to look for
    indexed_sel_array : list[list[Any, int]]
        list of nested list that contains indexed parameter names.

    Returns
    -------
    int
        return the true index position where the target resides within the
        provided array.


    Raises
    ------
    ValueError
        Raises when the target is not found within the provided list
    """
    # sort the list
    indexed_sel_array = sorted(indexed_sel_array, key=lambda x: x[0])

    # set up index positions
    low_idx = -1
    high_idx = len(indexed_sel_array)

    # conducting binary search for target element and return true index pos
    while high_idx - low_idx > 1:

        mid_idx = (high_idx + low_idx) // 2

        # return the value if the mid point index point to target
        if target == indexed_sel_array[mid_idx][0]:
            return indexed_sel_array[mid_idx][1]

        # checking where the target resides (left or right half of the array)
        if target.lower() < indexed_sel_array[mid_idx][0].lower():
            high_idx = mid_idx
        else:
            low_idx = mid_idx

    # raised if the target is not found
    raise ValueError


def index_list(sel_array: List[Any]) -> List[Union[Any, int]]:
    """Adds index position to provided list. Returns a list of nested lists,
    where each nested list contains two elements. The first element is the
    original element obtained from the sel_array parameter. The second element
    is an integer the corresponds to the index position of the specific element
    found within the provided array.

    Parameters
    ----------
    sel_array : list[Any]
        array to be indexed

    Returns
    -------
    list[list[Any, int]]
        list of nested list where nested list contains two elements. The first
        element is the original element from the provided array and the second
        element corresponds to its index position within the provided array.

    Raises
    ------
    ValueError
        Raised if an empty list is provided
    TypeError
        Raised if a non-Sequence type object is provided. Sequence types are
        lists and tuple objects.

    Example
    -------
    >>> ls = ["hello", "world", ":)"]
    >>> indexed_ls = index_list(ls)
    >>> print(indexed_list)
    >>> [["hello", 0], ["world", 1], [":)", 2]]

    """
    # using list comprehension to to generate list of lists
    if not len(sel_array) > 0:
        raise ValueError("Empty list is provided")
    if not isinstance(sel_array, Sequence):
        raise TypeError("sel_arry must be either a list or a tuple array")

    indexed_elements = [[elm, idx] for idx, elm in enumerate(sel_array)]
    return indexed_elements


def read_count_mean(count_array: List[int]) -> float:
    """Returns the mean of a given read count

    Parameters
    ----------
    count_array : List[int]
        array that contains read counts of a given group

    Returns
    -------
    float
        mean value of all counts

    Raises
    ------
    TypeError
        if a non numerical type is captured or a List object is not provided
    """
    # checking data type
    if not isinstance(count_array, List):
        raise TypeError("count_array must be list")

    if len(count_array) == 0:
        print("Warning: Array with no length captured. Mean set to 0")
        return 0

    # checking element types
    for num in count_array:
        if not isinstance(num, int) and not isinstance(num, float):
            _type = type(num)
            msg = f"Only integers and floats allowed, you provided {_type}"
            raise TypeError(msg)

    # calculating mean
    _sum = sum(count_array)
    mean = round(_sum / len(count_array), 2)

    # result
    return mean


def filter_by_mean(
    grouped_read_counts: List[Any],
    threshold: Optional[Union[int, float]] = 0,
) -> List[Union[int, float]]:
    """Filtering read counts based on mean threshold

    Parameters
    ----------
    read_counts : List[Union[int, float]]
        list of read counts

    Returns
    -------
    List[Union[str, int, float]]
        returns a group list of values that meets the threshold.

    Raises
    ------
    TypeError
        Raised if a List is not provided, group name is not found, or read
        counts contain non-numerical datatypes.
    """

    # type checking
    if not isinstance(grouped_read_counts, List):
        raise TypeError("grouped_read_counts must be a list")
    if len(grouped_read_counts) == 0:
        raise ValueError("Empty list is provided")
    if not isinstance(grouped_read_counts[0][0], str):
        raise TypeError("Group name is not found")
    if not isinstance(threshold, int) and not isinstance(threshold, float):
        raise TypeError("threshold must be must be an int or float")

    # iterating through group_counts
    filtered_groups = []
    for grouped_data in grouped_read_counts:

        if len(grouped_data) == 1:
            msg = f"{grouped_data[0]} contains no data"
            continue

        # splitting data group_name and read_counts
        group_name, read_counts = grouped_data[0], grouped_data[1]

        # calculate the mean
        mean = read_count_mean(read_counts)

        # store values if mean is higher than the threshold
        if mean >= threshold:
            result = [group_name, read_counts]
            filtered_groups.append(result)

    return filtered_groups
