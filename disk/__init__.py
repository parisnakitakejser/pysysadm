import psutil

def partitions():
    disk_partitions = psutil.disk_partitions()

    disks = []
    for inx, dpart in enumerate(disk_partitions):
        disk_usage = psutil.disk_usage(dpart.device)

        disks.append({
            'device' : dpart.device,
            'mountpoint' : dpart.mountpoint,
            'fstype' : dpart.fstype,
            'opts' : dpart.opts,
            'usage' : {
                'total' : disk_usage.total,
                'used' : disk_usage.used,
                'free' : disk_usage.free,
                'percent_used' : disk_usage.percent,
            }
        })

    return disks
