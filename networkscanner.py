# Network Scanner for Python.

# The goal Scan ports, tagets hosts and looks super cool.
 
#!/usr/bin/env python3

from tkinter import *
from socket import *
import time
# So, the object here had to be moved around some
def scan_ports():
    target = entry.get() # retrieves the hostname
    t_IP = gethostbyname(target) # resoolves host name to target ip
    result_text.delete(1.0, END) # clears the widget of anything prior
    result_text.insert(END, f'Starting scan on host: {t_IP}\n') # should display a messag to show start of the scan

    for i in range(1, 1000): # the for i is to ensure scan exists for scanned ports 1-1000
        s = socket(AF_INET, SOCK_STREAM) # creates TCP socket and address socket type
        conn = s.connect_ex((t_IP, i))
        if conn == 0: # if connection is succesful the conn == line will execute the scan, we could change the number if you want
            result_text.insert(END, f'Port {i}: OPEN\n') # this is the line that shows the output of th scna in the widget
        s.close()

    result_text.insert(END, f'Time taken: {time.time() - startTime:.2f} seconds') # this just prints out the time result for the scan.

# Created main loop window for desktop
root = Tk()
root.title('Network Scanner')

# good ol widgets
label = Label(root, text='Enter the host to be scanned:')
label.pack(pady=10)

entry = Entry(root)
entry.pack(pady=10)
# the actual scan button
scan_button = Button(root, text='Scan Ports', command=scan_ports)
scan_button.pack(pady=10)

# loops with lines 12-22 for results in gui
result_text = Text(root, height=10, width=50)
result_text.pack(pady=10)

# Start GUI event loop
startTime = time.time()
root.mainloop()
