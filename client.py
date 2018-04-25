import socket					# Import socket module
import pdftotext				# import pdftotext		need to install into system using 'pip install pdftotext'
from getch import getch, pause			# import getch			need to install into system using 'pip install py-getch'

run = True
# Gets server and controller port number for test runs
# This has to be changed to a static port number

#sPort = raw_input('Enter server port number: ')
#sPort = int(sPort)

#cPort = raw_input('Enter controller port number: ')
#cPort = int(cPort)

sPort = 9999
cPort = 9998
while run:
	host = socket.gethostname()

	s = socket.socket()
	s.connect((host, sPort))

	c = socket.socket()
	c.connect((host, cPort))


	while True:
		lst = c.recv(1024)
		print('\nList of Files: \n')
		print(lst)
		#c.send('list')
		f = open('tempFile','wb')
		fail = True
		while fail:
			name = raw_input('Enter name of file to display (enter exit to close): ')
			if name == 'exit':
				s.send('exit')
				run = False
				sys.exit(0)	
			
			s.send(name)
			l = s.recv(1024)
			if l != 'error':
				fail = False
				while (l):
					f.write(l)
					l = s.recv(1024)
			else:
				print('File does not exist')
		f.close()
		# creating a pdf file object
		pdfile = open('tempFile', 'rb')
		pdf = pdftotext.PDF(pdfile)

		pagenum = len(pdf)	
		page = -1
		pagenum = int(pagenum)
		page = int(page)

		print '\nFile Ready to Display'
		print 'Use A and D to move through the file'
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
					print('End of File')
					break
			elif (input == 'Q') or (input == 'q'):
				break
			print(pdf[page])
		break
# Close the socket when done
c.close()
s.close()
