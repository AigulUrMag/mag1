while True:
	password=str(input('Введите пароль:  '))
	len1=len(password)
	if len1<8:
		print ('   Введите пароль заново')
	else:
		a=1
		i=0
		b=0
		while a<len1:
			if str(password[a-1]) not in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
				print ('   Введите пароль заново')
				break
			else :
				if str(password[a-1]) in 'qwertyuiopasdfghjklzxcvbnm':
					i=i+1
				if str(password[a-1]) in 'QWERTYUIOPASDFGHJKLZXCVBNM':
					b=b+1
				a=a+1	
		else:
			if i!=0 and b!=0 :
				print ('Пароль верен ')
				break
			else: 	
				print ('   Введите пароль заново')

