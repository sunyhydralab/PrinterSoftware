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

    print(available_printers)
    # Selecting the first available printer for demonstration
    

    # Create a Job - assuming you have a Job class
    test_job = Job("20mm_calibration.gcode", "test", 1, 1, 1)
    # This just selects the first printer in the list.  Replace this with the queue.

    selected_printer = available_printers[0]
    print("Selected Port: ", selected_printer)
    selected_printer.connect()  # Connect to the printer
    # selected_printer.reset()    # Reset the printer
    selected_printer.printJob(test_job)  # Send the job to the printer
    selected_printer.disconnect()        # Disconnect from the printer



# def printer_job_handler(printer):
#     while True:
#         try:
#             # Get the next job (block until a job is available)
#             job = printer.queue.get(block=True)
#             # If job returns a new job run the print. 
#             printer.connect()
#             printer.reset()
#             printer.printJob(job)
#             printer.disconnect()
#             printer.queue.task_done()
#         except Exception as e:
#             print(f"Error with printer {printer.serial_port}: {e}")

# if __name__ == '__main__':

#     # Remove and set to passed variable from front end. 
#     serial_printers = int(input("Enter 0 for real printers or 1 for virtual printers: "))

#     if serial_printers == 0:
#         available_printers = Printer.getSupportedPrinters(virtual=False)
#     elif serial_printers == 1:
#         available_printers = Printer.getSupportedPrinters(virtual=True)
#     else:
#         print("Invalid input. Please enter 0 for real printers or 1 for virtual printers.")
#         exit()

#     if not available_printers:
#         print("No supported printers found.")
#         exit()

#     # Adding a queue to each printer and starting a handler thread
#     for printer in available_printers:
#         printer.queue = queue.Queue()
#         threading.Thread(target=printer_job_handler, args=(printer,), daemon=True).start()

#     # Main loop to accept new jobs
#     while True:
#         # Receive or generate new jobs. Placeholder.
#         new_job = Job("20mm_calibration.gcode", "test", 1, 1, 1)  # Implement this function new job. 

#         if new_job:
#             # Assign the job to a printer.  Add check to find which printer to select. Right just takes the first, this is a Placeholder.
#             selected_printer = available_printers[0]
#             selected_printer.queue.put(new_job)

       

