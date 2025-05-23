

# method1
import math

def checkprime1(n:int):
    if n==2 or n==3:
        return True
    elif n<=1 or n%2==0 or n%3==0:
        return False
    
    for i in range(5,int(math.sqrt(n))+1,6):
        # 11 --> 5,
        if n%i==0 or n%(i+2)==0:
            return False

    return True

# method 2:
def checkprime2(n:int):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True


if __name__=='__main__':
    print(checkprime1(10))
    print(checkprime2(19))