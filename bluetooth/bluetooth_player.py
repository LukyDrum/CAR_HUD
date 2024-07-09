import subprocess

from bluetooth.song_info import SongInfo
from bluetooth.device import BluetoothDevice, get_devices

class BluetoothPlayer:
    def __init__(self):
        self.dbus_object = "org.bluez.MediaControl1"
        self.device = self._get_active_device()

    def play(self) -> None:
        base = self._get_base_command()
        cmd = base + " " + f"{self.dbus_object}.Play"

    def pause(self) -> None:
        base = self._get_base_command()
        cmd = base + " " + f"{self.dbus_object}.Pause"

    def play_pause(self) -> None:
        pass

    def next(self) -> None:
        pass

    def previous(self) -> None:
        pass

    def song_info(self) -> SongInfo:
        pass

    def _get_active_device(self) -> BluetoothDevice:
        devices = get_devices()
        for dev in devices:
            if dev.connected:
                return dev
    
    def _get_base_command(self) -> str:
        device = self._get_active_device()
        return f"dbus-send --system --print-reply --dest=org.bluez /org/bluez/hci0/dev_{device.address.replace(':','_')}/player0"
    
    def update_device(self) -> None:
        self.device = self._get_active_device()


def run_with_timeout(command: str, timeout: float):
    subprocess.run(command.split(" "), timeout=timeout)