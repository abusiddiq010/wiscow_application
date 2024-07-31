import psutil
import logging
import os

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 90
LOG_FILE = "system_health.log"

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"CPU usage is above threshold: {cpu_usage}%")
    return cpu_usage

def check_memory():
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f"Memory usage is above threshold: {memory_usage}%")
    return memory_usage

def check_disk():
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f"Disk usage is above threshold: {disk_usage}%")
    return disk_usage

def check_processes():
    processes = len(psutil.pids())
    logging.info(f"Number of running processes: {processes}")
    return processes

def main():
    logging.info("Starting system health check")
    cpu_usage = check_cpu()
    memory_usage = check_memory()
    disk_usage = check_disk()
    processes = check_processes()

    logging.info(f"CPU Usage: {cpu_usage}%")
    logging.info(f"Memory Usage: {memory_usage}%")
    logging.info(f"Disk Usage: {disk_usage}%")

if __name__ == "__main__":
    main()
