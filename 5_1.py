lass StringVar:
	def __init__(self,str1) :
		self.str1=str1
	def set(self,str1) :
		self.str1=str1
		return self.str1
	def get(self,str1) :
		return str1
str2= StringVar("Hello ")
print(str2.set("good by"))
print(str2.get("Hello"))

