# problem link : https://codeforces.com/problemset/problem/231/A
# converting the number into list 



class Solution :
    # count frequency of 1 and 0
    # for this purpose we can use hashmap
    def count10(self,n):
     if n.count(1)>=2:
        return True
     return False

        
    

if __name__=="__main__":
    sol=Solution()
    n=int(input())
    count:int=0

    for _ in range(n):
       nums = list(map(int,input().split()))
       if sol.count10(nums):
          count+=1
    print(count)
    







