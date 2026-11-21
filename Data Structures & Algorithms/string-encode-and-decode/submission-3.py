class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            res += str(len(word)) + '#' + word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            separator = s.index('#', i)
            length = int(s[i:separator])
            start = separator + 1
            end = start + length

            res.append(s[start:end])
            i = end

        return res