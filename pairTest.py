import bluetooth

devices = bluetooth.discover_devices()
bt_addr = ""
for device in devices:
    print([_ for _ in bluetooth.find_service(address=device) if 'RFCOMM' in _['protocol']])
    bt_addr = device

# now manually select the desired device or hardcode its name/mac whatever in the script bt_addr = ...

port = [_ for _ in bluetooth.find_service(address=bt_addr) if 'RFCOMM' in _['protocol']][0]['port']

s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((bt_addr, port))