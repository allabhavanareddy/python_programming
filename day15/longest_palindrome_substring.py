'''abdbsdabca
  longest palindrome substring'''

s="abnsdabca"
l=[]
for i in range(len(s)):
    sub=""
    for j in range(i,len(s)):
        sub=sub+s[j]
        l.append(sub)
print(l)

m=0
long=""
for word in l:
    f=1
    for i in range(len(word)//2):
        if word[i]!=word[len(word)-1-i]:
            f=0
            break
    if f==1 and len(word)>len(long):
        long=word
print(long)
        
        
            
            

