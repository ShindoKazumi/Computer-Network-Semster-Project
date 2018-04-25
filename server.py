import socket
from subprocess32 import Popen, PIPE

s = socket.socket()        
host = socket.gethostname()
port = 9999
#port = raw_input('Enter port number: ')
#port = int(port)
s.bind((host, port))

s.listen(1)

while True:
	# Establish connection with controller
	contConn, addr = s.accept()
	
	# Code to return list to controller
	cmd = contConn.recv(1024)
	cmd = cmd.split() 
	p = Popen(cmd, stdout=PIPE)
	result = p.communicate()
	contConn.send(result[0])
	contConn.close()

	while True:
		# Establish connection with displayer
		conn, addr = s.accept()     
		print 'Got connection from', addr
		print "Waiting for file name..."	
			
		while True:	
			try:
				name = conn.recv(1024)
				if name == 'exit':
					conn.close()
					break
				path = 'files/' + name	
				f = open(path,'rb')
				l = f.read(1024)
				while (l):
					conn.send(l)
					l = f.read(1024)
				f.close()
				print "Done Sending"
				conn.shutdown(socket.SHUT_WR)
				conn.close()
				break
			except IOError:
				print('File failed to open')
				conn.send('error')
			else:
				break
		break
