import os
import psutil
import sys
import time
import datetime

old_vms = 0
log = open("log.log", "a")
i = 0
time_step = 10

while (1):    
    process = psutil.Process(int(sys.argv[1]))
    vms = process.memory_info().vms
    timing = datetime.datetime.now()
    diff_vms = vms - old_vms
    percent_vms = (float(diff_vms) / vms) * 100
    if (i % time_step == 0):
        print (timing)
    print ("vms: {0}".format(vms))
    print ("old_vms: {0}".format(old_vms))
    print ("diff_vms: {0}".format(diff_vms))
    print ("percent_vms: {0}%".format(percent_vms))
    print ("")
    if (i % time_step == 0):
        log.write("{0}\n".format(timing))
    log.write("vms: {0}\n".format(vms))
    log.write("old_vms: {0}\n".format(old_vms))
    log.write("diff_vms: {0}\n".format(diff_vms))
    log.write("percent_vms: {0}%\n\n".format(percent_vms))
    time.sleep(1)
    old_vms = vms
    i += 1


log.close()
