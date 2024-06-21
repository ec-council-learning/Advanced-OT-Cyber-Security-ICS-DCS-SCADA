https://python-snap7.readthedocs.io/en/1.3/API/client.html
https://python-snap7.readthedocs.io/en/1.3/API/server.html
---

import snap7
client = snap7.client.Client()
client.connect("127.0.0.1", 0, 0, 102)
client.get_connected()
True
data = client.db_read(1, 0, 4)
data
bytearray(b"\x00\x00\x00\x00")
data[3] = 0b00000001
data
bytearray(b'\x00\x00\x00\x01')
client.db_write(1, 0, data)
client.destroy()


---

import snap7
client = snap7.client.Client()
client.connect("127.0.0.1", 0, 0, 102)
buffer = client.db_get(1)  # reads the db number 1.
buffer
bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00...<truncated>\x00\x00")

---

block_info = client.get_block_info("DB", 1)
print(block_info)


-----

cpu_info = client.get_cpu_info()
print(cpu_info)

----

client.get_cpu_state()

--

client.get_pdu_length()
---
client.get_plc_datetime()

----

block_list = client.list_blocks()
print(block_list)