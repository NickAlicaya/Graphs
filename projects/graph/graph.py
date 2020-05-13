"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()
        

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Vertex does not exist')    

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        qq = Queue()
        # add starting_vertex to Queue, note enqueue adds to the tail
        qq.enqueue(starting_vertex)
        # print({starting_vertex})
        # keep track of visited nodes
        visited = set()

        # repeat until queue is empty
        while qq.size() > 0:

            # dequeue first vert(remember dequeue pops the head)
            v = qq.dequeue()

            # if its not visited
            if v not in visited:
                print(v)
                # then adds or marks it as visited
                visited.add(v)

                for next_vert in self.get_neighbors(v):
                    qq.enqueue(next_vert)
                    # print({next_vert})


    def dft(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # s = Stack()
        print(starting_vertex)

        if visited is None:
            visited = set()

        visited.add(starting_vertex)

        for child in self.vertices[starting_vertex]:
            if child not in visited:
                self.dft_recursive(child, visited)    

  
    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # checks if visited is None then initiates as empty set()
        if visited is None:
            visited = set()

        print(starting_vertex)    

        # track visited nodes
        visited.add(starting_vertex)

        #call the function recursively
        for child in self.get_neighbors(starting_vertex):
            if child not in visited:
                self.dft_recursive(child, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue
        q = Queue()
        # enqueue A PATH TO the starting vertex ID
        q.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()

        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            cur_path = q.dequeue()
            print('CURRENT_PATH_XXXXXXX',cur_path)
            # Grab the last vertex from the PATH
            cur_path_last_vertex = cur_path[-1]
            # CHECK IF IT'S THE TARGET
            if cur_path_last_vertex == destination_vertex:
                # IF SO, RETURN PATH
                return cur_path

            # If that vertex has not been visited...
            if cur_path_last_vertex not in visited:
                    
           
                # Mark it as visited...
                visited.add(cur_path_last_vertex)

                # Then add A PATH TO its neighbors to the back of the queue
                for n in self.get_neighbors(cur_path_last_vertex):
                    # _COPY_ THE PATH
                    new_path = list(cur_path) 
                    # APPEND THE NEIGHOR 
                    new_path.append(n)
                    # add the new path
                    q.enqueue(new_path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])

        visited = set()

        while s.size() > 0:
            path = s.pop()
            # if last item in list of path not in visited
            if path[-1] not in visited:
                if path[-1] == destination_vertex:
                    return path

                visited.add(path[-1])

            for child in self.get_neighbors(path[-1]):
                # makes a copy of path
                new_path = list(path)
                # adds child to list
                new_path.append(child)
                # add to stack to keep while loop going
                s.push(new_path)        

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        if path is None:
            path = []
        
        visited.add(starting_vertex)
        # makes a copy of path
        new_path = path+[starting_vertex]

        if starting_vertex == destination_vertex:
            return new_path

        for child in self.get_neighbors(starting_vertex):
            if child not in visited:
                child_path = self.dfs_recursive(child, destination_vertex, visited, new_path)
                if child_path:
                    return child_path    

        return None
            

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
