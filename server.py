import socket
from subprocess32 import Popen, PIPE


c = socket.socket()
s = socket.socket()        
host = socket.gethostname() 
port = raw_input('Enter port number:')
port = int(port)
s.bind((host, port))

s.listen(1)
# Establish connection with controller
contConn, addr = s.accept()
# code to return list to controller
cmd = c.recv(1024)

cmd = cmd.split() #to get 'ls', '-la'

p = Popen(cmd, stdout=PIPE)
result = p.communicate()

c.send(result[0])

contConn.close()
while True:
	while True:
		# Establish connection with displayer
		conn, addr = s.accept()     
		print 'Got connection from', addr
		print "Getting file name..."
		name = conn.recv(1024)
		if name == 'exit':
			conn.close()
			break
		f = open(name,'rb')
		l = f.read(1024)
		while (l):
			conn.send(l)
			l = f.read(1024)
		f.close()
		print "Done Sending"
		conn.shutdown(socket.SHUT_WR)
		conn.close()
