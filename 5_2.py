class Point():
	def __init__(self,x,y) :
		self.x=x
		self.y=y
	def __sub__(self,other) :
		return Point(other.x-self.x,other.y-self.y)
	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)
	def __mul__(self, other):
		return self.x * other.x + self.y * other.y
	def len(self,other):
		return (((other.x-self.x)**2)+((other.y-self.y)**2))**0.5
p1=Point(1,1)	
p2=Point(2,2)
r1=p2-p1
print(r1.x,r1.y)
r2=p1+p2
print(r2.x,r2.y)
r3=p2*p1
print(r3)
print(p2.len(p1))

