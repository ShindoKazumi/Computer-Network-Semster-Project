import socket

host = socket.gethostname()

# connect controller to server
#sPort = raw_input('Enter server port number: ')
#sPort = int(sPort)
sPort = 9999
cPort = 9998
# set up displayer connection
c = socket.socket()
#cPort = raw_input('Enter controller port number: ')
#cPort = int(cPort)
c.bind((host, cPort)) 
c.listen(1)

while True:
	# Establish connection with displayer
	s = socket.socket()
	s.connect((host, sPort))	
	conn, addr = c.accept()
	while True:
		# code to request list from server and then send to displayer
		print 'Connection address:', addr		
		cmd = 'ls files'
		s.send(cmd)
		output = s.recv(1024)
		conn.send(output)		
		break
	# close connection with displayer
	conn.close()
