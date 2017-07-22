import os
import psutil
import sys
process = psutil.Process(int(sys.argv[1]))
print(process.memory_info().rss)
