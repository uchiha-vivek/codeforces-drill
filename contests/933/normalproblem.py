import time
import tracemalloc


def rotation(a:str)->str:
    # when i see p --> q and vice-versa and w will remain same
    word:list[str]=[]
    for  char in a:
        if char =="p":
            word.append('q')
        elif char=='q':
            word.append('p')
        else:
            word.append(char)
            
    final_word = ''.join(word)[::-1]
    return final_word

t:int = int(input())

for _ in range(t):
    a:str = input()
    result = rotation(a)
    print(result)
