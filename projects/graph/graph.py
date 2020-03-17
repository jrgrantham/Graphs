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
            # add v2 to the vertices at v1
            self.vertices[v1].add(v2)
            # # add v1 to the vertices at v2 bidirectional or undirected
            # self.vertices[v2].add(v1)
        # otherwise
        else:
            # raise and exception and give an error
            raise IndexError("That vertex does not exist")

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
        # create empty queue enqueue the starting vertex id
        q = Queue()
        q.enqueue(starting_vertex)
        # create a set to store our visited vertices
        visited = set()

        # while queue is not empty (len greater than 0)
        while q.size() > 0:
            # dequeue the first vertex
            v = q.dequeue()
            # if that vertex has not been visited
            if v not in visited:
                # mark as visited and print for debugging
                visited.add(v)
                print(v) # for debugging
                # iterate over the child vertices of the current vertex
                for next_vertex in self.vertices[v]:
                    # enqueue the next vertex
                    q.enqueue(next_vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create empty stack push the starting vertex id
        s = Stack()
        s.push(starting_vertex)
        # create a set to store our visited vertices
        visited = set()

        # while stack is not empty (len greater than 0)
        while s.size() > 0:
            # pop the first vertex
            v = s.pop()
            # if that vertex has not been visited
            if v not in visited:
                # mark as visited and print for debugging
                visited.add(v)
                print(v) # for debugging
                # iterate over the child vertices of the current vertex
                for next_vertex in self.vertices[v]:
                    # push the next vertex
                    s.push(next_vertex)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # if the visited structure is set to None
        if visited is None:
            # create a new set for visited
            visited = set()
            
        
        # add a starting vertex to the visited set
        visited.add(starting_vertex)
        
        # print the start vertex
        print(starting_vertex)
        
        # loop over every child vertex in vertices set at the start vertex
        for child_vert in self.vertices[starting_vertex]:
            # if child vertex is not in visited
            if child_vert not in visited:            
                # do a recursive call to dft_recursive
                # using the child vertex and the current visited set as arguments
                self.dft_recursive(child_vert, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # firstly instantiate a Queue
        q = Queue()      
        # add a list containing the starting_vertex to the queue
        q.enqueue([starting_vertex])
        # instantiate empty set to hold visited vertices
        visited = set ()
        # while the length of the queue is more than zero
        while q.size() > 0:
            # set path equal to the first item in the queue (this will be a list containing all vertices within the current route)
            path = q.dequeue()
            # get the last element within the path list
            vert = path[-1]
            # check if the vertex has been visited before
            if vert not in visited:
                # if it is equal to the destination_vertex, we have reached our destination and can return the path
                if vert == destination_vertex:
                    return path
                # else, add it to visited
                visited.add(vert)
                # for every adjacent vertex of vert
                for adj_vert in self.vertices[vert]:
                    # copy the contents of the current path into new path and append the adjacent vertex
                    next_path = list(path)
                    next_path.append(adj_vert)
                    # add the new path to the queue
                    q.enqueue(next_path)
        # return False
        return False

    def dfs(self, starting_vertex, destination_vertex, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # firstly instantiate a Stack
        s = Stack()      
        # add a list containing the starting_vertex to the stack
        s.push([starting_vertex])
        # instantiate empty set to hold visited vertices
        visited = set ()
        # while the length of the stack is more than zero
        while s.size() > 0:
            # set path equal to the last item in the stack (this will be a list containing all vertices within the current route)
            path = s.pop()
            # get the last element within the path list
            vert = path[-1]
            # check if the vertex has been visited before
            if vert not in visited:
                # if it is equal to the destination_vertex, we have reached our destination and can return the path
                if vert == destination_vertex:
                    return path
                # else, add it to visited
                visited.add(vert)
                # for every adjacent vertex of vert
                for adj_vert in self.vertices[vert]:
                    # copy the contents of the current path into new path and append the adjacent vertex
                    next_path = list(path)
                    next_path.append(adj_vert)
                    # add the new path to the stack
                    s.push(next_path)
        # Return False
        return False

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # visited will be None on first pass
        if visited is None:
            # initalise it to list containing the initial starting_vertex
            visited = [starting_vertex]
        # the base case: is starting_vertex is equal to destination_vertex we have reached destination    
        if starting_vertex == destination_vertex:
            # return the list of vistited vertices
            return visited 
        # else for every neighbour of the current value of starting_vertex    
        for adjacent_vert in self.vertices[starting_vertex]:
            # if the neighbour has not been visited yet
            if adjacent_vert not in visited:
                # set the next_path equal to the value returned from recurring function passing in the neighbouring vertices as the starting_vert,
                # the destination_vertex and the concatenation of the current visited list with the adjacent vertex
                next_path = self.dfs_recursive(adjacent_vert, destination_vertex, visited + [adjacent_vert])
                # if next_path is not None 
                if next_path:
                    # return the next path
                    return next_path

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
    # print(graph.dfs_recursive(1, 6))
