


# extracting first word
# vivek sharma dev
#  vsd

test_cases:int  = int(input())
for _ in range(test_cases):
    a,b,c = input().split()
    # concateneate the first alphabet
    print(a[0]+b[0]+c[0])