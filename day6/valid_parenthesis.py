'''s=input()
st=[]
for i in s:
    if i=="{" or i=="(" or i=="[":
        st.append(i)
    else:
        if not st:#checs if it is empty
            print("False")
        elif i==')' and st[-1]=='(':
            st.pop()
        elif i==']' and st[-1]=='[':
            st.pop()
        elif i=='}' and st[-1]=='{':
            st.pop()
        else:
            print(s.index(i)+1)
            
               
if not st:
    print(-1)'''



s=input()
st=[]
f=0
c=0
for i in s:
    if i=="{" or i=="(" or i=="[":
        st.append(i)
    elif not s:
        if i==')' and st[-1]=='(' or  i==']' and st[-1]=='[' or i=='}' and st[-1]=='{':
            st.pop()
        else:
            print(c)
            f=1
            break
    else:
        print(c)
        f=1
            
               
if f==0:
    print(-1)


        