import sys
import os
import threading
import queue

# Import the classes 
from Classes.Job import Job
from Classes.Printer import Printer

if __name__ == '__main__':
    # Get the list of available printers. Pass 0 for a list of real connected printers.  Pass 1 for a list of 5 virtual printers.
    # serial_printers = int(input("Enter 0 for real printers or 1 for virtual printers: "))
    serial_printers = 1

    # Setup for real or virtual printers
    if serial_printers == 0:
        available_printers = Printer.getSupportedPrinters(virtual=False)
    elif serial_printers == 1:
        available_printers = Printer.getSupportedPrinters(virtual=True)
    else:
        print("Invalid input. Please enter 0 for real printers or 1 for virtual printers.")
        exit()

    # Check if any printers are available
    if not available_printers:
        print("No supported printers found.")
        exit()

    # print(available_printers)
    # Selecting the first available printer for demonstration
    

    # Create a Job - assuming you have a Job class
    test_job = Job("20mm_calibration.gcode", "test", 1, 1, 1)
    # This just selects the first printer in the list.  Replace this with the queue.

    selected_printer = available_printers[0]
    selected_printer.addJob(test_job)
   

    # Create a master printer queue api that will handle giving the jobs to the printers. 




