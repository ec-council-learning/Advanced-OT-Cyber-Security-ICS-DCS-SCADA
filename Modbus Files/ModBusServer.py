from pymodbus.server.async_modbus_tcp_server import AsyncModbusServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

# Create a sequential data block for holding registers
store = ModbusSlaveContext(di=ModbusSequentialDataBlock(0, [0]*100),
                           hr=ModbusSequentialDataBlock(0, [0]*100),
                           ir=ModbusSequentialDataBlock(0, [0]*100),
                           co=ModbusSequentialDataBlock(0, [0]*100))

# Create a Modbus server context
context = ModbusServerContext(slaves=store, single=True)

# Create a Modbus device identification
identity = ModbusDeviceIdentification()
identity.VendorName = 'pymodbus'
identity.ProductCode = 'PM'
identity.VendorUrl = 'http://github.com/riptideio/pymodbus'
identity.ProductName = 'pymodbus Server'
identity.ModelName = 'pymodbus Server'
identity.MajorMinorRevision = '1.0'

# Create a Modbus TCP server
server = AsyncModbusServer(context, identity=identity)

# Set the server IP address and port
server.server_address = ('127.0.0.1', 502)

# Start the server
server.start()

# Wait for the server to stop
server.serve_forever()

# Close the server
server.close()
