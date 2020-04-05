/*
QUESTION:
Given a list of sorted characters letters containing only lowercase letters,
and given a target letter target, find the smallest element in the list that
is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and
letters = ['a', 'b'], the answer is 'a'.
*/

/*
COMMUNICATION STEPS:
- So I'm supposed to iterate over a list to find the very first greater value character?
- Do I need to return it in a specific way such as capitalized or in an array?
- What do I return if there target value isn't found?
[Refer to comments in the code for the rest]

PSEUDO
- Create a function that takes in a list of characters and target
- Have a low and high value since I'm going to use binary search
- Have a condition where low is <= high 
- Calculate the middle value 
- Have a series of checks to move the boundaries
- Return first character if not found or the character if found
*/

function find_smallest_el(arr: string[], target: string): string {
    // low and high values to set the boundaries
    let low = 0;
    let high = arr.length - 1;
    let ans = 0; // Holds the position of the first greatest value if found

    while (low <= high) {
        // Calculates the middle of the array
        let mid = low + (high - low) / 2;

        // Enters if we found a value greater than the target
        if (arr[mid] > target) {
            ans = mid; // Set the answer value to the greater value at mid
            high = mid - 1; // There could still be a greater first value, so move left
        } else {
            low = mid + 1; // Didn't find a correct value, move right
        }
    }
    return arr[ans];
}

const T1 = ['c', 'f', 'j'];
const find_val = 'f'; // should return 'j'

console.log(find_smallest_el(T1, find_val));
