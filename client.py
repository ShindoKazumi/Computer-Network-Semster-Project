import socket					# Import socket module
import pdftotext				# import pdftotext		need to install into system using 'pip install pdftotext'
from getch import getch, pause			# import getch			need to install into system using 'pip install py-getch'

run = True

# Get server and controller port from user input. This is for test runs
# This has to be changed to static port numbers
sPort = raw_input('Enter server port number: ')
sPort = int(sPort)

cPort = raw_input('Enter controller port number: ')
cPport = int(cPort)

while run:
	host = socket.gethostname()

	s = socket.socket()
	s.connect((host, sPort))

	c = socket.socket()
	c.connect((host, cPort))


	while True:
		name = raw_input('Enter name of file to display (enter exit to close): ')
		if name == 'exit':
			s.send('exit')
			run = False
			break
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

		while True:
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
		break
	# Close the socket when done
	s.close()                                   
