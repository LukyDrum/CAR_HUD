uuids=$(bluetoothctl devices | cut -f2 -d' ')

for uuid in $uuids;
do
    bluetoothctl info $uuid
done | grep -e "Device\|Connected\|Name"