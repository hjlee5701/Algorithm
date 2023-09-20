import sys


def up_heapify(queue):
    child_index = len(queue) - 1
    while child_index != 0:
        parent_index = (child_index - 1) // 2
        if queue[parent_index] < queue[child_index]:
            queue[parent_index], queue[child_index] = queue[child_index], queue[parent_index]
            child_index = parent_index
        else:
            return

def down_heapify(queue):
    parent = 0
    bigger_child = find_bigger_child_index(parent, queue)

    while parent != bigger_child:
        queue[parent], queue[bigger_child] = queue[bigger_child], queue[parent]
        parent = bigger_child
        bigger_child = find_bigger_child_index(parent, queue)

def find_bigger_child_index(parent, queue):
    left_child = parent * 2 + 1
    right_child = parent * 2 + 2

    if left_child < len(queue) and queue[parent] < queue[left_child]:
        parent = left_child
    if right_child < len(queue) and queue[parent] < queue[right_child]:
        parent = right_child
    return parent


N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap) == 0:
            print(0)
            continue
        else:
            print(heap[0])
            heap[0] = heap[len(heap)-1]
            heap.pop()  # heap[1]에 heap.pop()값을 바로 넣게 되면 원소가 하나 남았을 때 오류 발생
            down_heapify(heap)
    else:
        heap.append(x)
        up_heapify(heap)