import itertools

items=[1,2,3]

comnbinations = list(itertools.combinations(items,2))
permutations = list(itertools.permutations(items,2))
print(f'Combinations : {comnbinations}')
print(f'Permutations : {permutations}')