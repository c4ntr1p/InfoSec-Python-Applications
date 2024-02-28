# Network Scanner for Python. I'd like to work on a GUI icon and display box so result happens outside of command line.
# dont forget! sudo chmod +X networkscanner (in linux) 

#!/usr/bin/env python3
from tkinter import *
from socket import *
import time

#def scan_ports():
<FUNCTION>

startTime = time.time()

if __name__ == '__main__':
   target = input('Enter the host to be scanned: ')
   t_IP = gethostbyname(target)
   print ('Starting scan on host: ', t_IP)
   
   for i in range(50, 500):
      s = socket(AF_INET, SOCK_STREAM)
      
      conn = s.connect_ex((t_IP, i))
      if(conn == 0) :
         print ('Port %d: OPEN' % (i,))
      s.close()
print('Time taken:', time.time() - startTime)

# Below is all I could find tonight on the tail. Header still needs some work. But man this file is amazing.... 
# Create the main Window
root =TK ()
root.title('Network Scanner')

# Create widgets and buttons
<FUNCTION>

# Start GUI Loop
startTime = time.time()
root.mainloop()
