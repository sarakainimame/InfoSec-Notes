### Port Scanner ### 

import socket

def scan (target, ports):
	print('\n' + ' Scanning for: ' + str(target))
	for port in range (1, ports):
		scan_port (target, port)

def scan_port(ip_address, port):
	try:
		my_socket = socket.socket()
		my_socket.connect((ip_address, port))
		print ('[+] Port ' + str(port) + ' is Open')
	except:
		pass

targets = input('[*] Enter the target you want to scan: ')
ports = int(input('[*] Enter how many ports you want to scan: '))
if ',' in targets:
	print('[*] Scanning multiple targets')
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)

else:
	scan(targets, ports)