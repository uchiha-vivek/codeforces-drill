# https://codeforces.com/contest/1999/problem/A

# function to do sum of digits
def summation(num:int):
    sum_of_digit = sum(int(digit) for digit in str(num))
    return sum_of_digit


t:int = int(input())

for _ in range(t):
    num:int = int(input())
    ans = summation(num)
    print(ans)