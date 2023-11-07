import serial
import threading

class VirtualPrinter:

    # Constructor
    def __init__(self, name):
        self.name = name
        # Create a serial port of the virtual printer
        self.ser = serial.serial_for_url('loop://', timeout=1)

    def run(self):
        print(self.name, " is running")
        # loop to process commands
        while True:
            # Read in the data from the port
            incoming = self.ser.read(self.ser.in_waiting or 1)
            if incoming:
                # This is where we should put the check for correct Gcode commands
                response = self.checkGcode(incoming)
                # Write the response
                self.ser.write(response)

    def checkGcode(self, data):
        # Simulate the data return of the printer (print the message)
        print("Command: ",data," Received: ok")
        # check the Gcode against allowed commands
        # Print "OK" if it is a valid command.  Implement once we have a list of correct Gcode commands
        return data
    
    def start(self):
        # Multiple threads for each printer
        thread = threading.Thread(target=self.run)
        # Close the thread when the program exits
        thread.daemon = True
        # Start the thread
        thread.start()
        return thread

