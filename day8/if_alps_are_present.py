'''qwweer yuiop asdfvgh JL mnbvlkjcxz
no'''

'''n=input()
s=set(n)
if len(s)==27:
    print("yes")
else:
    print("no")'''


n=input()
s="abcdefghijklmnopqrstuvwxyz"
for i in s:
    if i not in n:
        print("no")
        break
else:
    print("yes")
            

n=input()
for i in range(97,123):
    if chr(i) not in n:
        print("no")
        break
else:
    print("yes")
    

a=input()
d=set()
for i in a:
    if i.islower():
        d.add(i)
print(d)


a=input()
d=[0]*26
for i in a:
    if i.islower():
        d[ord(i)-97]=1
print(all(d))



    


