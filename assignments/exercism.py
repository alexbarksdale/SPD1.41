'''
Exercism problem: Nth Prime
Given a number n, determine what the nth prime is.

POSSIBLE TEST INPUTS
6 - 2, 3, 5, 7, 11, 13
10 - 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
15 - 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47

PSEUDO
- Check if number is a negative
- Init a list with 2 since we know that's a prime number
- Have a number check variable
- Loop until the list is less than the number we input
- Iterate over the list and check if the number is prime (% == 0)
    - otherwise append
- Increment the number check by 2 since we don't have to check for primes
- Return the last number (nth)
'''


def nth_prime(number):
    if number < 0:
        raise ValueError('Prime numbers can\'t be negative numbers')

    # initial prime number list
    prime_numbers = [2]
    num_check = 3  # first value to check
    while len(prime_numbers) < number:
        for p in prime_numbers:
            # Check if the number is not prime
            if num_check % p == 0:
                break
        else:
            prime_numbers.append(num_check)
        num_check += 2  # don't need to check even numbers
    print(prime_numbers)
    return prime_numbers[-1]  # last prime num


# nth_prime stuff
TestCase = 10  # Expected: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
EdgeCase = -5  # Expected: Error: Prime numbers can't be negative numbers
print(nth_prime(TestCase))
# print(nth_prime(EdgeCase))

'''
Exercism problem: Pangram

Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan gramma, "every letter")
is a sentence using every letter of the alphabet at least once.

POSSIBLE TEST INPUTS
FALSE - 'The goat jumped over the goat'
TRUE - 'The five boxing wizards jump quickly'
FALSE - 'The flying flamingoz went to quibo land'

PSEUDO
- Create a variable with the alphabet
- Remove spaces from the input
- Iterate over the alphabet and check if the character is in the string given
- Return true or false

OR

- Put the string into the set since a set doesn't have duplicates
- Check if the length is greater than 26 since there are 26 letters in the alphabet
- Return true or false
'''


def check_pangram(string):
    # Put the string into a set to remove duplicates, remove spaces and lowercase
    string_set = set(string.lower().replace(' ', ''))
    # Check if the set is greater than 26 (contains all characters)
    return len(string_set) >= 26


TestCase2 = 'The five boxing wizards jump quickly'
EdgeCase2 = 'The flying flamingoz!!@3 went%$! to quibo*& land'
print(check_pangram(TestCase2))  # True
print(check_pangram(EdgeCase2))  # False not because of the non ascii though
