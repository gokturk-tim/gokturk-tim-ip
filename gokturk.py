import os
import time

os.system("apt install figlet")
os.system("clear")
os.system("figlet GOKTURK TIM")
print("""
Bu araçla otomatik olarak IP Adres değiştirebilirsiniz, değeri saniye olarak girin. GökTürk Tim gururla sunar...

~Darhan Bir Türk~ ~BayındırJapheth~
""")

sure = input("IP Değişim Süre(saniye) : ")

os.system("anonsurf start")
os.system("clear")
print("Yeni IP Adres :")
print("-----------------------------")
os.system("curl icanhazip.com")
print("-----------------------------")

while True:
	time.sleep(sure)
	os.system("anonsurf restart")
	os.system("clear")
	print("Yeni IP Adres :")
	print("-----------------------------")
	os.system("curl icanhazip.com")
	print("-----------------------------")
