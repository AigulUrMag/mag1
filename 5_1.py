class StringVar(str):
	def __init__(self,str) :
		self.str=str
	def set(self,str) :
		return str.upper()
	def get(self,str) :
		return str
str1= StringVar("Hello ")
print(str1.set("good by"))
print(str1.get("Hello"))


