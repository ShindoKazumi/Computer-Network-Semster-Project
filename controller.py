import socket

host = socket.gethostname()

# connect controller to server
s = socket.socket()
sPort = raw_input('Enter server port number: ')
sPort = int(sPort)
s.connect((host, sPort))

# set up displayer connection
c = socket.socket()
cPort = raw_input('Enter controller port number: ')
cPort = int(cPort)
c.bind((host, cPort)) 
c.listen(1)

while True:
	# Establish connection with displayer
	conn, addr = c.accept()
	while True:
		# code to request list from server and then send to displayer
		cmd = raw_input("user > ")
		s.send(cmd)
		print 'Connection address:', addr
		break
	# close connection with displayer
	conn.close()
