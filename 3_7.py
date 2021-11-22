def area(a,b,c):
	p=(a+b+c)/2
	area1=p*(p-a)*(p-b)*(p-c)
	area=area1**0.5
	return area

a = int ( input ( "Введите a:" ))
b = int ( input ( "Введите b:" ))
c = int ( input ( "Введите c:" ))
print("Площадь треугольника "area(a,b,c))