class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for word in strs:
            ans += word + "\n"
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        curr = ""
        for letter in s:
            if letter == "\n":
                ans.append(curr)
                curr = ""
            else:
                curr += letter
        return ans
