import serial
from serial.tools import list_ports
import time
from Classes.Queue import Queue
from Classes.VirtualPrinter import VirtualPrinter


# Class for each printer.
class Printer:
    # Constructor for the Printer class
    def __init__(self, serial_port, filament=None):
        self.serial_port = serial_port
        self.ser = None
        self.filament = None
        self.queue = Queue()

    # Method to connect to the printer via serial port.
    def connect(self):
        self.ser = serial.Serial(self.serial_port, 115200, timeout=1)

    # Method to disconnect from the printer via serial port.
    def disconnect(self):
        if self.ser:
            self.ser.close()

    # Method to reset the printer. Sends the printer to home and resets the extruder.
    def reset(self):
        self.sendGcode("G28")
        self.sendGcode("G92 E0")

    # Method to send gcode commands to the printer.
    def sendGcode(self, message):
        self.ser.write(f"{message}\n".encode("utf-8"))
        time.sleep(0.1)
        while True:
            response = self.ser.readline().decode("utf-8").strip()
            if "ok" in response:
                break
        print(f"Command: {message}, Received: {response}")

    # Method to print a job.
    def printJob(self, job):
        for line in job.gcode_lines:
            self.sendGcode(line)

    @staticmethod
    def createVirtualPrinter():
        #List of printers
        printerList = []
        # Create 5 virtual printers
        for i in range(5):
            # Create a virutal printer
            printer = VirtualPrinter(f"Virtual{i}")
            # Add it to the list
            printerList.append(printer)
            # Start the printer thrad
            printer.start()
        # Return the list of virutal printers
        return printerList

    # Method to get a list of all the connected serial ports. Static Method that can be called without an instance.
    # Pass: 0 for real connected printers or 1 for virtual printers.
    @staticmethod
    def getSupportedPrinters(simulate):

        # Make a list of the supported printers.
        # Save the port and description to list. With key value pairs of port and description.
        printerList = []

        if(simulate == 0):
            # Get a list of all the connected serial ports.
            ports = serial.tools.list_ports.comports()
            for port in ports:
                # Keep a list of supported printers.
                supportedPrinters = ["Original Prusa i3 MK3", "Makerbot"]
                # Check if the printer is supported and if true add it to the list.
                if port.description in supportedPrinters:
                    printerList.append(port)
                # Print out the list of supported printers.
                print(f"Port: {port.device}, Descp: {port.description}")
            # Return the list of supported printers.
            return printerList
        elif(simulate == 1):
            # set printerList to the returned values from createVirutalPrinter
            printerList = Printer.createVirtualPrinter()
            return printerList
        else:
            print("Only pass 0 or 1. 0 for real printers. 1 for virutal printers")
    
    
        
            

