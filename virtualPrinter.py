import serial
import threading
from main import master_ports

class DescribedSerialPort:
    def __init__(self, port_name, description, baudrate=115200, timeout=1):
        self.port_name = port_name
        self.description = description
        self.serial = serial.Serial(port_name, baudrate=baudrate, timeout=timeout)
    
    def read_command(self):
        return self.serial.readline()
    
    def write_response(self, response):
        self.serial.write(response)

    def close(self):
        self.serial.close()

def handle_master_port(port):
    while True:
        # Read any incoming commands
        incoming = port.read_command()
        if incoming:
            command = incoming.decode().strip()
            print(f"{port.description}: Received command on {port.port_name}: {command}")
            # Simulate processing the command...
            # Send a response back
            port.write_response(b'ok\n')
        port.close()


master_threads = []
for port_name, description in master_ports:
    description = "Original Prusa i3 MK3"
    described_port = DescribedSerialPort(port_name, description)
    master_thread = threading.Thread(target=handle_master_port, args=(described_port,))
    master_thread.start()
    master_threads.append(master_thread)


# If you need to join the threads (and if they are expected to complete)
for master_thread in master_threads:
    master_thread.join()
