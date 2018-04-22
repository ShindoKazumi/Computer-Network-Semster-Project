import socket                         # Import socket module

s = socket.socket()                   # Create a socket object
host = socket.gethostname()           # Get local machine name
port = 9999                           # Reserve a port for your service.
s.bind((host, port))                  # Bind to the port
s.listen(5)                           # Now wait for client connection.
while True:
  c, addr = s.accept()                # Establish connection with client.
  print 'Got connection from', addr
  print "Getting file name..."
  name = c.recv(1024)
  f = open(name,'rb')                 # Open file requested by client
  l = f.read(1024)
  while (l):
    c.send(l)
    l = f.read(1024)
  f.close()
  print "Done Sending"
  c.shutdown(socket.SHUT_WR)
  c.close()
