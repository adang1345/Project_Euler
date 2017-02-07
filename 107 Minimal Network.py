import queue


class Graph:
    def __init__(self, v, e):
        """Initialize vertices and edges. v is a set of Vertices, and e is a set of Edges."""
        for x in v:
            assert isinstance(x, Vertex)
        for x in e:
            assert isinstance(x, Edge)
        self.v = v
        self.e = e

    def __repr__(self):
        return repr(self.v) + "\n" + repr(self.e)

    def add_edge(self, edge):
        """Add edge u to the graph.
        Precondition: u is an Edge whose vertices are part of this graph"""
        assert isinstance(edge, Edge)
        self.e.add(edge)

    def neighbors(self, u):
        """Return the set of neighbors of vertex u.
        Precondition: u is part of this graph"""
        assert isinstance(u, Vertex)
        n = set()
        for edge in self.e:
            if u in edge.vertices:
                n.add(next(iter(edge.vertices.difference({u}))))
        return n

    def component(self, u):
        """Return the component of the graph that contains vertex u.
        Precondition: u is part of this graph"""
        assert isinstance(u, Vertex)
        reachable = {u}
        to_check = queue.Queue(-1)
        for n in self.neighbors(u):
            to_check.put(n)
        while not to_check.empty():
            a = to_check.get()
            if a not in reachable:
                reachable.add(a)
                for n in self.neighbors(a):
                    to_check.put(n)
        return reachable

    def total_weight(self):
        """Return the total weight of the edges"""
        return sum(edge.weight for edge in self.e)


class Vertex:
    def __init__(self, name):
        """Initialize a Vertex.
        Precondition: name is an int"""
        assert type(name) == int
        self.name = name

    def __repr__(self):
        return "Vertex" + str(self.name)


class Edge:
    def __init__(self, vertices, weight):
        """Initialize an Edge.
        Precondition: vertices is a set of two Vertices, weight is an int"""
        for x in vertices:
            assert isinstance(x, Vertex)
        assert len(vertices) == 2
        assert type(weight) == int
        self.vertices = vertices
        self.weight = weight

    def __lt__(self, other):
        """Allow edges to be sorted by weight"""
        return self.weight < other.weight

    def __repr__(self):
        return "(" + repr(self.vertices) + "," + repr(self.weight) + ")"


# read file into a 2D list of strings, which represents a distance matrix
g1 = open("107 Network.txt").read().split()
g2 = [row.split(",") for row in g1]

# construct graph from distance matrix
vertices = []
edges = set()
for n in range(len(g2)):
    vertices.append(Vertex(n))
for n in range(len(vertices)):
    for potential_neighbor in range(n):
        if g2[n][potential_neighbor] != "-":
            new_edge = Edge({vertices[n], vertices[potential_neighbor]}, int(g2[n][potential_neighbor]))
            edges.add(new_edge)
vertices = set(vertices)
graph = Graph(vertices, edges)
original_weight = graph.total_weight()
print("Original Weight: " + str(original_weight))

# perform Kruskal's algorithm
tree = Graph(vertices, set())
edges = list(edges)
edges.sort()
for edge in edges:
    edge_vertices = list(edge.vertices)
    if edge_vertices[0] not in tree.component(edge_vertices[1]):
        tree.add_edge(edge)
optimal_weight = tree.total_weight()
print("Optimal Weight: " + str(optimal_weight))
print("Saved Weight: " + str(original_weight - optimal_weight))
