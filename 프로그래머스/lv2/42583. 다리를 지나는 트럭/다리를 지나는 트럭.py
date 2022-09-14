from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    cnt = 0
    total_weight = 0
    in_bridge = deque([0 for _ in range(bridge_length)])


    while in_bridge:
        cnt += 1
        tmp = in_bridge.popleft()
        total_weight -= tmp

        if truck_weights:
            if truck_weights[0] + total_weight <= weight:
                truck = truck_weights.popleft()  
                in_bridge.append(truck)
                total_weight += truck
            else:
                in_bridge.append(0)
                
    return cnt