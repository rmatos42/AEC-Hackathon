import os
import psutil
import sys
import time
import datetime

old_vms = 0
log = open("log.log", "a")
i = 0

while (1):    
    process = psutil.Process(int(sys.argv[1]))
    vms = process.memory_info().vms
    timing = datetime.datetime.now()
    if (i % 10 == 0):
        print timing
    print ("vms: {0}".format(vms))
    print ("old_vms: {0}".format(old_vms))
    print ("vms - old_vms: {0}".format(vms - old_vms))
    print ("")
    if (i % 10 == 0):
        log.write("{0}".format(timing))
    log.write("vms: {0}".format(vms))
    log.write("old_vms: {0}".format(old_vms))
    log.write("vms - old_vms: {0}".format(vms - old_vms))
    time.sleep(.1)
    old_vms = vms
    i += 1


log.close()
