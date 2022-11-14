from collections import deque

def solution(order):
    order = deque(order)
    main_box = deque([i for i in range(1,len(order)+1)])
    sub_box = []
    container = []

    for box in main_box:
        if sub_box and sub_box[-1] == order[0]:
            container.append(sub_box.pop())
            order.popleft()

        if box == order[0]:
            container.append(box)
            order.popleft()
        else:
            sub_box.append(box)

    while sub_box:
        sub_tmp = sub_box.pop()
        if sub_tmp == order[0]:
            order.popleft()
            container.append(sub_tmp)
        else:
            break

    return len(container)
