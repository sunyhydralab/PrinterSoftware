import serial
from serial.tools import list_ports
import time
from collections import deque
# from Classes.Queue import Queue
import threading

# Class for each printer.
class Printer:
    # Constructor for the Printer class
    def __init__(self, serial_port, filament=None, virtual=False):
        self.serial_port = serial_port
        self.ser = None
        self.filament = filament
        self.virtual = virtual
        self.queue = deque()
        self.thread = threading.Thread(target=self.printQueue).start()

    # Method to connect to the printer via serial port.
    def connect(self):
        if not self.virtual:
            print("In connect")
            self.ser = serial.Serial(self.serial_port, 115200, timeout=1)
        else:
            print("Connected to virtual printer.")

    # Method to disconnect from the printer via serial port.
    def disconnect(self):
        if self.ser:
            self.ser.close()

    # Method to reset the printer. Sends the printer to home and resets the extruder.
    def reset(self):
        print("In Reset")
        self.sendGcode("G28")
        print("Return Home")
        self.sendGcode("G92 E0")

    # Method to send gcode commands to the printer.
    def sendGcode(self, message):
        if self.virtual:
            print(f"Virtual Printer - Command: {message}, Received: ok")
            return
        self.ser.write(f"{message}\n".encode("utf-8"))
        time.sleep(0.1)
        while True:
            response = self.ser.readline().decode("utf-8").strip()
            if "ok" in response:
                break
        print(f"Command: {message}, Received: {response}")

    # Method to print a job.
    def printJob(self, job):
        print("In Print Job")
        for line in job.gcode_lines:
            self.sendGcode(line)
    
    #Method to add a job to the queue.
    def addJob(self, job):
        self.queue.append(job)
        print("Job added to queue")
        
    # Method to print the queue.
    # We should add a way to delay the next print job until 
    # the print has been cleared from the printer.
    def printQueue(self):
        print("In Print Queue")
        while True:
            try:
                # Check if the queue is empty
                if not self.queue:
                    # Wait for a second to check again.
                    time.sleep(1)
                    continue
                # Get the next job from the left of the queue
                job = self.queue.popleft()
                # If job returns a new job, run the print
                if job:
                    print("Printing Job")
                    self.connect()
                    self.reset()
                    self.printJob(job)
                    self.disconnect()
            except Exception as e:
                print(f"Error with printer {self.serial_port}: {e}")

    # Method to get a list of all the connected serial ports. 
    # Static Method that can be called without an instance.
    @staticmethod
    def getSupportedPrinters(virtual=False):

        # Make a list of the supported printers.
        # Save the port and description to list. 
        # With key value pairs of port and description.
        printerList = []

        if virtual:
            # Assuming you want to create a predefined number of virtual printers
            num_virtual_printers = 3  # You can change this number as needed
            for i in range(num_virtual_printers):
                # Creating virtual Printer objects
                printerList.append(Printer("Virtual Port " + str(i), virtual=True))
            return printerList

        # Get a list of all the connected serial ports.
        ports = serial.tools.list_ports.comports()

        # Keep a list of supported printers.
        supportedPrinters = ["Original Prusa i3 MK3", "Makerbot"]
        for port in ports:
            
            # Check if the printer is supported and if true add it to the list.
            if port.description in supportedPrinters:
                printerList.append(Printer(port.device))
            # Print out the list of supported printers.
            print(f"Port: {port.device}, Descp: {port.description}")
        # Return the list of supported printers.
        return printerList
        
    
    
        
            

