import socket					# Import socket module
import pdftotext				# import pdftotext		need to install into system using 'pip install pdftotext'
from getch import getch, pause			# import getch			need to install into system using 'pip install py-getch'

host = socket.gethostname()

s = socket.socket()
sPort = raw_input('Enter server port number: ')
sPort = int(sPort)
s.connect((host, sPort))

c = socket.socket()
cPort = raw_input('Enter controller port number: ')
cPport = int(cPort)
c.connect((host, cPort))


while 1:
	name = raw_input('Enter name of file to display: ')
	f = open('tempFile','wb')
	s.send(name)
	l = s.recv(1024)
	while (l):
		f.write(l)
		l = s.recv(1024)
	f.close()
	print "Done Receiving"

	# creating a pdf file object
	pdfile = open('tempFile', 'rb')
	pdf = pdftotext.PDF(pdfile)

	pagenum = len(pdf)	
	page = 0
	pagenum = int(pagenum)
	page = int(page)

	print 'Press the A and D keys to move through the file'
	print 'Or press Q to quit'

	while 1:
		input = getch()
		if (input == 'A') or (input == 'a'):
			if 0 < page:  
				page = page - 1
		elif (input == 'D') or (input == 'd'):
			if page < pagenum-1:
				page = page + 1
			else:
				break
		elif (input == 'Q') or (input == 'q'):
			break
		print(pdf[page])
# Close the socket when done
s.close()                                   
