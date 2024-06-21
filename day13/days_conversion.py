days=int(input())
y=days//360
days=days%360
m=days//30
days=days%30
w=days//6
d=days%6
print(f"{y}:{m}:{w}:{d}")
