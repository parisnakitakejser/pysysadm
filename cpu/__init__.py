import psutil

def count():
    cpu_logical = psutil.cpu_count(logical=False)
    cpu_cores = psutil.cpu_count(logical=True)

    return {
        'logical' : cpu_logical,
        'core' : cpu_cores,
    }

def procent(interval=0.1):
    cpu_procent_core = psutil.cpu_percent(interval=interval,percpu=True)
    cpu_procent_total = psutil.cpu_percent(interval=interval)

    core_load = {}

    for inx, core in enumerate(cpu_procent_core):
        core_load['core-{inx}'.format(inx=inx)] = core

    return {
        'total' : cpu_procent_total,
        'cores' : core_load
    }

def times():
    cpu_time = psutil.cpu_times()

    return {
        'user' : cpu_time.user,
        'nice' : cpu_time.nice,
        'system' : cpu_time.system,
        'idle' : cpu_time.idle,
    }
