import subprocess

from bluetooth.song_info import SongInfo
from bluetooth.device import BluetoothDevice, get_devices
from bluetooth.utils import pass_dbus_variant

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

    def _get_status(self) -> str:
        if self.device is None:
            return ""

        cmd = f"dbus-send --system --type=method_call --print-reply --dest=org.bluez /org/bluez/hci0/dev_{self.device.get_dbus_address()}/player0 org.freedesktop.DBus.Properties.Get string:org.bluez.MediaPlayer1 string:Status"

        # print("Command:   " + cmd)

        try:
            output = subprocess.check_output(cmd.split(" "), timeout=0.5)
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError):
            return ""

        return output.decode("utf-8").strip()

    def _get_track(self) -> str:
        if self.device is None:
            return ""

        cmd = f"dbus-send --system --type=method_call --print-reply --dest=org.bluez /org/bluez/hci0/dev_{self.device.get_dbus_address()}/player0 org.freedesktop.DBus.Properties.Get string:org.bluez.MediaPlayer1 string:Track"

        # print("Command:   " + cmd)

        try:
            output = subprocess.check_output(cmd.split(" "), timeout=0.5)
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError):
            return ""

        return output.decode("utf-8").strip()

    def update_device(self) -> None:
        new_dev = self._get_active_device()
        if new_dev != None:
            self.device = self._get_active_device()

    def get_song_info(self) -> SongInfo:
        string = self._get_track()

        if string == "":
            return SongInfo("", "", "")

        song_dictionary = pass_dbus_variant(string, ["Title", "Artist", "Album"])

        return SongInfo(song_dictionary["Title"], song_dictionary["Artist"], song_dictionary["Album"])

    def update_playing_status(self) -> None:
        self.playing = "playing" in self._get_status()


def run_with_timeout(command: str, timeout: float):
    subprocess.run(command.split(" "), timeout=timeout)