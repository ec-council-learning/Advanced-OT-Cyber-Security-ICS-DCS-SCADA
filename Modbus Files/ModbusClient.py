from pyModbusTCP.client import ModbusClient

# Create a Modbus client instance
c = ModbusClient()

# Set the Modbus server IP address and port
c.host('127.0.0.1')  # Replace with your Modbus server IP address
c.port(502)  # Replace with your Modbus server port (default is 1700)

# Connect to the Modbus server
c.open()

# Check if the connection is open
if c.is_open():
    print("Connected to Modbus server!")

    # Now you can use Modbus functions to read/write data
    # For example, read 10 holding registers starting from address 0
    regs = c.read_holding_registers(0, 10)
    print(regs)

    # Close the connection when done
    c.close()
else:
    print("Failed to connect to Modbus server!")
