import pytest

class Graph:
    def __init__(self, routes):
        self.vertices = []
        self.graph_dict = {}

        for start, end in routes:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

        print(self.graph_dict)

    def get_paths(self, start, end, path=[]):

        path = path + [start]

        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return []
        
        paths = []
        
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node,end,path)
                for p in new_paths:
                    paths.append(p)
        return paths

    ##          Paris
    ## Mumbai  ─  |  ─  New York  ─  Toronto
    ##          Dubai

    def get_shortest_path(self, start, end, path=[]):

        path = path + [start]

        if start == end:
            return path
        if start not in self.graph_dict:
            return None

        shortest_path = None

        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node,end,path)
                if sp:
                    if shortest_path == None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path
    


if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    route_graph = Graph(routes)
    start = 'Mumbai'
    end = 'New York'
    #print(f"Available routes between {start} and {end}:", route_graph.get_paths(start,end))
    print(f"Shortest path between {start} and {end}:", route_graph.get_shortest_path(start, end))

@pytest.fixture
def sample_graph():
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
    return Graph(routes)

def test_get_paths(sample_graph):
    # Test case for getting all paths from Mumbai to New York
    paths = sample_graph.get_paths("Mumbai", "New York")
    assert paths == [
        ["Mumbai", "Paris", "Dubai", "New York"],
        ["Mumbai", "Paris", "New York"],
        ["Mumbai", "Dubai", "New York"]
    ], f"Expected different paths, but got {paths}"

    # Test case when start and end are the same
    same_node_path = sample_graph.get_paths("Mumbai", "Mumbai")
    assert same_node_path == [["Mumbai"]], f"Expected [['Mumbai']], but got {same_node_path}"

    # Test case when no path exists
    no_path = sample_graph.get_paths("Toronto", "Dubai")
    assert no_path == [], f"Expected no path, but got {no_path}"

def test_get_shortest_path(sample_graph):
    # Test case for getting shortest path from Mumbai to New York
    shortest_path = sample_graph.get_shortest_path("Mumbai", "New York")
    assert shortest_path == ["Mumbai", "Paris", "New York"], f"Expected shortest path to be ['Mumbai', 'Paris', 'New York'], but got {shortest_path}"

    # Test case when start and end are the same
    same_node_shortest_path = sample_graph.get_shortest_path("Mumbai", "Mumbai")
    assert same_node_shortest_path == ["Mumbai"], f"Expected ['Mumbai'], but got {same_node_shortest_path}"

    # Test case when no path exists
    no_shortest_path = sample_graph.get_shortest_path("Toronto", "Dubai")
    assert no_shortest_path is None, f"Expected None for no path, but got {no_shortest_path}"

def test_graph_initialization():
    routes = [
        ("A", "B"),
        ("A", "C"),
        ("B", "C"),
        ("C", "D")
    ]
    graph = Graph(routes)
    assert graph.graph_dict == {"A": ["B", "C"], "B": ["C"], "C": ["D"]}, f"Expected graph_dict to be {{'A': ['B', 'C'], 'B': ['C'], 'C': ['D']}}, but got {graph.graph_dict}"