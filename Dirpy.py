import os,time
k=0
while k<4:
	print(" ")
	print ("    	1. Current Dir")
	print("   	2. Create a file")
	print("        3. Remove a file ")
	print("    	4. Rename a file ")
	print("        5. Terminal")
	print("  	6. Exit")
	menu=input("	Enter the choices >>  ")
	
	
	if menu=="1":
		i=1
		while i<5:
			path=os.getcwd()
			print(path,'\n')
			print("	Type 'ls'to list the directios")
			print("	Type'cd'to changpe directios")
			gh=input('      >>')
			mm=gh
			hh=gh[:2]
			mm=mm[3:]
			
			if hh in "ls":
				try:
	
					kk=os.listdir()
					for rang in kk:
						print('         ',rang)
					print('\n')
				except PermissionError as j:
						print(j)
				
			elif hh in "cd":
				try:
					os.chdir(mm)
				except FileNotFoundError as ll:
					print(ll)
			elif gh in "exit":
				i=8
			
		time.sleep(2)
		os.system('clear')
		
	elif menu=="2":
		try:
			cre=input("		File name >>")
			os.mkdir(cre)
			print('     	  The File has been with name',cre)
			time.sleep(2)
			os.system('clear')
		except FileExistsError as h:
			print(h)
			time.sleep(3)
			os.system('clear')	
		
		
	elif menu=="3":
		try:
			rem=input("		File name >>")
			os.rmdir(rem)
			time.sleep(2)
		except FileNotFoundError as e:
			print(e)
			time.sleep(4)
		os.system('clear')
			
			
	elif menu=="4":
		try:
			em=input("		File name >>")
			ren=input("		New File name >>")
			os.rename(em,ren)
			time.sleep(2)
		except FileNotFoundError as t:
			print(t)
			time.sleep(4)
			os.system('clear')
			
			
	elif menu=="5":
		i=0
		while i<1:
			ter=input(">>$")
			if ter in "ls":
				h=os.getcwd()
				print(h)
				
			elif ter in "exit":
				time.sleep(2)
				i=5
			else:
				os.system(ter)
				time.sleep(2)
		os.system('clear')
	elif menu=="6":
				print("				Thank you")
				time.sleep(2)
				k=8
				os.system('clear')
		
	else :
			print("             Invaild choice")
			time.sleep(2)
			print(" ")
			os.system('clear')
	