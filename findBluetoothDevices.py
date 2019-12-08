import bluetooth, subprocess, traceback
from tkinter import *

device_addr = ""
device_name = ""


def list_devices():
    device_list = []
    print("Performing inquiry...")

    nearby_devices = bluetooth.discover_devices(duration=4, lookup_names=True,
                                                flush_cache=True, lookup_class=False)

    print("Found {} devices".format(len(nearby_devices)))

    for addr, name in nearby_devices:
        try:
            if name == "HC-06":
                device_list.append("   {} - {}".format(addr, name))
        except UnicodeEncodeError:
            print("   {} - {}".format(addr, name.encode("utf-8", "replace")))
    return device_list


def connect_to_imu():
    name = device_name  # Device name
    addr = device_addr  # Device Address
    port = 1  # RFCOMM port
    passkey = "1234"  # passkey of the device you want to connect

    # kill any "bluetooth-agent" process that is already running
    subprocess.call("kill -9 `pidof bluetooth-agent`", shell=True)

    # Start a new "bluetooth-agent" process where XXXX is the passkey
    status = subprocess.call("bluetooth-agent " + passkey + " &", shell=True)

    # Now, connect in the same way as always with PyBlueZ
    try:
        s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        s.connect((addr, port))
        print("Connected")
    except bluetooth.btcommon.BluetoothError as err:
        # Error handler
        traceback.print_exc()


def main():
    list_devices()


if __name__ == "__main__":
    main()
