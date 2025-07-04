from collections import deque

queue = deque([])

queue.append(1)
queue.append(2)
queue.append(55)

queue.popleft()
print(queue)

if not queue:
    print("empty")