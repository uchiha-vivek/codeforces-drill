# String problem
# Problem Link : https://codeforces.com/problemset/problem/59/A
class Solution:
    def count_length(self,char:str)->int:
        return len(char)
    
    # counting the nummber  of uppercase and lowercase
    # ViVek
    # lower --> i,e,k count=3
    # upper --> V,V count=2
    def count_upper_and_lower_cases_logic1(self,text:str)->str:
        upper:int = sum(1 for ch in text if ch.isupper())
        lower:int =sum(1 for ch in text if ch.islower())
        
        # start building the cases
        # if upper count is same as lower count
        # Time complexity : O(N)  two iterations for upper and lower
        # space complexity : .lower() and .upper() return copy of string --> O(N)
        if upper==lower:
            return text.lower()
        # codeforces example -->HoUse must be replaced with house
        elif lower>upper:
            return text.lower()
        # codeforces example --> ViP — with VIP. 
        else:
            return text.upper()
    
    # logic2 
    def count_upper_and_lower_cases_logic2(self,text:str)->str:
        upper:int = sum(1 for ch in text if ch.isupper())
        lower:int =sum(1 for ch in text if ch.islower())
        # reducing the cases from previous logic
        if upper>lower:
            return text.upper()
        else:
            return text.lower()


if __name__=="__main__":
    sol=Solution()
    char:str = input('Enter the character :')
    ans:int= sol.count_upper_and_lower_cases_logic1(char)
    ans1:int =sol.count_upper_and_lower_cases_logic2(char)
    print(ans1)