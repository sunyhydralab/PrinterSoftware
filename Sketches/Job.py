import serial
import serial.tools.list_ports
import time

class Job:
    # Constructor for the Job class
    def __init__(self, file, name, quantity, priority):
        self.file = file  # The G-code file
        self.name = name    # Name of the job
        self.gcode_lines = self.load_gcode(file_path)  # List containing the G-code lines
        self.quantity = quantity  # Quantity of the job
        self.priority = priority  # Priority of the job
        
    # Method to load G-code from a given file path
    def load_gcode(self, path):
        lines = []
        with open(path, "r") as g:
            for line in g:
                line = line.strip()  # Remove whitespace
                if len(line) == 0:  # Do not send blank lines
                    continue
                if ";" in line: # Remove inline comments
                    line = line.split(";")[0].strip()  # Remove comments starting with ";"
                if len(line) == 0 or line.startswith(";"):  # Don't send empty lines and comments
                    continue
                lines.append(line)  # Add the G-code line to the list
        return lines  # Return the list of G-code lines



class Printer:
    # Constructor for the Printer class
    def __init__(self, serial_port):
        self.serial_port = serial_port
        self.ser = None

    def connect(self):
        self.ser = serial.Serial(self.serial_port, 115200, timeout=1)

    def disconnect(self):
        if self.ser:
            self.ser.close()

    def reset(self):
        self.send_gcode("G28")
        self.send_gcode("G92 E0")

    def send_gcode(self, message):
        self.ser.write(f"{message}\n".encode('utf-8'))
        time.sleep(0.1)
        while True:
            response = self.ser.readline().decode("utf-8").strip()
            if "ok" in response:
                break
        print(f"Command: {message}, Received: {response}")

    def print_job(self, job):
        for line in job.gcode_lines:
            self.send_gcode(line)

    
    def get_supported_printers():
        # Get a list of all the connected serial ports.
        ports = serial.tools.list_ports.comports()
        # Make a list of the supported printers.
        for port in ports:
            # Save the port and description to list. With key value pairs of port and description.
            printerList = []
            # Keep a list of supported printers.
            supportedPrinters = ["Original Prusa i3 MK3", "Makerbot"]
            # Check if the printer is supported and if true add it to the list.
            if port.description in supportedPrinters:
                printerList.append(port)   
            # Print out the list of supported printers.
            print(f"Port: {port.device}, Descp: {port.description}")
        # Return the list of supported printers.
        return printerList


# Usage
if __name__ == '__main__':
    available_printers = Printer.get_supported_printers()
    # Assuming the first available printer is selected for demo purposes.  
    # This is where the queue would come in.
    
    # This just selects the first printer in the list.  Replace this with the queue.
    selected_port = available_printers[0].device if available_printers else None

    if selected_port:
        prusa_printer = Printer(selected_port)
        prusa_printer.connect()
        prusa_printer.reset()

        test_job = Job(file, name, quantity, priority)
        prusa_printer.print_job(test_job)

        prusa_printer.reset()
        prusa_printer.disconnect()
    else:
        print("No supported printers found.")
