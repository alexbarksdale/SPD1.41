/*
QUESTION:
Given a non-negative integer num, return the number of steps to
reduce it to zero. If the current number is even, you have to
divide it by 2, otherwise, you have to subtract 1 from it.
*/

/*
COMMUNICATION STEPS:
- So I need to return (x) amount of steps it takes to reduce a number to zero
and if the current number I'm on in the iteration is even I have to divide by 2 
otherwise I need to subtract 1?
- Are the the numbers in sorted order?

PSEUDO
- Have a function take in a number
- Have a variable that tracks the steps
- Have a variable that is === to the num to avoid mutating the original value
- Have a while loop until the value is 0
- Have a series of checks to see if I need to divide by 2 or subtract 1
- Return the steps
*/

function numberOfSteps(num: number): number {
    let steps = 0; // tracks the # of steps
    let red_num = num; // avoids mutating the original value

    while (red_num > 0) {
        // Checks to see if the current number is divisible by 2
        if (red_num % 2 === 0) {
            // divides the number by 2
            red_num /= 2;
        } else {
            // If it's not divisible by 2 then we have to substract 1 from it
            red_num -= 1;
        }
        // Always increases the steps since either condition will always happen
        steps += 1;
    }
    return steps;
}

const T2 = 14;
console.log(numberOfSteps(T2)); // This should be 6 steps to get to 0
