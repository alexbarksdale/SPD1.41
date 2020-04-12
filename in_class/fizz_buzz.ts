function FizzBuzz(n: number): string[] {
    let output = [];
    for (let i = 1; i < n + 1; i += 1) {
        if (i % 15 === 0) output.push('FizzBuzz');
        else if (i % 3 === 0) output.push('Fizz');
        else if (i % 5 === 0) output.push('Buzz');
        else output.push(i.toString());
    }
    return output;
}
console.log(FizzBuzz(15));

/*
 * Bad
function FizzBuzz(targetnum)
{
    for (var i=1; i < targetnum; i++;) {
        let result = "";
        if (i%3 === 0) result += "FizzBuzz";
        if (i%5 === 0) result += "Buzz";
        if (i%3 > 0 && i%5 > 0) result = i
        console.log(result += "\n");
    }
}
*/

