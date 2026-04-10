class Solution:

    def encode(self, strs: List[str]) -> str:
        decode = ""
        for s in strs:
            decode += str(len(s)) + "#" + s
        return decode        

    def decode(self, s: str) -> List[str]:
        encode, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            encode.append(s[j+1 : j+1+length])
            i = j+1+length
        return encode
