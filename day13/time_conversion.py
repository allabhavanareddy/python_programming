'''ip:7262 sec
op:2h:1m:2s'''
n=int(input())
h=n//3600
s=n%3600
m=s//60
s=s%60
print(f"{h}h:{m}m:{s}s")
