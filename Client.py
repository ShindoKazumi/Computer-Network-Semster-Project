import socket                                 # Import socket module

s = socket.socket()                           # Create a socket object
host = socket.gethostname()                   # Get local machine name
port = 9999                                   # Reserve a port for your service.

s.connect((host, port))
name = raw_input('Enter name of file to display: ')
f = open('tempFile','wb')                     # Create tempfile to read into display
s.send(name)
l = s.recv(1024)
while (l):                                    # Read contents of serverfile into tempfile
  f.write(l)
  l = s.recv(1024)
f.close()
print "Done Receiving"
s.close()                                     # Close the socket when done
