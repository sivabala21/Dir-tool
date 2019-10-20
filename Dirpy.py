import os,time
k=0
red="\033[31m"
green="\033[32m"
yellow="\033[33m"
de="\033[0m"
while k<4:
	print("\033[32m ")
	print ("    	1. Current Dir")
	print("   	2. Create a file")
	print("        3. Remove a file ")
	print("    	4. Rename a file ")
	print("        5. Terminal")
	print("  	6. Exit \033[0m")
	menu=input("	Enter the choices >>  ")
	
	
	if menu=="1":
		i=1
		while i<5:
			path=os.getcwd()
			print(path,'\n\n')
			print(yellow,'''       Type 'ls'to list the directios''')
			print("	Type'cd'to change directios ",de)
			gh=input('      >>')
			mm=gh
			hh=gh[:2]
			mm=mm[3:]
			
			if hh in "ls":
				try:
	
					kk=os.listdir()
					print("\n\n")
					for rang in kk:
						print('         ',rang)
					print('\n')
				except PermissionError as j:
						print(red,j,de)
				
			elif hh in "cd":
				try:
					os.chdir(mm)
				except FileNotFoundError as ll:
					print(red,ll,de)
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
			print(red,h,de)
			time.sleep(3)
			os.system('clear')	
		
		
	elif menu=="3":
		try:
			rem=input("		File name >>")
			os.rmdir(rem)
			time.sleep(2)
		except FileNotFoundError as e:
			print(red,e,de)
			time.sleep(4)
		os.system('clear')
			
			
	elif menu=="4":
		try:
			em=input("		File name >>")
			ren=input("		New File name >>")
			os.rename(em,ren)
			time.sleep(2)
		except FileNotFoundError as t:
			print(red,t,de)
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
				print(	yellow,"\n\n	Thank you",de)
				time.sleep(2)
				k=8
				os.system('clear')
		
	else :
			print(red,"             Invaild choice",de)
			time.sleep(2)
			print(" ")
			os.system('clear')
	