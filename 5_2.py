class Point():
	def __init__(self,x,y) :
		self.x=x
		self.y=y
	def __sub__(self,other) :
		return Point(abs(other.x-self.x),abs(other.y-self.y))
	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)
	def __mul__(self, other):
		return self.x * other.x + self.y * other.y
	def len(self):
		return (self.x ** 2 + self.y ** 2) ** 0.5
p1=Point(1,9)	
p2=Point(4,6)
r1=p2-p1
print(r1.x,r1.y)
r2=p1+p2
print(r2.x,r2.y)
r3=p2*p1
print(r3)
print(p1.len())

