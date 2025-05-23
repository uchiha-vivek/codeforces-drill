# Q1: How many words can be formed by using 3 letters from the word "DELHI"? 
from itertools import permutations

word:str = 'delhi'
length:int = 3

perms= permutations(word,length)

words= [''.join(p) for p in perms]
print(f'the count is : {len(words)}')
print(words)