from scapy.all import *

# Create an Ethernet frame
eth = Ether(dst="01:0e:cf:00:00:00", src="fe80::9ed0:d208:996c:d66b", type=0x8892)

# Create a PROFINET DCP Identify Request
profinet_dcp = (
    b'\xfe\xfd\x00\x01'  # Service Identifier
    b'\x00\x01\x01'      # Request ID
    b'\x00\x00'          # Service Type and Service ID
    b'\x05\x01'          # XID and Response Delay
    b'\x00\x00\x00\x00'  # DCP Option and Suboption
)

# Combine Ethernet frame with PROFINET DCP payload
packet = eth / Raw(load=profinet_dcp)

# Send the crafted packet
sendp(packet, iface="eth0", count=1)
