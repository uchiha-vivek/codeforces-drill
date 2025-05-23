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
tracemalloc.start()
start_time = time.time()
for _ in range(t):
    a:str = input()
    result = rotation(a)
    print(result)

end_time = time.time()
current,peak= tracemalloc.get_traced_memory()
tracemalloc.stop()


print(f"\nExecution Time: {end_time - start_time:.6f} seconds")
print(f"Current Memory Usage: {current / 1024:.2f} KB")
print(f"Peak Memory Usage: {peak / 1024:.2f} KB")
