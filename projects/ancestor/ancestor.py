from utils import Queue,Stack,Graph


def earliest_ancestor(ancestors, starting_node):
    """
        10
     /
    1   2   4  11
     \ /   / \ /
      3   5   8
       \ / \   \
        6   7   9
    Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor – the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. If the input individual has no parents, the function should return -1.
    """
    # UPER
    # use bft
    # use len(longest)
    # if len(longest) == 1 then return -1
    # check the length of the set of vertices for the longest
    # if there is no child return -1
    # while there is an edge:
    # ancestor[0] is parent ancestor[1] is child         
  
        # starting node has no parent then return -1   
    
    # initialize with the starting node is equal to the child
    # after that the child becomes the parent
    

    # graph = Graph()
    # # relatives is a node
    # for relatives in ancestors:
    #     for relative in relatives:
    #         graph.add_vertex(relative)
    #         # print('GRAPHXXXXXX',graph.vertices)  

    # for relatives in ancestors:
    #     graph.add_edge(relatives[1],relatives[0]) 
    #     print('GRAPHXXXXXX',graph.vertices)  





    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        graph.add_edge(pair[1],pair[0])
        print('XXXXXVERTICESXXXX',graph.vertices)


    q = Queue()
    q.enqueue([starting_node])
    max_path_len = 1
    earliest_ancestor = -1

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]

        # if path is longer or equal and value is smaller, or path is longer
        if (len(path) >= max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
            earliest_ancestor = v
            max_path_len = len(path)    

        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)
    return earliest_ancestor            









    # graph = Graph()
    # # relatives is a node
    # for relatives in ancestors:
    #     for relative in relatives:
    #         graph.add_vertex(relative)
    #         # print('GRAPHXXXXXX',graph.vertices)  

    # for relatives in ancestors:
    #     graph.add_edge(relatives[1],relatives[0]) 
    #     print('GRAPHXXXXXX',graph.vertices)        

    # # default path length to compare to 
    # longest_path = 1
    # # default earliest ancestor to compare to
    # earliest_ancestor = -1
    # # initialize the path with a list containing the starting_node
    # last_node = 0
    # ancestors_vert = graph.vertices

    # for v in ancestors_vert:

    #     path = graph.dfs(starting_node, v)

    #     if path is not None and len(path) > longest_path:

    #         last_node = v
    #     elif not path and longest_path == 1:
    #         last_node = -1

    # return last_node        
   
        






