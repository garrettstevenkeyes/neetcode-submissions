class Solution:
    def isPalindrome(self, s: str) -> bool:
        # init start and end
        start = 0
        end = len(s) -1
        # iterate from front and back
        while start < end:
            #check it the character is a alphnumeric front and back
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1

            if not start < end:
                break

            #check equality
            if s[start].lower() != s[end].lower():
                return False

            #move both pointers
            start += 1
            end -= 1

        #return true at the end
        return True