from collections import deque

def minutes2hours(minutes):
    return divmod(minutes, 60)

class Barber:
    def __init__(self):
        self.time = 0
        self.busy = False
    def getVisitor(self, time):
        self.time = time
        self.busy = True
    def currTime(self):
        return self.time
    def cutTime(self):
        return self.time + 20
    def makeCut(self):
        self.time = self.time + 20
        self.busy = False
        return self.time

n = int(input())
d = deque()
res = [""] * n
idx = 0
b = Barber()
for i in range(n):
    hours, minutes, thresh = [int(elem) for elem in input().split()]
    time = 60 * hours + minutes
    if not b.busy:
        b.getVisitor(time)
    else:
        #barber is busy
        #empty queue
        #drop all
        while b.time+20 < time and len(d)>0:
            prev_time = b.makeCut()
            while res[idx] != "":
                idx += 1
            res[idx] = prev_time
            idx += 1
            time_new = d.popleft()
            b.getVisitor(max(prev_time, time))
        if len(d) > 1:
            numPeople = len(d) + 1
            if numPeople > thresh:
                res[i] = time
            else:
                d.append(time)
            continue
        elif len(d) == 1:
            if b.time+20 == d[0]:
                numPeople = 1
            else:
                numPeople = 2
            if numPeople > thresh:
                res[i] = time
            else:
                d.append(time)
        else:
            if b.busy:
                if b.time+20 <= time:
                    prev_time = b.makeCut()
                    while res[idx] != "":
                        idx += 1
                    res[idx] = prev_time
                    b.getVisitor(time)
                else:
                    if thresh != 0:
                        d.append(time)
                    else:
                        res[i] = time
            else:
                b.getVisitor(time)
while len(d)!=0:
    prev_time = b.makeCut()
    while res[idx] != "":
        idx += 1
    res[idx] = prev_time
    idx += 1
    time_new = d.popleft()
    b.getVisitor(max(prev_time, time))
prev_time = b.makeCut()
while res[idx] != "":
    idx += 1
res[idx] = prev_time

for elem in res:
    time =minutes2hours(elem)
    print(time[0], time[1])