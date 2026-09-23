import time
import psutil
while True:
    print("DevOps Health Monitor is running!")
    print("CPU Usage:", psutil.cpu_percent(), "%")
    print("Memory Usage:", psutil.virtual_memory().percent, "%")

    time.sleep(5)
