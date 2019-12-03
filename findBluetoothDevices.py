import bluetooth
from tkinter import *

device_addr = ""


def list_devices():
    device_list = []
    print("Performing inquiry...")

    nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True,
                                                flush_cache=True, lookup_class=False)

    print("Found {} devices".format(len(nearby_devices)))

    for addr, name in nearby_devices:
        try:
            device_list.append("   {} - {}".format(addr, name))
        except UnicodeEncodeError:
            print("   {} - {}".format(addr, name.encode("utf-8", "replace")))
    return device_list


def init_gui():
    root = Tk()
    dev_list = list_devices()

    lb = Listbox(root, width=250)
    i = 0
    for dev in dev_list:
        lb.insert(i, dev)
        i = i + 1
    select_button = Button(root, text="Select Device", command=select)
    lb.pack()
    select_button.pack()
    root.mainloop()


def select():
    print("Test")


def main():
    init_gui()


if __name__ == "__main__":
    main()
