class Voin():
	def __init__(self,health): 
		self.health=health
			
	def ataka(self) :
		if self.health>20:
			self.health-=20
			return self.health
		else :	
			self.health=0
		return self.health	
unit1=Voin(100)
unit2=Voin(100)
while unit2.health!=0 and unit1.health!=0 :
	n=input("Введите 1 или 2 ")
	if n=='1' :
		print(n)
		unit2.ataka()
		print("Атаковал первый,осталось здоровья у второго ",unit2.health)
	else :
		print(n)
		unit1.ataka()
		print("Атаковал второй,осталось здоровья у первого", unit1.health)
else :
	print("Игра закончена")	
if unit2.health==0 		:
	print("Выиграл первый игрок")	
else:
	print("Выиграл второй игрок")		
