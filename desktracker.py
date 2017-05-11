import time
import datetime
from bluetooth.ble import DiscoveryService

file = open( "myaddr.txt", "r" )

target_name = "Charge 2"
target_address = str( file.read() )

print "target_address: ", target_address

#This is only for low enery bluetooth devices
service = DiscoveryService()

while True:

    #Do this every 5 minutes
    devices = service.discover(2)

    for address, name in devices.items():
        print "found address, ", address
        if address == target_address:
            print "addresses equal"
        else:
            print address,"!=",target_address

#    print "You are away", datetime.datetime.now()
    time.sleep(5)



file.close()
