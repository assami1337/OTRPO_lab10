from prometheus_client import start_http_server, Gauge
import psutil
import os
import time

CPU_USAGE = Gauge('cpu_usage', 'CPU usage per core', ['core'])
MEMORY_TOTAL = Gauge('memory_total', 'Total memory in OS')
MEMORY_USED = Gauge('memory_used', 'Used memory in OS')
DISK_TOTAL = Gauge('disk_total', 'Total disk space', ['mountpoint'])
DISK_USED = Gauge('disk_used', 'Used disk space', ['mountpoint'])


def collect_metrics():
    cpu_percentages = psutil.cpu_percent(percpu=True)
    for i, percentage in enumerate(cpu_percentages):
        CPU_USAGE.labels(core=i).set(percentage)

    mem = psutil.virtual_memory()
    MEMORY_TOTAL.set(mem.total)
    MEMORY_USED.set(mem.used)

    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            DISK_TOTAL.labels(mountpoint=partition.mountpoint).set(usage.total)
            DISK_USED.labels(mountpoint=partition.mountpoint).set(usage.used)
        except PermissionError:
            continue


if __name__ == '__main__':
    HOST = os.getenv('EXPORTER_HOST', '0.0.0.0')
    PORT = int(os.getenv('EXPORTER_PORT', 8000))

    start_http_server(PORT, addr=HOST)
    print(f'Exporter запущен на {HOST}:{PORT}')

    while True:
        collect_metrics()
        time.sleep(5)