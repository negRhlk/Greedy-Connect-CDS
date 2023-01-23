"""
The setting of the network is determined in this file.
For plugging in static models and using static algorithms in the network design-time you can use the initializer.py file
"""

import random
import networkx as nx
import numpy as np
from node import node
from detect_neighbor import detect_neighbor
from choice_feature import choice_feature
import matplotlib.pyplot as plt
import math
from pylab import plot, show, savefig, xlim, figure, \
    ylim, legend, boxplot, setp, axes

# ---------------------------- global variables -------------------------------
global update_mobility_interval, lowpower_Poll_interval
global BUFFER_SIZE, reception_ratio
global NUMBER_NODES, ENVIRONMENT, NUMBER_RELAY_NODE, NUMBER_RELAY_G_NODE
global heartbeat_log, logger, energy_log, mobility_flag, R_h, x, y, next_update, Relay_Node, Relay_G_Node
global NETWORK_TTL, PACKET_LENGTH, EXECUTION_TIME, TOTAL_LOG, BYTE, DATA_RATE, SCAN_STEP, SWITCH_TIME
global Advertise_time, Receive_Delay, sleep_time, Receive_window, destination, max_seq
global GENERATION_EVENT_Adv37, HEARTBEAT_EVENT_Adv37, RELAY_EVENT_Adv37, AD38_EVENT, AD39_EVENT, AD39_EVENT_End
global SCAN37_EVENT, SCAN38_EVENT, SCAN39_EVENT, SCAN37_C_EVENT, SCAN38_C_EVENT, SCAN39_C_EVENT, SWITCH_37TO38
global SWITCH_38TO39, SEND_POLL, FRIEND_RELAY, NODE_TIME, NODE_EVENT, Time, i_node
global SINK_NODE, JUST_RELAY, JUST_GENERATION, RELAY_AND_GENERATION, LOW_POWER, FRIEND_RELAY_NODE, FRIEND_NODE
global nodes, Center_node, Center_node_static, Show_progress_interval, Show_progress

# -----------------------------------------------------------------------------
# ----------------------------- initial settings -------------------------------
# --------------------------- deployment setting ------------------------------
NUMBER_NODES = 200  # the number of nodes in the network
x = []  # the positions of nodes in the network
y = []

# The size of the environment that the network nodes are spread in it, 
# in this case, is 25*25 meters
ENVIRONMENT = 120

# -----------------------------------------------------------------------------
# The radius of the node communication range
NODE_RANGE = 11.26

Gar = nx.Graph()
Relay_Node = []
Relay_G_Node = []

# -----------------------------------------------------------------------------
random_network = 0

# Random topology
if random_network == 0:

    # x = [16, 22, 2, 3, 12, 7, 19, 1, 23, 17, 4, 7, 21, 3, 20, 13, 15, 16, 5, 8, 6, 22, 5, 11, 18, 20, 6, 2, 5, 1, 5, 4,
    #      23, 6, 19, 5, 4, 6, 10, 6, 18, 2, 2, 5, 16, 25, 9, 14, 13, 8, 3, 5, 1, 10, 22, 3, 8, 9, 22, 5, 14, 25, 12, 1,
    #      4, 3, 1, 19, 22, 22, 19, 9, 22, 25, 25, 14, 11, 6, 9, 12, 23, 4, 9, 21, 1, 20, 21, 10, 6, 10, 14, 6, 18, 23, 5,
    #      12, 15, 12, 9, 2]
    # y = [7, 24, 21, 18, 14, 24, 17, 20, 5, 20, 12, 12, 15, 12, 1, 1, 20, 8, 15, 3, 25, 8, 12, 5, 9, 15, 23, 1, 24, 11,
    #      4, 23, 13, 13, 4, 24, 13, 16, 23, 16, 6, 24, 6, 14, 18, 21, 6, 22, 12, 6, 5, 21, 3, 7, 19, 19, 13, 8, 13, 6, 7,
    #      20, 22, 3, 24, 10, 7, 5, 2, 4, 16, 1, 13, 16, 13, 12, 12, 15, 21, 3, 16, 19, 2, 4, 6, 21, 4, 2, 16, 22, 12, 17,
    #      3, 22, 19, 5, 10, 21, 7, 16]

    # 200 nodes in 120 * 120 environment
    x = [17, 9, 59, 22, 62, 16, 62, 29, 55, 79, 22, 33, 41, 1, 79, 48, 65, 33, 66, 72, 37, 14, 59, 3, 70, 20, 73, 21,
         72, 15, 20, 7, 52, 25, 45, 72, 8, 71, 80, 9, 79, 47, 49, 3, 28, 64, 32, 19, 45, 16, 15, 44, 58, 78, 3, 70, 66,
         47, 63, 29, 12, 72, 66, 54, 35, 76, 35, 21, 72, 7, 9, 73, 45, 3, 22, 36, 29, 68, 12, 80, 43, 26, 33, 19, 50,
         21, 31, 21, 26, 16, 41, 38, 77, 79, 78, 36, 68, 62, 48, 17, 62, 47, 62, 72, 102, 87, 41, 53, 82, 96, 78, 115,
         40, 57, 94, 89, 45, 73, 115, 62, 88, 100, 46, 98, 62, 64, 81, 57, 116, 70, 80, 43, 67, 49, 90, 105, 58, 58, 90,
         93, 48, 106, 104, 66, 44, 89, 45, 60, 44, 44, 83, 100, 118, 89, 101, 71, 46, 53, 63, 51, 78, 54, 106, 109, 62,
         68, 51, 95, 89, 107, 42, 114, 114, 81, 60, 65, 109, 78, 110, 120, 107, 92, 85, 48, 73, 72, 55, 100, 75, 105,
         90, 113, 113, 112, 85, 68, 45, 89, 87, 90]
    y = [31, 9, 30, 52, 58, 20, 63, 15, 70, 40, 37, 53, 47, 76, 4, 44, 73, 58, 7, 27, 12, 6, 71, 37, 52, 25, 43, 4, 4,
         50, 51, 64, 25, 48, 30, 33, 4, 3, 67, 60, 54, 13, 51, 75, 23, 79, 8, 46, 41, 59, 2, 43, 41, 70, 11, 7, 79, 28,
         46, 46, 78, 63, 20, 21, 26, 38, 35, 24, 6, 30, 19, 16, 55, 59, 6, 22, 53, 74, 69, 21, 31, 38, 12, 5, 23, 67,
         53, 39, 55, 19, 21, 56, 50, 38, 2, 19, 27, 77, 8, 78, 46, 70, 50, 51, 94, 85, 91, 58, 83, 45, 53, 108, 87, 55,
         107, 42, 51, 102, 116, 117, 100, 104, 43, 72, 86, 43, 101, 87, 65, 112, 90, 114, 53, 113, 78, 109, 95, 66, 62,
         90, 65, 110, 99, 120, 71, 55, 93, 106, 41, 82, 52, 56, 100, 91, 97, 80, 101, 112, 72, 54, 62, 73, 59, 112, 91,
         40, 99, 101, 107, 65, 95, 47, 70, 110, 43, 83, 63, 65, 89, 93, 115, 56, 88, 115, 120, 113, 94, 58, 76, 119, 76,
         79, 75, 57, 74, 87, 47, 90, 99, 40]

# Grid topology
else:
    for i17 in range(int(NUMBER_NODES / math.sqrt(NUMBER_NODES)) + 5):
        for j17 in range(int(NUMBER_NODES / math.sqrt(NUMBER_NODES))):
            # x = random.randint(1,ENVIRONMENT)
            x.append(9 * i17)
            # y = random.randint(1,ENVIRONMENT)
            y.append(9 * j17)

# ------------------------------ Node Initializing ----------------------------
nodes = []

for i1 in range(NUMBER_NODES):
    # the positions of the nodes adds to them
    nodes.append(node(i1, x[i1], y[i1]))
    # the positions of the nodes add to the network topology
    Gar.add_node(nodes[i1].ID, pos=(nodes[i1].Xposition, nodes[i1].Yposition))

# ----------------------------- Statice Algorithms ----------------------------
# ------------------------------ Detect Neighbour -----------------------------
# by calling the detect_neighbour function the neighbors of each node is determined
for node_source in range(NUMBER_NODES):
    neighbor = detect_neighbor(node_source, NODE_RANGE, NUMBER_NODES, nodes, Gar)
    nodes[node_source].neighbors = neighbor

# print(nodes[8].neighbors)
# ----------------------------- Relay Node Selection -----------------------------

# # Dividing nodes into 16 groups based on their position
# divs = dict()
# steps = 10
# for i in range(NUMBER_NODES):
#     divs[i] = []
#
# for i in range(0, ENVIRONMENT + 1, steps):
#     for k in range(NUMBER_NODES):
#         if i <= nodes[k].Xposition < i + steps:
#             divs[i].append(nodes[k].ID)
#
# divs_list = []
#
# for key in divs:
#     if divs[key] != []:
#         divs_list.append(divs[key])
#
#
# # Creating a 2D list with the length of len(div_list) * len(div_list)
# new_list_div = []
# for i in range(len(divs_list)):
#     new_list_div.append([])
#     for j in range(len(divs_list)):
#         new_list_div[i].append([])
#
# for i in range(len(new_list_div)):
#     for m in range(len(divs_list[i])):
#         for k in range(0, ENVIRONMENT + 1, steps):
#             if k <= nodes[m].Yposition < k + steps:
#                 index = k // steps
#                 new_list_div[i][index].append(nodes[m].ID)
#
# count = 0
# for i in range(len(new_list_div)):
#     for j in range(len(new_list_div[i])):
#         count += len(new_list_div[i][j])
# print(count)
# print(new_list_div)

# -------------------------- Connected Dominating Set -------------------------

# for nod in nodes:
#     if nod.COLOR == "yellow":
#         node_white_count = len(nod.neighbors)  # white_count of the nod
#         dominator = True
#
#         # calculating the white_count of nod's neighbours
#         for nbr in nod.neighbors:
#             if len(nodes[nbr].neighbors) > node_white_count:
#                 dominator = False
#                 break
#         if dominator:
#             nod.COLOR = "black"
#             for nbr in nod.neighbors:
#                 nodes[nbr].COLOR = "grey"

# --------- Greedy construction of a dominating set - Phase 1 ------------
for nod in nodes:
    node_white_count = 0  # white_count of the nod

    if nod.COLOR == "yellow":
        # Calculating the white_count of the nod
        for i in nod.neighbors:
            if nodes[i].COLOR == "yellow":
                node_white_count += 1
        dominator = True  # A flag for defining the nod as a dominator

        nbr_white_count = {}  # For saving neighbours white_count in a dictionary
        for i in nod.neighbors:
            whites = 0
            for j in nodes[i].neighbors:
                if nodes[j].COLOR == "yellow":
                    whites += 1
            nbr_white_count[i] = whites

        for nbr in nod.neighbors:
            if nbr_white_count[nbr] > node_white_count:
                dominator = False
                break
        if dominator:
            nod.COLOR = "black"
            for nbr in nod.neighbors:
                nodes[nbr].COLOR = "grey"

# --------- Greedy construction of a dominating set - Phase 2 ------------
for nod in nodes:
    node_white_count = 0
    if nod.COLOR == "yellow":
        # Calculating the white_count of the nod
        for i in nod.neighbors:
            if nodes[i].COLOR == "yellow":
                node_white_count += 1

        nbr_white_count = {}  # For saving neighbours white_count in a dictionary
        for i in nod.neighbors:
            whites = 0
            for j in nodes[i].neighbors:
                if nodes[j].COLOR == "yellow":
                    whites += 1
            nbr_white_count[i] = whites

        nbr_white_count[nod.ID] = node_white_count

        temp = 0
        high = 0
        for key in nbr_white_count:
            if nbr_white_count[key] > temp:
                temp = nbr_white_count[key]
                high = key

        nodes[high].COLOR = "black"
        for nbr in nodes[high].neighbors:
            if nodes[nbr].COLOR == "yellow":
                nodes[nbr].COLOR = "grey"

# ----------------- Connecting the Dominating Set - Requirements -----------------
grey_nodes = []

# Setting grey nodes' component ID to 1
for nod in nodes:
    if nod.COLOR == "grey":
        nod.component = -1
        grey_nodes.append(nod)

# Setting black nodes' component ID
for nod in nodes:
    if nod.COLOR == "black":
        node_black_nbr = [-1]
        for i in nod.neighbors:
            if nodes[i].COLOR == "black":
                node_black_nbr.append(nodes[i].ID)
        if nod.ID > max(node_black_nbr):
            nod.component = nod.ID
        else:
            nod.component = max(node_black_nbr)
    # print(nod.ID, ':', nod.component)

# I HAVE A QUESTION!
# for i in range(NUMBER_NODES):
#     if nodes[NUMBER_NODES - 1 - i].COLOR == "black":
#         for j in nodes[NUMBER_NODES - 1 - i].neighbors:
#             if nodes[j].component > nodes[NUMBER_NODES - 1 - i].component:
#                 nodes[NUMBER_NODES - 1 - i].component = nodes[j].component
#         print(nodes[NUMBER_NODES - 1 - i].ID, ':', nodes[NUMBER_NODES - 1 - i].component)

# ----------------- Connecting the Dominating Set - Phase 1 -----------------
for nod in grey_nodes:
    # print(nod.ID)
    dominators = set()
    nodes_id = []
    for i in nod.neighbors:
        if nodes[i].COLOR == "black":
            dominators.add(nodes[i].component)
            nodes_id.append(nodes[i].ID)
    dominators = list(dominators)
    # print(dominators)

    if len(dominators) == 2:
        max_component = max(dominators)
        nod.COLOR = "black"
        nod.component = max_component
        for i in nodes_id:
            if nodes[i].component != max_component:
                nodes[i].component = max_component

# for i in range(NUMBER_NODES):
#     print(nodes[i].ID, ':', nodes[i].component)

# I HAVE A QUESTION!
# for i in range(NUMBER_NODES):
#     if nodes[NUMBER_NODES - 1 - i].COLOR == "black":
#         for j in nodes[NUMBER_NODES - 1 - i].neighbors:
#             if nodes[j].component > nodes[NUMBER_NODES - 1 - i].component:
#                 nodes[NUMBER_NODES - 1 - i].component = nodes[j].component
#         print(nodes[NUMBER_NODES - 1 - i].ID, ':', nodes[NUMBER_NODES - 1 - i].component)

# ----------------- Connecting the Dominating Set - Phase 2 -----------------
for u in nodes:
    if u.COLOR == "grey":
        for i in u.neighbors:
            if nodes[i].COLOR == "grey":
                highU = -1
                highV = -1

                for j in u.neighbors:
                    if nodes[j].component > highU:
                        highU = nodes[j].component

                for j in nodes[i].neighbors:
                    if nodes[j].component > highV:
                        highV = nodes[j].component

                if highU != highV:
                    # print('u: ', u.ID, 'highU: ', highU)
                    # print('v: ', nodes[i].ID, 'highV: ', highV)
                    # print("----------------------")

                    u.COLOR = "black"
                    nodes[i].COLOR = "black"

                    u.component = max([highU, highV])
                    nodes[i].component = max([highU, highV])
                break
            break

# for i in range(NUMBER_NODES):
    # if nodes[NUMBER_NODES - 1 - i].COLOR == "black":
    #     for j in nodes[NUMBER_NODES - 1 - i].neighbors:
    #         if nodes[j].component > nodes[NUMBER_NODES - 1 - i].component:
    #             nodes[NUMBER_NODES - 1 - i].component = nodes[j].component
    #         else:
    #             nodes[j].component = nodes[NUMBER_NODES - 1 - i].component
    # print(nodes[NUMBER_NODES - 1 - i].ID, ':', nodes[NUMBER_NODES - 1 - i].component)
for i in range(NUMBER_NODES):
    if nodes[i].COLOR == "black":
        Relay_Node.append(nodes[i].ID)

print(Relay_Node)
# --------------------------- Plot Network Topology ---------------------------
# print(nx.info(Gar))
fig = figure()  # it is possible to use figsize=(num, num)
color = [nodes[i].COLOR for i in range(NUMBER_NODES)]

pos = {}
for i in range(len(Gar.nodes)):
    pos[i] = np.array([nodes[i].Xposition, nodes[i].Yposition])

nx.draw(Gar, pos=pos, with_labels=True, node_color=color)
plt.savefig('topology.png', dpi=200, bbox_inches='tight')
# plt.show()
