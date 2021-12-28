import os
print('''
,--.  ,--.               ,--.                                   ,--.   
|  '--'  | ,--,--. ,---. |  ,---.  ,---.,--.--.,--. ,--.,---. ,-'  '-. 
|  .--.  |' ,-.  |(  .-' |  .-.  || .--'|  .--' \  '  /| .-. |'-.  .-' 
|  |  |  |\ '-'  |.-'  `)|  | |  |\ `--.|  |     \   ' | '-' '  |  |   
`--'  `--' `--`--'`----' `--' `--' `---'`--'   .-'  /  |  |-'   `--'   
                                               `---'   `--'           ''')
print("Hey there, I am Hashcrypt :v")
        
text = ("""          
        
|----------------------------------|
|\033[32mOkay then lets try it manually\033[31m :) \033[0m|
|----------------------------------|

""")
ver2 = str(input("\033[32m\nDo have a .txt file of the Hashes?(Y/n/quit): " + "\033[0m"))

if ver2 == 'Y':
	fuckyou = str(input("\033[32m\nEnter file path :" + "\033[0m"))
	os.system("python3 Hashcrypt -f " + fuckyou)
	input("\nPress Enter to continue")
	os.system("clear")
	os.system("python3 crypto.py")
	
		
elif ver2 == 'quit':
	print("\033[31m\nThank You, exiting")
	os.system("exit")           
elif ver2 == 'n' :
	print(text)
	ver1 = str(input("\033[32mPlease enter the Hash here: " + "\033[0m"))
	print("""	
|----------------------------------------------------------|
|  1.Normall Hash identification.                          |
|__________________________________________________________|
|  2.Hash identification as JSON format.                   |
|__________________________________________________________|
|  3.Hash identification with Base64 decoder.              |
|__________________________________________________________|
|  4.Hash identification (Accessible mode).                |
|__________________________________________________________|
|  5.Hash identification within a string.                  |
|__________________________________________________________|
|  6.Normall Hash identification without J.T.R info.       |
|__________________________________________________________|
|  7.Normall Hash identification without Hashcat info.     |
|__________________________________________________________|
|  0.Exit                                                  |
|----------------------------------------------------------|
""")
	ver3 = int(input("\033[32m\nSelect a option: " + "\033[0m"))
	if ver3 == 1:
		os.system("python3 Hashcrypt -t '" + ver1 + "'")
		input("\nPress Enter to continue") 
		os.system("clear")
		os.system("python3 crypto.py")
	elif ver3 == 2:
		os.system("python3 Hashcrypt -t '" + ver1 + "' -g")
		input("\nPress Enter to continue")
		os.system("clear")
		os.system("python3 crypto.py")
	elif ver3 == 3:
		os.system("python3 Hashcrypt -t '" + ver1 + "' -b64")
		input("\nPress Enter to continue")
		os.system("clear")
		os.system("python3 crypto.py")
	elif ver3 == 4:
		os.system("python3 Hashcrypt -t '" + ver1 + "' -a")
		input("\nPress Enter to continue")
		os.system("clear")
		os.system("python3 crypto.py")
	elif ver3 == 5:
		os.system("python3 Hashcrypt -t '" + ver1 + "' -e")
		input("\nPress Enter to continue")
		os.system("clear")
		os.system("python3 crypto.py")
	elif ver3 == 6:
		os.system("python3 Hashcrypt -t '" + ver1 + "' --no-john --no-banner")
		input("\nPress Enter to continue")
		os.system("clear")
		os.system("python3 crypto.py")
	elif ver3 == 7:
		os.system("python3 Hashcrypt -t '" + ver1 + "' --no-hashcat --no-banner")
		input("\nPress Enter to continue")
		os.system("clear")
		os.system("python3 crypto.py")
	elif ver3 == 0:
		print("\033[31m\nThank You, exiting")
		os.system("exit")
	else:
		print("\033[31mInvalid Input")

else:
	print("\033[31m\nInvalid Input")
	input("\033[0m\nPress Enter to continue")
	os.system("clear")
	os.system("python3 crypto.py")












