# problem link : https://codeforces.com/problemset/problem/472/A

# 12 -> x+y here both x and y are composite
# probably a check also needs to be made whether  x and y is composite
# first smallest composite number is 4


class Solution:
    def isComposite(self,num:int)->bool:
        if num <=3:
            return False
        
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return True
        return False
    
    # 12 --> (4,8)/ (6,6)
    def composite_pair(self,num:int):
        for i in range(4,(num//2)+1):
            if self.isComposite(i) and self.isComposite(num-i):
                return (i,num-i)
        return None

if __name__=="__main__":
    sol=Solution()
    num = int(input())
    print(sol.composite_pair(num))

