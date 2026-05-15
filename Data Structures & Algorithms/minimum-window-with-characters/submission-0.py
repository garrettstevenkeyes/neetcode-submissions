class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #edge case
        if t == "": return ""

        countT, window = {}, {}
        #init our count t map
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        #init our have need counts
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        #iterate chars
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                #update res
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = (r-l+1)
                
                #shrink from the left of window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""