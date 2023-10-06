# System imports
import sys
import os

# Import the classes 
import Classes.Job as Job
import Classes.Printer as Printer


if __name__ == '__main__':

    # Get the list of available printers. 
    available_printers = Printer.get_supported_printers()
    # Assuming the first available printer is selected for demo purposes.  
    # This is where the queue would come in.
    
     # Create the Job. All this information will come from the front end database.
    test_job = Job(file, name, quantity, priority)

    # This just selects the first printer in the list.  Replace this with the queue.
    selected_port = available_printers[0].device if available_printers else None

    if selected_port:
        # Basic structure of sending a job to the printer.
        prusa_printer = Printer(selected_port)  # Create a Printer object.
        prusa_printer.connect()  # Connect to the printer.
        prusa_printer.reset()  # Reset the printer.
        prusa_printer.print_job(test_job)  # Send the job to the printer.
        prusa_printer.reset()  # Reset the printer.
        prusa_printer.disconnect()  # Disconnect from the printer.
    else:
        print("No supported printers found.")