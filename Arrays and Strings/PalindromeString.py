def palindromecheck(s:str):
    for i in range(0,((int)(len(s)/2))):
        start=0
        end=len(s)-1-i
        if s[start]!=s[end]:
            return False
        return True
str1=input("Enter string")
print(palindromecheck(str1))
    