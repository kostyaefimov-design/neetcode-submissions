class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [s[i].lower() for i in range(len(s)) if s[i].isalpha() or s[i].isdigit()]
        return s[::-1] == s

"""def isPalindrome(s: str):
    s = [s[i].lower() for i in range(len(s)) if s[i].isalpha() or s[i].isdigit()]
    left = 0
    right = len(s) - 1
    for i in range(len(s)):
        if s[left] == s[right]:   
            left +=1
            right -= 1
        else:
            return False
    return True   
print(isPalindrome("0P")) """