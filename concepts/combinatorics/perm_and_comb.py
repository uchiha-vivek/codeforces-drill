# finding permutation and combination of a number
import math

n:int = 5
r:int = 2

# combination
nCr :int = math.comb(n,r)

# permuatation
nPr:int = math.perm(n,r)

print(f'combination is : {nCr}')
print(f'permuatation is : {nPr}')