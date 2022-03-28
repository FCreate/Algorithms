from collections import deque
def add_twenty(hours, minutes):
    minutes = minutes + 20
    if minutes > 59:
        hours+=1
        minutes -=60
    return (hours, minutes)
def diff(date1, date2):
    hours = date2[0] - date1[0]
    if hours == 0:
        minutes = date2[1] - date1[1]
    else:
        minutes = 60*hours + date2[1] - date1[1]
    return minutes

n = int(input())
d = deque()
q = [int(elem) for elem in input().split()]
curr_time = (q[0], q[1])
deque.append((curr_time))
last_time = curr_time
isBusy = True
for _ in range(n-1):
    q = [int(elem) for elem in input().split()]
    if diff((q[0], q[1]), (curr_time)) > 20:

    deque.append()