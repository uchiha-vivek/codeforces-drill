


def replace_singular_with_plural(word:str,replacement:str):
    index = word.rfind('us')
    # if that string is present
    if index != -1:
        return word[:index] + replacement + word[index+2:]
    return word


test_case:int = int(input())
for _ in range(test_case) :
    word = input()
    ans:str=  replace_singular_with_plural(word,'i')
    print(ans)