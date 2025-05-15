import time
import tracemalloc

# f(a, b) = a + b = n
# Function to find number of pairs (excluding 0)


# finding all the different paris
def pair(number:int):
    pairs=[]
    for a in range(1,number):
        b=number-a
        if b>=1:
            pairs.append((a,b))
    return pairs

# find the pair numbers
def number_of_pairs(number:int):
    return number-1

test_case:int = int(input())
tracemalloc.start()
start_time = time.time()
for _ in range(test_case):
    number:int = int(input())
    result = number_of_pairs(number)
    print(result)

end_time = time.time()
current,peak= tracemalloc.get_traced_memory()
tracemalloc.stop()


print(f"\nExecution Time: {end_time - start_time:.6f} seconds")
print(f"Current Memory Usage: {current / 1024:.2f} KB")
print(f"Peak Memory Usage: {peak / 1024:.2f} KB")
