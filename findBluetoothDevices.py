import bluetooth
from tkinter import *


def list_devices():
    devices = bluetooth.discover_devices()
    out = ""
    if devices:
        for bdaddr in devices:
            device_name = bluetooth.lookup_name(bdaddr)
            device_addr = bdaddr
            out = "Device Name: " + device_name + " Device Address: " + device_addr
    else:
        out = "No devices found"
    return out


def init_gui():
    root = Tk()
    out = list_devices()
    title_label = Label(root, text=out)
    title_label.pack()
    root.mainloop()


def main():
    init_gui()


if __name__ == "__main__":
    main()
