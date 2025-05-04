# problem link : https://codeforces.com/problemset/problem/339/A
# string and sorting
# we have 3+2+1 and we need to convert it into 1+2+3



class Solution:
    def splitchar(self,char:str):
        number = char.split('+') # Here we get a list of numbers which are string ['1','2']
        register  = [int(num) for num in number]
        register.sort()  # nlogn
        sorted_register_string:str = '+'.join(str(num) for num in register)
        return sorted_register_string


if __name__=="__main__":
    sol=Solution()
    char:str = input()
    ans = sol.splitchar(char)
    print(ans)