import socket                                 # Import socket module
import PyPDF2                                 # import PyPDF2         need to install into syatem using 'pip install PyPDF2'
from getch import getch, pause                # import getch          need to install into system using 'pip install py-getch'

s = socket.socket()
host = socket.gethostname()                   
port = 9999                                   

s.connect((host, port))

# Get name of file to display
name = raw_input('Enter name of file to display: ')

# Create tempfile to read into display
f = open('tempFile','wb')                     
s.send(name)
l = s.recv(1024)
# Read contents of serverfile into tempfile
while (l):                                    
  f.write(l)
  l = s.recv(1024)
f.close()
print "Done Receiving"

# creating a pdf file object
pdfFileObj = open('tempFile', 'rb')
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
 
pagenum = pdfReader.numPages
page = 0
pagenum = int(pagenum)
page = int(page)

print 'Press the A and D keys to move through the file'
print 'Or press Q to quit'

# creating a pdf file object
while 1:
  input = getch()
  if (input == 'A') or (input == 'a'):
    if 0 < page:  
      page = page - 1
  elif (input == 'D') or (input == 'd'):
    if page < pagenum:
      page = page + 1
  elif (input == 'Q') or (input == 'q'):
      break
  pageObj = pdfReader.getPage(page)
  print(pageObj.extractText())
 
# closing the pdf file object
pdfFileObj.close()
# closing the socket
s.close()
