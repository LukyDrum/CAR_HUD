import subprocess

from bluetooth.song_info import SongInfo
from bluetooth.device import BluetoothDevice, get_devices

class BluetoothPlayer:
    def __init__(self):
        self.dbus_object = "org.bluez.MediaPlayer1"
        self.device = self._get_active_device()
        self.playing = False

    def play(self) -> None:
        self._run_dbus_command("Play")

    def pause(self) -> None:
        self._run_dbus_command("Pause")

    def play_pause(self) -> None:
        self.playing = not self.playing

        if self.playing:
            self.play()
        else:
            self.pause()

    def next(self) -> None:
        self._run_dbus_command("Next")

    def previous(self) -> None:
        self._run_dbus_command("Previous")

    def song_info(self) -> SongInfo:
        pass

    def _get_active_device(self) -> BluetoothDevice:
        devices = get_devices()
        for dev in devices:
            if dev.connected:
                return dev
    
    def _get_base_command(self) -> str:
        return f"dbus-send --system --print-reply --dest=org.bluez /org/bluez/hci0/dev_{self.device.get_dbus_address()}/player0"
    
    def _run_dbus_command(self, command: str) -> None:
        base = self._get_base_command()
        cmd = base + " " + f"{self.dbus_object}.{command}"

        print("Command:   " + cmd)

        subprocess.run(cmd.split(" "))


    def update_device(self) -> None:
        new_dev = self._get_active_device()
        if new_dev != None:
            self.device = self._get_active_device()


def run_with_timeout(command: str, timeout: float):
    subprocess.run(command.split(" "), timeout=timeout)