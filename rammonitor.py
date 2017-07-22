import os
import psutil
import sys
import time



# data = []
old_vms = 0
log = open("log.log", "a")
while (1):    
    process = psutil.Process(int(sys.argv[1]))
    vms = process.memory_info().vms
    # data.append(vms)
    print "vms:", vms
    print "old_vms:", old_vms
    print "vms - old_vms:", vms - old_vms
    print ""
    log.write("vms: {0}\n".format(vms))
    log.write("old_vms: {0}\n".format(old_vms))
    log.write("vms - old_vms: {0}\n\n".format(vms - old_vms))
    time.sleep(.1)
    old_vms = vms

log.close()
