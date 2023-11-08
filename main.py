import sys
import os
import time

# Import the classes 
import serial.tools.list_ports
from Classes.Job import Job
from Classes.Printer import Printer

# On Linux/OSX. Run this command in the terminal to create 5 virtual serial printers.
"""
for i in {1..5}; do
    socat -d -d pty,raw,echo=0 pty,raw,echo=0 &
done
"""
# When you are done testing, run this command in the terminal to remove the virtual serial printers.
"""
for i in {1..5}; do
    killall socat
done
"""
# Replace the port names with the virtual serial ports created by the above command.
master_ports = ['/dev/pts/2', '/dev/pts/4', '/dev/pts/6', '/dev/pts/8', '/dev/pts/10']
slave_ports = ['/dev/pts/3', '/dev/pts/5', '/dev/pts/7', '/dev/pts/9', '/dev/pts/11']

# Get the list of available printers. Pass 0 for a list of real connected printers.  Pass 1 for a list of 5 virtual printers.
serial_printers = 1


if __name__ == '__main__':

    # Real printers
    if serial_printers == 0:
        available_printers = Printer.getSupportedPrinters()
    # Virtual printers
    elif serial_printers == 1:
         # Setup the available printers to the virtual printers.
         available_printers = [Printer(port) for port in slave_ports]
    else:
        print("Invalid input.  Please enter 0 for real printers or 1 for virtual printers.")

    # Assuming the first available printer is selected for demo purposes.  
    # This is where the queue would come in.
    ports = serial.tools.list_ports.comports()
    available_ports = [port.device for port in ports]
    print("Available ports: ", available_ports)
     # Create the Job. All this information will come from the front end database.
    test_job = Job("20mm_calibration.gcode", "test", 1, 1, 1)

    # This just selects the first printer in the list.  Replace this with the queue.

    selected_port = available_printers[0].device if available_printers else None
    print("Selected Port: ", selected_port)
    if selected_port:
        # Basic structure of sending a job to the printer.
        prusa_printer = Printer(selected_port)  # Create a Printer object.
        prusa_printer.connect()  # Connect to the printer.
        prusa_printer.reset()  # Reset the printer.
        prusa_printer.printJob(test_job)  # Send the job to the printer.
        prusa_printer.disconnect()  # Disconnect from the printer.
    else:
        print("No supported printers found.")

