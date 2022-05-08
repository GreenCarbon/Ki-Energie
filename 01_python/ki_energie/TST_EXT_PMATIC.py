


import pmatic
# PMATIC vorerst nicht benutzen, das funktioniert nicht sauber mit unserer Homematic-Version



#import ssl

#ssl._create_default_https_context = ssl._create_unverified_context

ccu = pmatic.CCU(address="http://192.168.20.54", credentials=("Admin", "Ki#Energie"))
#ccu = pmatic.CCU(address="http://192.168.20.205", credentials=("Karsten", "ia2g4ayh"))
ccu.api.print_methods()

for room in ccu.rooms:
    print(room.name)
#for device in ccu2.room.devices:
#    print("  %s: %s" % (device.name, device.summary_state))
        
#for device in ccu1.devices.query():
#for device in ccu1.devices:
#    print("%-20s %6s" % (device.name, device.is_open and "open" or "closed"))
    
print("Low battery: ")
for device in ccu.devices:
    if device.is_battery_low:
        print("  %s" % device.name)
else:
    print("  All battery powered devices are fine.")   