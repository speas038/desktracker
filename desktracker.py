import bluetooth

target_name = "Charge 2"
target_address = None


nearby_devices = bluetooth.discover_devices();

for baddr in nearby_devices:
    print bluetooth.lookup_name( baddr ), ": ", baddr
#    if target_name == bluetooth.lookup_name( baddr ):
#        target_address = baddr
#        break

#if target_address is not None:
#    print "found bluetooth address of ", target_name, target_address
#else:
#    print "Could not find address"
