def lengthOfLastWord(self, s: str) -> int:
        r=s.split()
        max=len(r[0])
        for i in range(1,len(r)):
            if len(r[i])>max:
                max=len(r[i])
        return max
