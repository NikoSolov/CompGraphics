import serial
import serial.tools.list_ports
import time

ports = serial.tools.list_ports.comports()
portname="COM14"

print("List of ports:")
for port, desc, hwid in sorted(ports):
 print(port, desc)
 if "USB-SERIAL CH340" in desc:
  print("port founded")
  portname = port

time_code=serial.Serial(port=portname, baudrate=9600,  timeout=.1)
time.sleep(2)
print("Look at the PuTTY")

while True:
 for i in range(256):
  time_code.write(bytearray([i]))
  time.sleep(0.05)
