#!/usr/bin/python3


# Setup file for the d4rk ghost framework tool

import os 
print("-" * 90)
print("Setup File for d4rk Ghost Framwork ")
print("-" * 90)


try:

	import colorama
	exit()
	
	

except:
	print("[-] colorama module not installed ! ")
	print("[+] Installing colorama module for you .. " )
	os.system("pip3 install colorama")
	print("[+] sucessfully Installed colorama module " )

try:
	import bane
	exit()

except:
	print(" [-] Bane module not installed installing for you")
	os.system("pip3 install bane")
	print("[+] sucessfully installed bane ")


print("[+] Completed . Requirement Already satisfied")	

	






