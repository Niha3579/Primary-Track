import psutil # type: ignore
import time

def system_monitor(interval=3):
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        print("System Usage Monitor")
        print(f"CPU Usage    : {cpu}%")
        print(f"Memory Usage : {memory}%")
        print(f"Disk Usage   : {disk}%")

system_monitor()
