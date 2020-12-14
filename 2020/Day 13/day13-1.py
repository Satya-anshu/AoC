lines = open('in.txt','r').readlines()
dep_time = int(lines[0].strip('\n'))
bus_service = lines[1].strip('\n').split(',')
bus_ids = []
print(bus_service)
for bus in bus_service:
    if bus != 'x':
        bus_ids.append(bus)
wait_times = []
lowest_wait = [10**10, 0]
for time in bus_ids:
    time = int(time)
    q = dep_time // time
    wait = time * q
    if wait < dep_time:
        wait += time
    if wait-dep_time < lowest_wait[0]:
        lowest_wait = [wait-dep_time, time]
    wait_times.append([wait-dep_time, time])
print("Part 1: ", lowest_wait[0] * lowest_wait[1])

