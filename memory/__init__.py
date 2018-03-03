import psutil

def status():
    mem = psutil.virtual_memory()

    return {
        'total' : mem.total,
        'procent_used' : mem.percent,
        'free' : mem.free,
        'available' : mem.available,
        'used' : mem.used,
        'active' : mem.active,
        'inactive' : mem.inactive,
        'wired' : mem.wired,
    }
