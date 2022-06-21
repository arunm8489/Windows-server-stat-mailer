import psutil

# function returning time in hh:mm:ss
def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)


def fetch_space():
    stats = {'space':{},
             'mounts': [],
             'battery':{}}

    #fetch space related information
    hdd = psutil.disk_usage('/')
    total_space =  hdd.total / (2**30)
    used_space =  hdd.used / (2**30)
    free_space = hdd.free / (2**30)
    stats['space']['total_space'] = total_space
    stats['space']['used_space'] = used_space
    stats['space']['free_space'] = free_space

    
    #get disk partitions
    disk_partition = psutil.disk_partitions()
    for i in disk_partition:
        stats['mounts'].append(i[0])


    # battery health
    battery = psutil.sensors_battery()
    bat_percent = battery.percent
    is_plugged = battery.power_plugged
    remaining_battery = convertTime(battery.secsleft)

    stats['battery']['percent'] = bat_percent
    stats['battery']['is_plugged'] = is_plugged

    return stats

if __name__=="__main__":
    x = fetch_space()
    print(x)
