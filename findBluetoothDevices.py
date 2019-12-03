import bluetooth


def list_devices():
    devices = bluetooth.discover_devices()

    if devices:
        print("Nearby devices: ")
        for bdaddr in devices:
            device_name = bluetooth.lookup_name(bdaddr)
            device_addr = bdaddr
            print("Device Name: " + device_name + " Device Address: " + device_addr)
    else:
        print("No devices found")


def main():
    list_devices()

# print("Attempting to establish a connection to " + device_name)
# try:
#     sock = bluetooth.BluetoothSocket()
# except bluetooth.BluetoothError:
#     print("An error has occured!")


if __name__ == "__main__":
    main()
