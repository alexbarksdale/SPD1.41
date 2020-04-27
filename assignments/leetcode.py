'''
PROBLEM:
https: // leetcode.com/problems/decompress-run-length-encoded-list/

QUESTION:
We are given a list nums of integers representing a list compressed with run-length encoding.
For each such pair, there are freq elements with value val concatenated in a sublist.
Concatenate all the sublists from left to right to generate the decompressed list.
Return the decompressed list.

TEST CASES:
- [2, 4, 4, 4]
T2 = [1, 1, 2, 3]
- [1, 3, 3]

VARIABLE TRACE:
T1 = [1, 2, 3, 4]

iteration: 0 | T1 = []
iteration: 1 | T1 = [2]
- First pair: [1, 2] freq = 1 & val = 2 == = [2]
iteration: 2 | T1 = [2, 4, 4, 4]
- Second pair: [3, 4] freq = 3 & val = 4 == = [4, 4, 4]
return [2,4,4,4]
'''

from typing import List


def decompressRLElist(nums: List[int]) -> List[int]:
    decom_list = []  # hold the decompressed values
    for i in range(1, len(nums), 2):
        decom_list += [nums[i]]*nums[i-1]
    return decom_list


T1 = [1, 2, 3, 4]
print(decompressRLElist(T1))


'''
PROBLEM:
Jewels and Stones
https: // leetcode.com/problems/jewels-and-stones/

QUESTION:
You're given strings J representing the types of stones that are jewels, and
S representing the stones you have.  Each character in S is a type of stone you have.
You want to know how many of the stones you have are also jewels.
The letters in J are guaranteed distinct, and all characters in J and S are letters.
Letters are case sensitive, so "a" is considered a different type of stone from "A".

TEST CASES:
J = "aA"
S = "aAAbbb"
Result: 3

J = "z"
S = "ZZ"
Result: 0

VARIABLE TRACE:
J = "aA"
S = "aAAbbb"
Result: 3

iteration: 0 | jewel_count = 1
iteration: 1 | jewel_count = 2
iteration: 2 | jewel_count = 3
iteration: 3 | jewel_count = 3
iteration: 4 | jewel_count = 3
iteration: 5 | jewel_count = 3
iteration: 6 | jewel_count = 3
return 3
'''


def numJewelsInStones(J: str, S: str) -> int:
    jewel_count = 0

    for char in S:
        if char in J:
            jewel_count += 1
    return jewel_count


J = "aA"
S = "aAAbbbb"

print(numJewelsInStones(J, S))
