"""Assignment 1

Fill in the following function skeletons - descriptions are provided in 
the docstring (the triple quote thing at the top of each function)

Some assert statements have been provided - write more of them to test your code!

The `raise NotImplementedError(...)`s are placeholders to help you not skip implementing
a function. They should be removed and replaced with your solution.

This portion of the assignment will not be graded, but this gives you some problems to 
check, if you do not complete the generative AI portion of the assignment.
"""

from typing import List, TypeVar


def absolute(n: int) -> int:
    if(n<0):
        return -n
    return int 


def factorial(n: int) -> int:
    total = 1
    while(n>1):
        total*=n
        n-=1
    return total

T = TypeVar("T")


def every_other(lst: List[T]) -> List[T]:
    return lst[::2]


def sum_list(lst: List[int]) -> int:
    total = 0
    for x in lst:
        total += x
    return total


def mean(lst: List[int]) -> float:
    mean = 0
    for x in lst:
        mean+=x
    return mean/len(lst)

def median(lst: List[int]) -> float:
    n = len(lst)
    if(n%2==1):
        return lst[int(n/2)]
    return ((lst[n/2]+lst[(n/2)+1]/2))


def duck_duck_goose(lst: List[str]) -> List[str]:
    index = 0  # Start counting from the first index
    
    while len(lst) > 2:
        # Calculate the index of the name to be removed
        index = (index + 2) % len(lst)  # +2 because we count the third name
        
        # Remove the name at the calculated index
        lst.pop(index)
    
    return lst


# this line causes the nested code to be skipped if the file is imported instead of run
if __name__ == "__main__":
    assert absolute(-1) == 1, "absolute of -1 failed"
    assert factorial(4) == 24, "factorial of 4 failed"
    assert every_other([1, 2, 3, 4, 5]) == [
        1,
        3,
        5,
    ], "every_other of [1,2,3,4,5] failed"
    assert sum_list([1, 2, 3]) == 6, "sum_list of [1,2,3] failed"
    assert mean([1, 2, 3, 4, 5]) == 3, "mean of [1,2,3,4,5] failed"
    assert median([1, 2, 3, 4, 5]) == 3, "median of [1,2,3,4,5] failed"

    names = ["roscoe", "kim", "woz", "solin", "law", "remess"]
    assert duck_duck_goose(names) == ["roscoe", "law"]

    print("All tests passed!")