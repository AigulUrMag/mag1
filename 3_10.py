def register(login,passwd) :
	data={'login':'passwd'}
	import json
	#with open('log.json', 'w') as f:
	#	json.dump(data,f)
	with open('log.json', 'r') as f:
		data=json.load(f)
		if login not in data.keys():
			data[login]=passwd
			with open('log.json', 'w') as f:
				print('ok')
				json.dump(data,f)
		else :
			print( "Введите логин снова") 		

def login_function(login,passwd):
	data={'login':'passwd'}
	import json
	with open('log.json', 'r') as f:
		data=json.load(f)
		print(data)
		if login in data.keys():
			if data[login] == passwd:
				print('Удачный вход')
			else : 	
				print('Введите пароль заново')
		else :
			print( "Введите логин снова") 		


#data={'login':'password'}
while True:
	login=input('Введите логин ')
	passwd=input('Введите пароль ')
	#register(login,passwd)	
	login_function(login,passwd)

