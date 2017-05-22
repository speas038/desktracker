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

device_found = False

while True:

    devices = service.discover(2)

    if target_address in devices and devices[target_address] == target_name:
        
        if device_found == False:

            print "Device returned"
            device_found = True

    else:
            
        if device_found == True:

            print "Device Left"
            device_found = False


        

#    print "You are away", datetime.datetime.now()
    time.sleep( SLEEP_INTERVAL )

file.close()
