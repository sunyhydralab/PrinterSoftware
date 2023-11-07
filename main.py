import sys
import os

# Import the classes 
import serial.tools.list_ports
from Classes.Job import Job
from Classes.Printer import Printer

# Current virtual printer implementation does not work.  Rewrite with socat.

if __name__ == '__main__':

    # Get the list of available printers. Pass 0 for a list of real connected printers.  Pass 1 for a list of 5 virtual printers.
    available_printers = Printer.getSupportedPrinters(0)
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
