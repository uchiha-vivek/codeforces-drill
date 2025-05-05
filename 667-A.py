# problem link : https://codeforces.com/problemset/problem/677/A

n,h = map(int,input().split())
a = list(map(int,input().split()))


total_width:int=0

for height in a :
    if height>h:
        total_width+=2
    else:
        total_width+=1
    
print(total_width)