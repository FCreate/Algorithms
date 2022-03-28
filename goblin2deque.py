from collections import deque

firstDeque = deque()
secondDeque = deque()

n = int(input())
for _ in range(n):
    q = input().split()
    #print(q)
    if q[0] == "+":
        #queues are not empty
        if len(firstDeque) == 0:
            firstDeque.append(int(q[1]))
            continue
        if len(secondDeque) == 0:
            secondDeque.append(int(q[1]))
            continue
        if len(firstDeque) > len(secondDeque):
            #queue is even
            secondDeque.append(int(q[1]))
        else:
            valGob = secondDeque.popleft()
            firstDeque.append(valGob)
            secondDeque.append(int(q[1]))
    elif q[0] == "*":
        if len(firstDeque) == 0:
            firstDeque.append(int(q[1]))
            continue
        if len(secondDeque) == 0:
            secondDeque.append(int(q[1]))
            continue
        if len(firstDeque) > len(secondDeque):
            #queue is even
            secondDeque.appendleft(int(q[1]))
        else:
            firstDeque.append(int(q[1]))
    else:
        #get element
        if len(firstDeque) == 0:
            print(secondDeque.popleft())
            continue
        if len(firstDeque) > len(secondDeque):
            print(firstDeque.popleft())
        else:
            print(firstDeque.popleft())
            if len(secondDeque)!=0:
                val = secondDeque.popleft()
                firstDeque.append(val)


