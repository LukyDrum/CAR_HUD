import subprocess
import os

class BluetoothDevice:
    def __init__(self, address: str, name: str, connected: bool) -> None:
        self.address = address
        self.name = name
        self.connected = connected


def get_devices() -> list[BluetoothDevice]:
    path = os.path.dirname(__file__) + "/list_bt_devices.sh"
    cmd = f"sh {path}"

    output = subprocess.check_output(cmd.split(" "))
    output_lines = output.decode("utf-8").split("\n")
    devices = []
    for i in range(len(output_lines), step=3):
        # Get device address
        line = output_lines[i].strip()
        address = line.split(" ")[1]
        # Get device name
        line = output_lines[i + 1].strip()
        name = line.split(" ", 1)[1]
        # Get device connected status
        line = output_lines[i + 2].strip()
        connected = True if "yes" in line else False

        devices.append(BluetoothDevice(address, name, connected))

    return devices


if __name__ == "__main__":
    devices = get_devices()

    for device in devices:
        print(f"{device.name} --- {device.address} --- {device.connected}")