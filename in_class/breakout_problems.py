'''
Given a list of n numbers, determine if it contains any duplicate numbers.

PSEUDO: The basic approach
- Have an array that'll store the numbers
- iterate through the numbers given
- Check if the number is in the non_dup array
- return false if there is a duplicate. True otherwise.
'''


def check_dup(num):
    non_dup = []

    for i in range(len(num)):
        if num[i] not in non_dup:
            non_dup.append(num[i])
        else:
            return False
    return True


T1 = [1, 2, 3, 4, 5, 5]
print(check_dup(T1))


'''
Find the middle item in a singly linked list

PSEUDO: Basic approach
- Have two pointers. One leader and a follower.
    - Leader goes ahead two steps
    - Follower who's right behind
- Loop until the leader is not None since that pointer will be ahead
'''


# ... assuming we have a working LL file
def find_middle_item(self):
    follower = self.head
    leader = self.head

    if self.head is None:
        return 'List is empty'

    while leader is not None and leader.next is not None:
        leader = leader.next.next
        follower = follower.next
    print("Middle Item: ", follower.data)
