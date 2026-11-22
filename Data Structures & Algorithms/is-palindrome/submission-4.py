class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1
        while start < end:
            #if the start is not an alpha numeric
            while start < end and not s[start].isalnum():
                start += 1

            #if the end if not an alpha numeric
            while start < end and not s[end].isalnum():
                end -= 1

            #compare characters
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True
