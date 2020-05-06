'''
QUESTION:
Implement function ToLowerCase() that has a string parameter str, and 
returns the same string in lowercase.

Example: Hello -> hello

Time complexity: O(n) where n is the amount of characters in a string
'''

from typing import List


def toLowerCase(str):
    output = ""
    # n characters
    for char in str:
        if ord(char) >= 65 and ord(char) <= 90:
            output += chr(ord(char)+32)
        else:
            output += char
    return output


T1 = 'Bob'
print(toLowerCase(T1))


'''
QUESTION:
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together. 
Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of
weight y has new weight y-x.
At the end, there is at most 1 stone left.  
Return the weight of this stone (or 0 if there are no stones left.)

Time complexity: O(n + nlogn) where n is the amount of items in the collection and nlogn 
is the cost of using .sort()
'''


def lastStoneWeight(stones: List[int]) -> int:
    # n items in the stones
    for _ in range(len(stones) - 1):
        stones.sort()  # nlogn
        temp = stones[-1] - stones[-2]
        stones[-1], stones[-2] = temp, -1
    return (stones[-1])


T2 = [2, 7, 4, 1, 8, 1]
print(lastStoneWeight(T2))
