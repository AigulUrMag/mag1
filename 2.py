s=109
v=int(input("Введите скорость:"))
t=int(input("Введите время:"))
s1=v*t
if s1<s:
   print('Байкер проехал',s1) 
else: 
   s2=int(s1/s)
   print('Байкер проехал',s1-s*s2)
