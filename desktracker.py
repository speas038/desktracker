import time
import datetime
from bluetooth.ble import DiscoveryService


SLEEP_INTERVAL = 5
DEV_ADDRESS_CFG_LOC = "./dev_mac.txt"


file = open( DEV_ADDRESS_CFG_LOC, "r" )

target_name = "Charge 2"
target_address = str.strip( file.read() )

print "target_address: ", target_address
print "target_name: ", target_name

#This is only for low enery bluetooth devices
service = DiscoveryService()

while True:

    device_present = False

    devices = service.discover(2)

    for address, name in devices.items():
        address = str.strip( address )
        name = str.strip( name )
        
        if address == target_address     \
            and target_name == name:
            
            device_present = True

    if device_present == True:
        print "Device Present"
    else:
        print "Device away"

#    print "You are away", datetime.datetime.now()
    time.sleep( SLEEP_INTERVAL )



file.close()
