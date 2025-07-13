class Solution:
    def reverseVowels(self, s: str) -> str:
        l=0
        r=len(s)-1
        s=list(s)
        while l<r:
            if s[l] in 'AEIOUaeiou':
                if s[r] in 'AEIOUaeiou':
                    s[l],s[r]=s[r],s[l]
                    l+=1
                    r-=1
                else:
                    r-=1
            else:
                l+=1
        s=''.join(s)
        return s
        