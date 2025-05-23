# How many words can be formed by using the letters from the word "DRIVER" such that all the vowels are always together? 
# vowels are i and e --> treat i and e together
# r is repeating two times
from itertools import permutations
import math

 
# fining count of vowels

 
 
import math
from itertools import permutations

def count_vowels(word):
    vowels = 'aeiou'
    count = 0
    for char in word.lower():
        if char in vowels:
            count += 1
    return count

def required_permutation(word):
    required_length = len(word) - 1
    perms = set(permutations(word, required_length))  # unique permutations
    count_of_vowels = count_vowels(word)
    answer = len(perms) * math.factorial(count_of_vowels)
    return answer

if __name__ == "__main__":
    word = input('Enter the word: ')
    ans = required_permutation(word)
    print("Required permutation count:", ans)
