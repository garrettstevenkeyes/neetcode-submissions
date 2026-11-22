class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += (str(len(word))+ '#' + word)
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            length = ""
            while s[i] != "#":
                length += s[i]
                i += 1

            start = i + 1  # Skip the "#"
            end = start + int(length)
            res.append(s[start:end])
            i = end

        return res