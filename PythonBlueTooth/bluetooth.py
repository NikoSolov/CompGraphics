import bluetooth

target_name = "HC-05"
target_address = None

nearby_devices = bluetooth.discover_devices()
for bdaddr in nearby_devices:
    a=bluetooth.lookup_name( bdaddr )
    print(bdaddr,a)
    if target_name == a:
        addr = bdaddr
        break
#addr="00:13:12:12:26:70"
port=1
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((addr, port))
print("connected")
s.send("i\na")

while True:
    data_received=""
    a=s.recv(1).decode("utf-8")
    while a!="\n":
        data_received += a
        a=s.recv(1).decode("utf-8")
    b=data_received.split()
    try:
        b.remove(":")
    except:
        pass
    print(b)
    b[0]=int(b[0][1:])
    for i in range(1,len(b)):
        b[i]=int("0x"+b[i][1:], 0)
    print(b, b[2])
    if b[2]<250: s.send("w")
    print("----------\n")
    s.send("a")