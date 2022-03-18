# coding utf-8
import numpy as np
import heapq

def shortestpath_tree(neiList, nei_edge_len, orient):
    """
    this function builds the shortest path tree rooted the orient by Dijkstra method
    :param neiList: dictionary, neighborhood list
    :param nei_edge_len: dictionary, distance list
    :param orient: int, the index of the orient
    :return:
    """
    node_num = len(neiList)
    Q = []
    distance = [float("inf")] * node_num
    previous_nodes = [-1] * node_num
    distance[orient] = 0

    for i in range(node_num):
        heapq.heappush(Q, (distance[i], i)) # for fast finding of minimum

    searched = set()

    while len(searched) != node_num:
        u = heapq.heappop(Q)
        searched.add(u[1])
        target_edge = nei_edge_len[u[1]]
        for i, length in enumerate(target_edge):
            if neiList[u[1]][i] in searched:
                pass
            else:
                possible_min_distance = distance[u[1]] + length
                if possible_min_distance < distance[neiList[u[1]][i]]:
                    distance[neiList[u[1]][i]] = possible_min_distance
                    previous_nodes[neiList[u[1]][i]] = u[1] # memorize the previous node of u[1] on the shortest path tree
                    heapq.heappush(Q, (distance[neiList[u[1]][i]], neiList[u[1]][i]))

    return previous_nodes

def get_shortestpath(shortest_path_tree, destination):
    """
    this func reads the shortest path tree backward
    :param shortest_path_tree: list, return of shortestpath_tree()
    :param destination: int, the index of the orient
    :return:
    """
    previous_node = destination
    route = []
    while previous_node != -1:
        route.append(previous_node)
        previous_node = shortest_path_tree[previous_node]
    return route[::-1]

def get_path_length(path, neiList, nei_edge_len):
    """
    this func calculate the total length of the path
    :param path: list, return of get_shortestpath()
    :param neiList: dictionary, neighborhood list
    :param nei_edge_len: dictionary, distance list
    :return:
    """
    sp_l = 0.0
    if len(path) == 1: # the orient and the destination are not connected
        sp_l = float("inf")
    else:
        for i in range(len(path)-1):
            start = path[i]
            end = path[i+1]
            l = nei_edge_len[start][neiList[start].index(end)]
            sp_l += l
    return sp_l

### network data ###
neiList = {0: [1, 8, 9],
           1: [0, 3, 5, 8, 9],
           2: [3, 4, 6, 7],
           3: [1, 2, 5, 6, 7, 9],
           4: [2, 6, 9],
           5: [1, 3, 7, 8],
           6: [2, 3, 4, 9],
           7: [2, 3, 5, 8],
           8: [0, 1, 5, 7],
           9: [0, 1, 3, 4, 6]}
nei_edge_len = {0: [40, 60, 70],
                1: [40, 75, 35, 45, 75],
                2: [20, 85, 75, 40],
                3: [75, 20, 50, 60, 40, 80],
                4: [85, 15, 50],
                5: [35, 50, 35, 55],
                6: [75, 60, 15, 45],
                7: [40, 40, 35, 85],
                8: [60, 45, 55, 85],
                9: [70, 75, 80, 50, 45]}

if __name__ == "__main__":
    ### Dijkstra method ###
    # the shortest path tree #
    spt = shortestpath_tree(neiList, nei_edge_len, orient=0)
    # the shortest path from 0 to 7
    sp = get_shortestpath(spt, destination=7)
    print("the shortest path from 0 to 7: ", sp)
    # the length of the shortest path from 0 to 7 #
    l = get_path_length(sp, neiList, nei_edge_len)
    print("length: ", l)