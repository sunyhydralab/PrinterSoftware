import serial
import serial.tools.list_ports
import time

# Class for each printer job.
class Job:
    # Constructor for the Job class
    def __init__(self, file, name, quantity, priority, status):
        self.file = file  # The G-code file
        self.name = name    # Name of the job
        self.gcode_lines = self.load_gcode(file)  # List containing the G-code lines
        self.quantity = quantity  # Quantity of the job
        self.priority = priority  # Priority of the job
        self.status = status # Status of the job
        
    # Method to load G-code from a given file path
    def loadGcode(self, path):
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

    # Method to find file type.
    def fileType(self):
        name, ext = os.path.splitext(file)
        self.extension = ext
        
    # Method for X3G/GCODE conversion.    
    def printFile(self):
        if(self.extension == ".gcode"):
            # send to compatible printer 
        elif(self.extension == ".x3g"): 
            # send to compatible printer 
