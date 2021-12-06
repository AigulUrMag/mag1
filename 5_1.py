class StringVar:
	def __init__(self,str1) :
		self.str1=str1
	def set(self,str1) :
		return str1.upper()
	def get(self,str1) :
		return str1
str2= StringVar("Hello ")
print(str1.set("good by"))
print(str1.get("Hello"))


