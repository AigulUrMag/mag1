class Voin():
	
	health=100
	#health2=100
	
	def ataka(self) :
		if health>20:
			self.health-=20

unit1=Voin()
unit2=Voin()
print(unit1.health)
print(unit2.health)
#while unit1.ataka.health2>0
n=input("Введите 1 или 2")
if n==1 :
	unit2.ataka()
	print("Атаковал первый,осталось здоровья у второго ",unit2.health)
else :
	unit1.ataka()
	print("Атаковал второй,осталось здоровья у первого", unit1.health)