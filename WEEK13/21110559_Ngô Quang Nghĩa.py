# Reversed IDA*
import copy
from typing import Type
import math
import numpy as np

INF = float(math.inf)
# Puzzle 3x4
h = 3
w = 4
class Node:
    def __init__(self, state, cost, parent_node, pos_action):
        self.state = state
        self.cost = cost
        self.parent_node = parent_node
        self.pos_action = pos_action
    def pos_actions(self):
        pos_actions= []
        node = self
        while node:
            if node.pos_action:
                pos_actions.append(node.pos_action)
            node = node.parent_node
        return list(reversed(pos_actions))

# Trạng thái đầu vào
state_input = [tuple(map(int, input().split())) for _ in range(3)]
state_input = tuple(state_input)
# Trạng thái mục tiêu
goal = ((0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11))

# Hoán đổi 2 trạng thái
state_input__reversed = goal
goal__reversed = state_input

# Truy xuất vị trí chính xác sử dụng từ điển nhanh hơn so với duyệt ma trận
true_pos = {v: (i, j) for i, row in enumerate(goal__reversed) for j, v in enumerate(row)} 

# Tính giá trị heuristic dựa trên tổng manhattan nhanh hơn so với sử dụng tổng Euclid
def heuristic(state):
    return sum(abs(i - true_pos[v][0]) + abs(j - true_pos[v][1])
               for i, row in enumerate(state) for j, v in enumerate(row) if v != 0)

def get_empty_tile_pos(state):
    for i in range(3):
        for j in range(4):
            if state[i][j] == 0:
                return (i, j)

def generate_childs(node):
    moves = ((-1,0), (0, 1), (1, 0), (0, -1))   
    empty_pos = get_empty_tile_pos(node.state) 
    for move in moves:
        i_af = empty_pos[0] + move[0]
        j_af = empty_pos[1] + move[1]
        if i_af >= 0 and i_af < 3 and j_af >= 0 and j_af < 4:
            state = list(copy.deepcopy(node.state))
            for i in range(3):
                state[i] = list(state[i])
            state[empty_pos[0]][empty_pos[1]] = state[i_af][j_af]
            state[i_af][j_af] = 0
            for i in range(3):
                state[i] = tuple(state[i])
            state = tuple(state)
            yield Node(state, node.cost + 1, node, (i_af, j_af))
 
# Reversed IDA*
def idas(node:Node,threshold):
    f = node.cost + heuristic(node.state)
    if f > threshold:
        return f
    if node.state == goal__reversed:
        global goal_node
        goal_node = node
        return -1
    min_f = INF
    for child_node in generate_childs(node):
       f = idas(child_node,threshold)
       if f == -1:
           return f
       elif f < min_f:
           min_f = f    
    return min_f           
          
root = Node(state_input__reversed, 0, None, None)
threshold = heuristic(root.state)
while True:
    f = idas(root,threshold)
    if f == INF or f == -1:
        break
    else:
        threshold = f   

# In action ra màn hình
if goal_node != None:
    actions = goal_node.pos_actions()
    actions.reverse()
    actions.pop(0) 
    actions.append(get_empty_tile_pos(state_input__reversed))
    for pos in actions:
        print(f"{pos[0]} {pos[1]}")


